# Press the green button in the gutter to run the script.
from parameters_utiils import ValueSet, Parameter, ParameterSet

if __name__ == '__main__':
    # Example 1: Create a ValueSet object with a set of values
    # Create a ValueSet with a list of parameter values
    # values = ValueSet("test", parameter_values=[1, 2, 3, 4])
    #
    # # Sample a value from the set of values
    # sampled_value = values.sample()
    #
    # # Example 2: Sample a value from the set
    # print(f"Sampled value: {sampled_value}")
    # Create a continuous parameter
    # Create a continuous parameter
    p1 = Parameter("p1", "continuous", 0, 1)

    # Create a discrete parameter
    p2 = Parameter("p2", "discrete", 0, 10)

    # Create a ValueSet
    values = ValueSet("test", parameter_values=[1, 2, 3, 4])

    # Create a ParameterSet with a list of parameters and ValueSets



