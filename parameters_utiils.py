import random
import typing
from typing import List, Dict, Union


class Parameter:
    def __init__(self, name: str, parameter_type: str, min_value: float, max_value: float) -> None:
        self.name = name
        self.parameter_type = parameter_type
        self.min_value = min_value
        self.max_value = max_value

    def update(self, min_value: float = None, max_value: float = None) -> None:
        """
        Update the minimum or maximum value of the parameter.
        """
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    def sample(self) -> float:
        """
        Sample a value from the range specified by the minimum and maximum values.
        """
        if self.parameter_type == "continuous":
            return random.uniform(self.min_value, self.max_value)
        elif self.parameter_type == "discrete":
            return random.randint(int(self.min_value), int(self.max_value))
        else:
            raise ValueError(f"Invalid parameter type: {self.parameter_type}")


class ValueSet:
    def __init__(self, name: str, parameter_values: typing.List[float]) -> None:
        self.name = name
        self.parameter_values = parameter_values

    def sample(self) -> float:
        """
        Sample a value from the set of values.
        """
        return random.choice(self.parameter_values)

    def update(self, new_values: List[float]) -> None:
        """
        Update the set of values with a new list of values.
        """
        self.parameter_values = new_values


class ParameterSet:
    def __init__(self, name: str, parameters: List[Union[Parameter, ValueSet]]) -> None:
        self.name = name
        self.parameters = parameters

    def sample(self) -> Dict[str, float]:
        """
        Sample a value for each parameter in the set.
        Returns a dictionary of parameter names and sampled values.
        """
        sampled_values = {}
        for parameter in self.parameters:
            sampled_values[parameter.name] = parameter.sample()
        return sampled_values

    def update(self, parameter_name: str, attribute: str, new_value: float) -> None:
        """
        Update the specified attribute of a parameter with a new value.
        """
        for parameter in self.parameters:
            if parameter.name == parameter_name:
                setattr(parameter, attribute, new_value)
                break
