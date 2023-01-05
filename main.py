# Press the green button in the gutter to run the script.
from parameters_utiils import ValueSet

if __name__ == '__main__':
    # Example 1: Create a ValueSet object with a set of values
    values = ValueSet("test", parameter_values=[1, 2, 3, 4])

    # Example 2: Sample a value from the set
    sampled_value = values.sample()
    print(f"Sampled value: {sampled_value}")

