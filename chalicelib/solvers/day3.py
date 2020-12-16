import math
from collections import namedtuple
from dataclasses import dataclass
from typing import Iterable

from chalicelib.challenge import ChallengeSolver

Slope = namedtuple('Slope', ('right', 'down'))

@dataclass
class Pos:
    x: int
    y: int


def trees_on_slope(rows: Iterable[str], slope: Slope) -> int:
    line_len = len(rows[0])
    pos = Pos(0, 0)
    trees = 0
    while pos.y < len(rows):
        if rows[pos.y][pos.x] == '#':
            trees += 1
        pos.x = (pos.x + slope.right) % line_len
        pos.y += slope.down

    return trees


class TobogganTrajectory(ChallengeSolver):
    day = 3

    def __init__(self, input):
        self.tree_rows = input.decode('utf-8').split()
    
    def solve_a(self):
        return trees_on_slope(self.tree_rows, Slope(3, 1))

    def solve_b(self):
        slopes = (
            Slope(1, 1),
            Slope(3, 1),
            Slope(5, 1),
            Slope(7, 1),
            Slope(1, 2),
        )
        trees = [
            trees_on_slope(self.tree_rows, slope)
            for slope in slopes
        ]
        return math.prod(trees)