import string
from typing import List
from chalicelib.challenge import ChallengeSolver


class GroupAnswer:    
    def __init__(self):
        self.members = 0
        self.questions = [0 for _ in range(26)]
    
    def any_yes(self):
        return sum(bool(yeses) for yeses in self.questions)
    
    def all_yes(self):
        return sum(yeses == self.members for yeses in self.questions)


def parse_groups(input_data):
    group_answers = [GroupAnswer()]
    for line in input_data:
        if line == '':
            group_answers.append(GroupAnswer())
            continue
        group_answer = group_answers[-1]
        group_answer.members += 1
        for yes in line:
            group_answer.questions[string.ascii_lowercase.index(yes)] += 1
    
    return group_answers

class CustomCustoms(ChallengeSolver):
    day = 6
    group_answers = List[str]

    def __init__(self, input: bytes):
        data = input.decode('utf-8').splitlines()
        self.group_answers = parse_groups(data)
    
    def solve_a(self):
        return sum(group.any_yes() for group in self.group_answers)
    
    def solve_b(self):
        return sum(group.all_yes() for group in self.group_answers)