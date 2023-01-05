# Press the green button in the gutter to run the script.
from dt_utils import train_decision_tree
from parameters_utiils import ValueSet, Parameter, ParameterSet
import pandas as pd

from update_utils import update_param

if __name__ == '__main__':
    # Create a parameter set with two continuous parameters
    param_set = ParameterSet("param_set", [
        Parameter("p1", "continuous", 0, 1),
        Parameter("p2", "continuous", 0, 1)
    ])

    # Train the decision tree and update the parameters multiple times
    prev_rule = None  # Keep track of the previous rule
    for i in range(5):
        # Create a dataframe with random values for the parameters and the metric
        results = pd.DataFrame(columns=["p1", "p2", "metric"])
        results["p1"] = [param_set.parameters[0].sample() for _ in range(1000)]
        results["p2"] = [param_set.parameters[1].sample() for _ in range(1000)]
        results["metric"] = results["p1"] + results["p2"]

        # Train the decision tree and get the rule of the first split
        rule = train_decision_tree(results, param_set)
        for param in param_set.parameters:
            print("rule: ", rule)
            print(f"{param.name}: {param.min_value} - {param.max_value}")

        # Update the parameter based on the rule,
        update_param(rule, param_set)

    # Print the final parameter values

