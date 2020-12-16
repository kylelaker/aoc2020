from chalice import Chalice, NotFoundError
from aoc.solvers import get_solvers

app = Chalice(app_name='aoc2020')

def get_solver(day):
    solvers = get_solvers()
    try:
        return solvers[int(day)]
    except KeyError:
        return NotImplemented


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/day/{day}/challenge/{challenge}', methods=['POST'])
def day1a(day, challenge):
    input = app.current_request.raw_body
    if (solver_class := get_solver(day)) == NotImplemented:
        raise NotFoundError(f"Day {day} is not implemented yet.")
    solver = solver_class(input)

    if (answer := solver.solve(challenge)) == NotImplemented:
        raise NotFoundError("Challenge {challenge} is not implemented for Day {day}")
    
    return {'answer': answer}
