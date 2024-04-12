from abc import ABCMeta, abstractmethod
from typing_extensions import Self


class Operator(metaclass=ABCMeta):
    """
    Abstract base class for operators.

    This class serves as a base class for all operators. It defines the common behavior and attributes that operators should have.

    Attributes:
        v1: The first value for the operator.
        v2: The second value for the operator.
    """

    def __init__(self, v1: int | float, v2: int | float) -> None:
        """
        Initializes an instance of the Operator class.

        Parameters:
        v1 (int|float): The first value.
        v2 (int|float): The second value.
        """
        self.v1 = v1
        self.v2 = v2
        self.result: int | float = 0

    @abstractmethod
    def run(self) -> Self:
        """
        Executes the logic of the operator.

        Returns:
            Self: The instance of the operator.
        """
        pass

    @property
    def res(self) -> int | float:
        """
        Returns the result of the `run` method.

        Returns:
            int | float: The result of the `run` method.
        """
        return self.run().result
