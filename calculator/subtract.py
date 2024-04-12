"""

This module provides the `Subtract` class, which represents a subtraction operation. It inherits from the `Operator` class.

Example usage:
    subtractor = Subtract()
    subtractor.v1 = 10
    subtractor.v2 = 5
    result = subtractor.run().result
    print(result)  # Output: 5
"""

from calculator.operator import Operator


class Subtract(Operator):
    """
    Represents a subtraction operation.

    Attributes:
        v1 (int): The first value to be subtracted.
        v2 (int): The second value to be subtracted.
        result (int): The result of the subtraction operation.
    """

    def run(self) -> "Subtract":
        """
        Executes the subtraction operation and returns the result.

        Returns:
            Subtract: The current instance of the `Subtract` class.
        """
        self.result = self.v1 - self.v2
        return self
