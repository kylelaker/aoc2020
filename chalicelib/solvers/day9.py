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

    def __init__(self, input: bytes):
        lines = input.decode('utf-8').split()
        self.nums = [int(num) for num in lines]

    def solve_a(self):
        validator = XmasValidator(self.nums[:25])
        try:
            for num in self.nums[25:]:
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