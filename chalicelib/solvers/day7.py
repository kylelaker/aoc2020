import re

from dataclasses import dataclass
from collections import namedtuple
from typing import List

from chalicelib.challenge import ChallengeSolver

BAG_TYPES = {}
LINE_REGEX = re.compile(r"(?P<color>.*) bags contain (?P<rules>.*).")
RULE_REGEX = re.compile(r"(?P<count>\d+) (?P<color>.*) bags?")
BagRule = namedtuple('BagRule', ('count', 'color'))


class Bag:

    def __init__(self, color, bag_rules):
        self.color = color
        self.directly_contains = bag_rules
        BAG_TYPES[color] = self


    def can_eventually_contain(self, color):
        for rule in self.directly_contains:
            if color == rule.color:
                return True
            if BAG_TYPES[rule.color].can_eventually_contain(color):
                return True
        return False

    def bags_required_inside(self):
        count = 0
        for rule in self.directly_contains:
            count += rule.count + rule.count * BAG_TYPES[rule.color].bags_required_inside()
        return count
        

    @classmethod
    def parse(cls, line):
        line_match = LINE_REGEX.match(line)
        color = line_match.group('color')
        rule_texts = line_match.group('rules')
        rules = []
        for rule_text in rule_texts.split(','):
            rule_text = rule_text.strip()
            if rule_text == 'no other bags':
                continue
            rule_match = RULE_REGEX.match(rule_text)
            rule_count = int(rule_match.group('count'))
            rule_color = rule_match.group('color')
            rules.append(BagRule(rule_count, rule_color))
        
        return cls(color, rules) 


class HandyHaversacks(ChallengeSolver):
    day = 7
    bags = List[Bag]

    def __init__(self, input: bytes):
        lines = input.decode('utf-8').splitlines()
        self.bags = [Bag.parse(line) for line in lines]


    def solve_a(self):
        return sum(bag.can_eventually_contain('shiny gold') for bag in self.bags)
    
    def solve_b(self):
        return BAG_TYPES['shiny gold'].bags_required_inside()
