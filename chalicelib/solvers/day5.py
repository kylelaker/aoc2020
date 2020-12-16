from dataclasses import dataclass
from typing import List
from chalicelib.challenge import ChallengeSolver


class Seat:
    row: int
    column: int

    def __init__(self, row, column):
        self.row = row
        self.column = column

    @property
    def id(self):
        return self.row * 8 + self.column

    @classmethod
    def parse_str(cls, str):
        row_str = str[:7]
        col_str = str[7:]

        row = int(row_str.replace('F', '0').replace('B', '1'), 2)
        col = int(col_str.replace('L', '0').replace('R', '1'), 2)
        return cls(row, col)


class BinaryBoarding(ChallengeSolver):
    day = 5
    seats: List[Seat]

    def __init__(self, input):
        lines = input.decode('utf-8').split()
        self.seats = [Seat.parse_str(line) for line in lines]
    
    def solve_a(self):
        return max(seat.id for seat in self.seats)

    def solve_b(self):
        seat_ids = [seat.id for seat in self.seats]
        max_id = 127 * 8 + 7
        for seat_id in range(max_id):
            if seat_id not in seat_ids and seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
                return seat_id
        return -1
