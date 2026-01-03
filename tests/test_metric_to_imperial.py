import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.Metric_to_Imperial import Metric_to_Imperial


class TestMetricToImperial(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        calc = Metric_to_Imperial("Metric_to_Imperial")
        calc.prompt = lambda args: [0.0]
        result, unit = calc.form_celsius()
        self.assertAlmostEqual(result, 32.0)
        self.assertEqual(unit, "Fahrenheit")

    def test_meters_to_feet(self):
        calc = Metric_to_Imperial("Metric_to_Imperial")
        calc.prompt = lambda args: [1.0]
        result, unit = calc.form_meters()
        self.assertAlmostEqual(result, 3.2808, places=4)
        self.assertEqual(unit, "Feet")


if __name__ == "__main__":
    unittest.main()
