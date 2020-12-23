from string import hexdigits
from typing import List
from chalicelib.challenge import ChallengeSolver

REQUIRED_ATTRS = (
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
)


class Passport:
    def __init__(self):
        for attr in REQUIRED_ATTRS:
            setattr(self, attr, None)
    

    @property
    def valid_simple(self):
        for attr in REQUIRED_ATTRS:
            if not getattr(self, attr):
                return False
        return True

    @property
    def valid_secure(self):
        # yikes
        if not self.valid_simple:
            return False
        try:
            if not (1920 <= int(self.byr) <= 2002):
                return False
            if not (2010 <= int(self.iyr) <= 2020):
                return False
            if not (2020 <= int(self.eyr) <= 2030):
                return False
            if self.hgt[-2:] == 'cm':
                if not (150 <= int(self.hgt[:-2]) <= 193):
                    return False
            elif self.hgt[-2:] == 'in':
                if not (59 <= int(self.hgt[:-2]) <= 76):
                    return False
            else:
                return False
            if (not self.hcl.startswith('#')) and len(self.hcl) != 7:
                return False
            int(self.hcl[1:], 16)
            if self.ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                return False
            return len(self.pid) == 9 and self.pid.isnumeric()
        except (ValueError, TypeError) as err:
            print(err)
            return False


def process_passports(input_data):
    passports = [Passport()]
    for line in input_data:
        if line == '':
            passports.append(Passport())
            continue
        passport = passports[-1]
        line_fields = line.split()
        for line_field in line_fields:
            field, value = line_field.split(':')
            setattr(passport, field, value)
    return passports


class PassportProcessing(ChallengeSolver):
    day = 4

    passports: List[Passport]

    def __init__(self, input: bytes):
        data = input.decode('utf-8').splitlines()
        self.passports = process_passports(data)

    def solve_a(self):
        return sum(passport.valid_simple for passport in self.passports)

    def solve_b(self):
        return sum(passport.valid_secure for passport in self.passports)