"""
This module contains the `Multiply` class which represents a multiplication operation.
"""

from calculator.operator import Operator


class Multiply(Operator):
    """
    Represents a multiplication operation.

    Attributes:
        v1 (int): The first value to be multiplied.
        v2 (int): The second value to be multiplied.
        result (int): The result of the multiplication operation.
    """

    def run(self) -> "Multiply":
        """
        Executes the multiplication operation and returns the result.

        Returns:
            Multiply: The current instance of the `Multiply` class.
        """
        self.result = self.v1 * self.v2
        return self
