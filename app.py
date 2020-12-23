from chalicelib.challenge import ChallengeSolver
from typing import Dict, List, Union
from chalice import Chalice, NotFoundError
from chalicelib.solvers import get_solvers

app = Chalice(app_name='aoc2020')


Day = Union[str, int]
Challenge = Union[str, int]
NotImplementedType = type(NotImplemented)


def get_solver(day: Day) -> Union[ChallengeSolver, NotImplementedType]:
    solvers = get_solvers()
    try:
        return solvers[int(day)]
    except KeyError:
        return NotImplemented


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/days', methods=['GET'])
def supported_days() -> Dict[int, Dict[str, List[str]]]:
    """
    Get a list of all days for which any solution has been written.
    """

    days = {
        int(day): {'challenges': solver.supported_challenges()}
        for day, solver in get_solvers().items()
    }
    return days


@app.route('/day/{day}/challenges', methods=['GET'])
def get_day(day: Day) -> Dict[str, List[str]]:
    """
    Get all the supported challenges for a particular day.
    """

    if (solver_class := get_solver(day)) == NotImplemented:
        raise NotFoundError(f"Day {day} is not implemented yet.")

    return {'challenges': solver_class.supported_challenges()}


@app.route('/day/{day}/challenges', methods=['POST'])
def solve_day_all_challenges(day: Day) -> Dict[str, Dict[str, int]]:
    """
    Solve all the challenges for a given day.
    """

    input = app.current_request.raw_body
    if (solver_class := get_solver(day)) == NotImplemented:
        raise NotFoundError(f"Day {day} is not implemented yet.")
    solver = solver_class(input)

    answers = {}
    for challenge in solver_class.supported_challenges():
        solution = solver.solve(challenge)
        if solution == NotImplemented:
            continue
        answers[challenge] = solution

    return answers


@app.route('/day/{day}/challenge/{challenge}', methods=['POST'])
def solve_day_one_challenges(day: Day, challenge: Challenge) -> Dict[str, int]:
    """
    Solve a given challenge for a given day.
    """

    input = app.current_request.raw_body

    if (solver_class := get_solver(day)) == NotImplemented:
        raise NotFoundError(f"Day {day} is not implemented yet.")
    solver = solver_class(input)

    if (answer := solver.solve(challenge)) == NotImplemented:
        raise NotFoundError("Challenge {challenge} is not implemented for Day {day}")
    
    return {'answer': answer}
