import abc
import string

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

    def solve(self, challenge:str):
        if challenge.isnumeric():
            challenge = string.ascii_lowercase[int(challenge) - 1]

        return getattr(self, f'solve_{challenge}', lambda x: NotImplemented)()
