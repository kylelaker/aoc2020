from collections import defaultdict
from itertools import combinations, permutations
from typing import Counter, List
from chalicelib.challenge import ChallengeSolver


def count_differences(l):
    pairs = [(l[i], l[i + 1]) for i in range(len(l) - 1)]
    diffs = {}
    for a, b in pairs:
        diffs.setdefault(b - a, 0)
        diffs[b - a] += 1
    return diffs


class AdapterArray(ChallengeSolver):
    day = 10
    adapter_joltages: List[int]
    
    def __init__(self, input: bytes):
        lines = input.decode('utf-8').splitlines()
        nums = sorted(list(map(int, lines)))
        self.adapter_joltages = [0] + nums + [max(nums) + 3]
    
    def solve_a(self):
        diffs = count_differences(self.adapter_joltages)
        return diffs[1] * diffs[3]

    def solve_b(self):
        paths_to = defaultdict(int)
        paths_to[0] = 1
        for joltage in self.adapter_joltages:
            for allowed_diff in (1, 2, 3):
                next_joltage = joltage + allowed_diff
                if next_joltage in self.adapter_joltages:
                    paths_to[next_joltage] += paths_to[joltage]
        return paths_to[max(self.adapter_joltages)]
