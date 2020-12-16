from chalicelib.challenge import ChallengeSolver
from typing import List


class ReportRepair(ChallengeSolver):

    day = 1
    entries: List[int]

    def __init__(self, input):
        lines = input.decode('utf-8').split()
        self.entries = [int(line) for line in lines]

    def solve_a(self):
        desired_sum = 2020
        for entry in self.entries:
            if (diff := desired_sum - entry) in self.entries:
                return diff * entry
        return -1

    def solve_b(self):
        desired_sum = 2020
        for entry_a in self.entries:
            diff = desired_sum - entry_a
            for entry_b in self.entries:
                third_num = diff - entry_b
                if third_num in self.entries:
                    return entry_a * entry_b * third_num
        return -1