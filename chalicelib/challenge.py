import abc

class Challenge(abc.ABC):
    @abc.abstractproperty
    def day(self) -> int:
        """
        Which day the challenge is for
        """
        pass

    def solve_a(self):
        """
        Solve the first challenge of the day.
        """
        return NotImplemented

    def solve_b(self):
        """
        Solve the second challenge of the day.
        """
        return NotImplemented
