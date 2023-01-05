import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from parameters_utiils import ParameterSet


def train_decision_tree(results: pd.DataFrame, param_set: ParameterSet) -> str:
    # Separate the label column and feature columns
    X = results.drop('metric', axis=1)
    y = results['metric']

    # Train a decision tree regressor with at least 25% of the data in each leaf
    regressor = DecisionTreeRegressor(min_samples_leaf=len(results) // 20)
    regressor.fit(X, y)

    # Check if the tree has only one node
    if regressor.tree_.children_left[0] == -1:
        # Return None value
        return None

    # Get the first split of the decision tree
    first_split = regressor.tree_.feature[0]

    # Get the name of the parameter for the first split
    param_name = param_set.parameters[first_split].name

    # Get the threshold for the first split
    threshold = regressor.tree_.threshold[0]

    # Construct the rule string
    rule = f"{param_name} > {threshold}"

    return rule

#
# def train_decision_tree(results: pd.DataFrame, param_set: ParameterSet) -> Tuple[str, float, str]:
#     # Add a random feature column to the results dataframe
#     results['random_feature'] = [random.uniform(0, 1) for _ in range(len(results))]
#
#     # Separate the label column and feature columns
#     X = results.drop('metric', axis=1)
#     y = results['metric']
#
#     # Train a decision tree regressor
#     regressor = DecisionTreeRegressor(min_samples_leaf=len(results) // 4)
#     regressor.fit(X, y)
#
#     # Get the first split of the decision tree
#     first_split = regressor.tree_.feature[0]
#     print(regressor.tree_.feature)
#
#     # Get the name of the parameter for the first split
#     print("first split",first_split)
#     print(param_set.parameters)
#     print(param_set.parameters[0])
#     param_name = param_set.parameters[first_split].name
#
#     # Get the threshold for the first split
#     threshold = regressor.tree_.threshold[0]
#
#     return param_name, threshold, "middle"
