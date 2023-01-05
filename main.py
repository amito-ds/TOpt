# Press the green button in the gutter to run the script.
from dt_utils import train_decision_tree
from parameters_utiils import ValueSet, Parameter, ParameterSet
import pandas as pd

if __name__ == '__main__':
    # Create a dataframe with metric values and other columns
    results = pd.DataFrame({'param1': [0, 0, 0, 1, 1], 'param2': [0, 1, 0, 1, 0], 'metric': [0, 0, 0, 1, 1]})

    # Create a ParameterSet with a list of parameters
    params = [Parameter("param1", "continuous", 0, 1), Parameter("param2", "continuous", 0, 1)]
    param_set = ParameterSet("test", params)

    # Train a decision tree and print the first split
    rule= train_decision_tree(results, param_set)
    print(f"First split: {rule}")
