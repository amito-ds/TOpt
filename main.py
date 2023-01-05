# Press the green button in the gutter to run the script.
from parameters_utiils import ValueSet, Parameter, ParameterSet

if __name__ == '__main__':
    # Create a continuous parameter
    p1 = Parameter("p1", "continuous", 0, 1)

    # Create a ParameterSet with a list of parameters
    ps = ParameterSet("test", [p1])

    # Update the min_value attribute of the parameter
    ps.update("p1", "min_value", 0.5)

    # Print the updated min_value attribute
    print(p1.min_value)  # 0.5


