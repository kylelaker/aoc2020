from aoc.challenge import ChallengeSolver
from typing import List


class StoredPassword:
    def __init__(self, num_1, num_2, char, password):
        self.num_1 = num_1
        self.num_2 = num_2
        self.char = char
        self.password = password

    @classmethod
    def from_line(cls, line):
        sections = line.split()
        num_1, num_2 = map(int, sections[0].split('-'))
        char = sections[1].strip(':')
        password = sections[2]
        return cls(num_1, num_2, char, password)

    def is_valid(self, validator):
        return validator(self)


class PasswordPhilosophy(ChallengeSolver):

    day = 2
    passwords: List[StoredPassword]

    def __init__(self, input):
        lines = input.decode('utf-8').splitlines()
        self.passwords = [StoredPassword.from_line(line) for line in lines]

    def solve_a(self):
        def validate_sled(entry):
            return entry.num_1 <= entry.password.count(entry.char) <= entry.num_2

        return sum(password.is_valid(validate_sled) for password in self.passwords)

    def solve_b(self):
        def validate_toboggan(entry):
            return (
                entry.password[entry.num_1 - 1] == entry.char) != (entry.password[entry.num_2 - 1] == entry.char
            )

        return sum(password.is_valid(validate_toboggan) for password in self.passwords)
