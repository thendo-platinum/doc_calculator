"""This module contains a simple calculator class that performs basic arithmetic operations."""

from calculator.add import Add
from calculator.divide import Divide
from calculator.multiply import Multiply
from calculator.subtract import Subtract

# from teams_logger.logger import teams_logger


class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.

    Attributes:
        None

    Methods:
        add: Adds two numbers and returns the result.
        subtract: Subtracts two numbers and returns the result.
        multiply: Multiplies two numbers and returns the result.
        divide: Divides two numbers and returns the result.
        power: Raises a number to the power of another number and returns the result.
    """

    def add(self, a, b):
        """
        Adds two numbers and returns the result.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of the two numbers.
        """
        return Add(a, b).run().result

    def subtract(self, a, b):
        """
        Subtracts two numbers and returns the result.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The difference between the two numbers.
        """
        return Subtract(a, b).run().result

    def multiply(self, a, b):
        """
        Multiplies two numbers and returns the result.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The product of the two numbers.
        """
        return Multiply(a, b).run().result

    def divide(self, a, b):
        """
        Divides two numbers and returns the result.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            float: The quotient of the two numbers.
        """
        return Divide(a, b).run().result

    def power(self, a, b):
        """
        Raises a number to the power of another number and returns the result.

        Args:
            a (int): The base number.
            b (int): The exponent.

        Returns:
            int: The result of raising the base number to the power of the exponent.
        """
        res = 1
        for i in range(b):
            res = Multiply(res, a).run().result
        return res
