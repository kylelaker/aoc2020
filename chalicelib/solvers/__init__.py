import importlib
import inspect

from pathlib import Path

from chalicelib.challenge import ChallengeSolver

_SOLVERS = {}


def _load_solvers():
    def is_subclass(sub, parent):
        return (
            inspect.isclass(sub) and inspect.getmodule(sub) is None
            and issubclass(sub, parent)
        )
    
    directory = Path(__file__).resolve().parent
    print(directory)
    solvers = {}
    for file_path in directory.iterdir():
        if file_path.stem == '__init__' or file_path.suffix != '.py':
            continue
        module_name = file_path.stem
        try:
            spec = importlib.util.spec_from_loader(module_name, None)
            solver_module = importlib.util.module_from_spec(spec)
            exec(file_path.open().read(), solver_module.__dict__)
        except (ImportError, SyntaxError) as import_error:
            print(import_error)
        else:
            module_contents = [
                getattr(solver_module, item_name)
                for item_name in dir(solver_module)
            ]
            for solver_class in module_contents:
                if is_subclass(solver_class, ChallengeSolver):
                    solvers[solver_class.day] = solver_class
    return solvers


def get_solvers():
    global _SOLVERS
    if not _SOLVERS:
        _SOLVERS = _load_solvers()
    return dict(_SOLVERS)


if not _SOLVERS:
    _SOLVERS = _load_solvers()