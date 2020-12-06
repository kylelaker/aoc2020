import abc

class Challenge(abc.ABC):
    @abc.abstractproperty
    def day() -> int:
        """
        Which day the challenge is for
        """
        pass

    def solve_a():
        """
        Solve the first challenge of the day.
        """

    def solve_b():
        """
        Solve the second challenge of the day.
        """
