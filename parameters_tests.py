import random
import unittest

import pandas as pd

from dt_utils import train_decision_tree
from parameters_utiils import ParameterSet, Parameter, ValueSet


class TestParameter(unittest.TestCase):
    def test_sample_continuous(self):
        # Test that the sample method returns a continuous value from the
        # range specified by the minimum and maximum values
        p = Parameter("p", "continuous", 0, 1)
        sampled_value = p.sample()
        self.assertIsInstance(sampled_value, float)
        self.assertGreaterEqual(sampled_value, 0)
        self.assertLessEqual(sampled_value, 1)

    def test_sample_discrete(self):
        # Test that the sample method returns a discrete value from the
        # range specified by the minimum and maximum values
        p = Parameter("p", "discrete", 0, 10)
        sampled_value = p.sample()
        self.assertIsInstance(sampled_value, int)
        self.assertGreaterEqual(sampled_value, 0)
        self.assertLessEqual(sampled_value, 10)

    def test_sample_invalid_type(self):
        # Test that the sample method raises a ValueError if the parameter type is invalid
        p = Parameter("p", "invalid", 0, 1)
        with self.assertRaises(ValueError):
            sampled_value = p.sample()

    def test_init(self):
        # Test that a ValueSet is correctly initialized with a name and a list of parameter values
        values = ValueSet("test", [1, 2, 3])
        self.assertEqual(values.name, "test")
        self.assertEqual(values.parameter_values, [1, 2, 3])

    def test_sample(self):
        # Test that the sample method returns a value from the set of parameter values
        values = ValueSet("test", [1, 2, 3])
        sampled_value = values.sample()
        self.assertIn(sampled_value, [1, 2, 3])

    def test_sample2(self):
        # Test that the sample method returns a dictionary of parameter names and sampled values
        p1 = Parameter("p1", "continuous", 0, 1)
        p2 = ValueSet("p2", [1, 2, 3])
        ps = ParameterSet("test", [p1, p2])
        sampled_values = ps.sample()
        self.assertIsInstance(sampled_values, dict)
        self.assertEqual(set(sampled_values.keys()), {"p1", "p2"})
        self.assertIsInstance(sampled_values["p1"], float)
        self.assertIsInstance(sampled_values["p2"], int)
        self.assertGreaterEqual(sampled_values["p1"], 0)
        self.assertLessEqual(sampled_values["p1"], 1)
        self.assertIn(sampled_values["p2"], [1, 2, 3])

    def test_update(self):
        # Test that the update method updates the parameter_values attribute with a new list of values
        values = ValueSet("test", parameter_values=[1, 2, 3])
        values.update([4, 5, 6])
        self.assertEqual(values.parameter_values, [4, 5, 6])

    def test_update2(self):
        # Test that the update method updates the specified attribute of a parameter with a new value
        p1 = Parameter("p1", "continuous", 0, 1)
        ps = ParameterSet("test", [p1])
        ps.update("p1", "min_value", 0.5)
        self.assertEqual(p1.min_value, 0.5)

    def test_update3(self):
        # Test update method for continuous parameter
        p1 = Parameter("p1", "continuous", 0, 1)
        ps = ParameterSet("test", [p1])
        ps.update("p1", "min_value", 0.5)
        self.assertEqual(p1.min_value, 0.5)

        # Test update method for discrete parameter
        p2 = Parameter("p2", "discrete", 0, 10)
        ps = ParameterSet("test", [p2])
        ps.update("p2", "max_value", 5)
        self.assertEqual(p2.max_value, 5)

        # Test update method for ValueSet
        values = ValueSet("test", parameter_values=[1, 2, 3])
        ps = ParameterSet("test", [values])
        ps.update("test", "parameter_values", [4, 5, 6])
        self.assertEqual(values.parameter_values, [4, 5, 6])

    def test_train_decision_tree(self):
        # Create a parameter set with two continuous parameters
        param_set = ParameterSet(
            name="test",
            parameters=[
                Parameter("learning_rate", "continuous", 0, 1),
                Parameter("max_depth", "continuous", 1, 10)
            ]
        )

        # Create a results dataframe with random values for the two parameters and a random metric value
        # Make the metric value correlated with the learning_rate parameter
        results = pd.DataFrame(
            data={
                "learning_rate": [random.uniform(0, 1) for _ in range(100)],
                "max_depth": [random.uniform(1, 10) for _ in range(100)],
                "metric": [random.uniform(0, 1) for _ in range(100)]
            }
        )
        results['metric'] = results['learning_rate'] + random.uniform(-0.1, 0.1)

        # Train the decision tree
        rule = train_decision_tree(results, param_set)

        # Check if the first split variable is "learning_rate"
        self.assertEqual(rule.split(" ")[0], "learning_rate")


if __name__ == '__main__':
    unittest.main()
