from typing import List
from chalicelib.challenge import ChallengeSolver


class InvalidNumberError(Exception):
    def __init__(self, num):
        super().__init__(str(num))
        self.num = num


class XmasValidator:

    def __init__(self, preamble):
        self.prev_nums = list(preamble)

    def validate_next(self, num):
        for prev_num in self.prev_nums:
            if num - prev_num in self.prev_nums:
                self.prev_nums = self.prev_nums[1:] + [num]
                return
        raise InvalidNumberError(num)


class EncodingError(ChallengeSolver):
    day = 9
    nums: List[int]
    _preamble_size: int = 25

    def __init__(self, input: bytes):
        lines = input.decode('utf-8').splitlines()
        # This is a custom extension to the format for Day 9 to support
        # processing the given sample data, which uses a different
        # preamble length.
        if lines[0].startswith('#'):
            self._preamble_size = int(lines[0][1:].strip())
            lines = lines[1:]
        self.nums = [int(num) for num in lines]

    def solve_a(self):
        validator = XmasValidator(self.nums[:self._preamble_size])
        try:
            for num in self.nums[self._preamble_size:]:
                validator.validate_next(num)
        except InvalidNumberError as answer:
            return answer.num
        return -1
    
    def solve_b(self):
        target_answer = self.solve_a()
        for section_size in range(2, len(self.nums)):
            for section in zip(*(self.nums[start:] for start in range(section_size))):
                if sum(section) == target_answer:
                    return min(section) + max(section)
        return -1