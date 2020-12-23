import abc
import string
from typing import List, Union

NotImplementedType = type(NotImplemented)


class ChallengeSolver(abc.ABC):
    """
    Solve an Advent of Code challenge.

    Solutions should specialize this class, implementing a method called
    solve_{challenge} where {challenge} is 'a' or 'b' for whether it is the
    first or second challenge of the day respectively. Any solution that
    is not implemented must either not have a corresponding solve_ method
    or must return NotImplemented.
    """

    @abc.abstractmethod
    def __init__(self, input: bytes):
        pass

    @abc.abstractproperty
    def day(self) -> int:
        """
        Which day the challenge is for
        """
        pass

    def solve(self, challenge: str) -> Union[int, NotImplementedType]:
        if challenge.isnumeric():
            challenge = string.ascii_lowercase[int(challenge) - 1]

        return getattr(self, f'solve_{challenge}', lambda x: NotImplemented)()

    @classmethod
    def supported_challenges(cls) -> List[str]:
        attrs = cls.__dict__.keys()
        solver_methods = [
            attr
            for attr in attrs
            if attr.startswith('solve_')
        ]
        challenges = [solver[-1] for solver in solver_methods]
        return challenges