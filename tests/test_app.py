from pathlib import Path
from chalice.test import Client
from app import app
import pytest


sample_test_data = [
    (1, 'a', 514579),
    (1, 'b', 241861950),
    (2, 'a', 2),
    (2, 'b', 1),
    (3, 'a', 7),
    (3, 'b', 336),
    (4, 'a', 2),
    (4, 'b', 2),
    (5, 'a', 357),
    # Day 5 does not provide sample answer for the 2nd challenge
    # (5, 'b', None)
    (6, 'a', 11),
    (6, 'b', 6),
    (7, 'a', 4),
    (7, 'b', 32),
    (8, 'a', 5),
    (8, 'b', 8),
    # The sample for Day 9 has different rules than the actual challenge
    # (9, 'a', 127),
    # (9, 'b', 62),
    (10, 'a', 220),
    (10, 'b', 19208),
]


personal_test_data = [
    (1, 'a', 121396),
    (1, 'b', 73616634),
    (2, 'a', 643),
    (2, 'b', 388),
    (3, 'a', 162),
    (3, 'b', 3064612320),
    (4, 'a', 200),
    (4, 'b', 116),
    (5, 'a', 994),
    (5, 'b', 741),
    (6, 'a', 6878),
    (6, 'b', 3464),
    (7, 'a', 185),
    (7, 'b', 89084),
    (8, 'a', 1941),
    (8, 'b', 2096),
    (9, 'a', 88311122),
    (9, 'b', 13549369),
    (10, 'a', 1904),
    (10, 'b', 10578455953408),
]


def load_test_data_relative(file_name: str) -> bytes:
    directory = Path(__file__).resolve().parent
    file_path = directory / file_name
    return file_path.read_bytes()


@pytest.mark.parametrize("day,challenge,expected", sample_test_data)
def test_challenge_sample(day, challenge, expected):
    input = load_test_data_relative(f'sample_input/day{day}.txt')
    with Client(app) as client:
        response = client.http.post(f'/day/{day}/challenge/{challenge}', body=input)
    answer = response.json_body['answer']
    assert answer == expected


@pytest.mark.parametrize("day,challenge,expected", personal_test_data)
def test_challenge_actual(day, challenge, expected):
    input = load_test_data_relative(f'actual_inputs/day{day}.txt')
    with Client(app) as client:
        response = client.http.post(f'/day/{day}/challenge/{challenge}', body=input)
    answer = response.json_body['answer']
    assert answer == expected
