from calculator.operator import Operator


class Add(Operator):
    """
    Represents an addition operation.

    Attributes:
        v1 (int|float): The first value to be added.
        v2 (int|float): The second value to be added.
        result (int|float): The result of the addition operation.
    """

    def run(self) -> "Add":
        """
        Executes the addition operation and returns the result.

        Returns:
            Add: The current instance of the `Add` class.
        """
        self.result = self.v1 + self.v2
        return self
