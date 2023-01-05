import random
from typing import List
import typing


class Parameter:
    def __init__(self, name: str, parameter_type: str, min_value: float, max_value: float) -> None:
        self.name = name
        self.parameter_type = parameter_type
        self.min_value = min_value
        self.max_value = max_value

    def sample(self) -> float:
        """
        Sample a value from the range specified by the minimum and maximum values.
        """
        return random.uniform(self.min_value, self.max_value)


class ValueSet:
    """
    A class representing a set of discrete values.
    """

    def __init__(self, name: str, parameter_values: typing.List[float]) -> None:
        self.name = name
        self.parameter_values = parameter_values

    def sample(self) -> float:
        """
        Sample a value from the set of values.
        """
        return random.choice(self.parameter_values)


class ParameterSet:
    def __init__(self, name: str, parameters: List[Parameter]) -> None:
        self.name = name
        self.parameters = parameters
