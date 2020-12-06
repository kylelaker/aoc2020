from chalice import Chalice, NotFoundError
from chalice.app import BadRequestError
from chalicelib.day1 import ReportRepair
from chalicelib.day2 import PasswordPhilosophy

app = Chalice(app_name='aoc2020')


def get_solver(day):
    # TODO: Dynamically determine the correct solver based on the day attribute
    # of the solver class.
    if int(day) == 1:
        return ReportRepair
    if int(day) == 2:
        return PasswordPhilosophy
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
    if challenge == 'a':
        return {'answer': solver.solve_a()}
    if challenge == 'b':
        if (b_sol := solver.solve_b()) == NotImplemented:
            raise NotFoundError(f"Challenge B for Day {day} is not implemented")
        return {'answer': b_sol}
    raise NotFoundError(f"Day {day} Challenge {challenge} is not supported")
