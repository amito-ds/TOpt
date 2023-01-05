from parameters_utiils import ParameterSet


def update_param(rule: str, param_set: ParameterSet) -> None:
    # Split the rule string into parts
    parts = rule.split(" ")

    # Extract the parameter name and the threshold value
    param_name = parts[0]
    threshold = float(parts[2])

    # Find the parameter in the parameter set
    param = None
    for p in param_set.parameters:
        if p.name == param_name:
            param = p
            break

    # Check if the parameter was found
    if param is None:
        raise ValueError(f"Parameter {param_name} not found in parameter set {param_set.name}")

    # Update the parameter using the update method
    if parts[1] == "<":
        param.update(max_value=threshold)
    elif parts[1] == ">":
        param.update(min_value=threshold)
    else:
        raise ValueError(f"Invalid operator {parts[1]} in rule {rule}")

    return param_set
