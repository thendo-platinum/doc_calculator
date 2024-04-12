"""
This module contains the Divide class which performs division operation between two values.
"""

from typing_extensions import Self
from calculator.operator import Operator


class Divide(Operator):
    def run(self) -> Self:
        """
        Performs division operation between two values.

        Returns:
            Self: The instance of the Divide class.

        Raises:
            ValueError: If the second value is zero.
        """
        try:
            self.result = self.v1 / self.v2
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero.")
        return self
