import os
import sys
import unittest
from collections import OrderedDict

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.Acceleration import Acceleration
from modules.Accounting import Accounting
from modules.allowances import allowances
from modules.Area import Area
from modules.Astronomic_units import Astronomic_units
from modules.Astronomic_Units import Astronomic_Units
from modules.Budget import Budget
from modules.Computer_Conversion import Computer_Conversion
from modules.Culinary import Culinary
from modules.Energy_or_Work import Energy_or_Work
from modules.Fuel_Economy import Fuel_Economy
from modules.GED_Practice import GED_Practice
from modules.Imperial_to_Imperial import Imperial_to_Imperial
from modules.Imperial_to_Metric import Imperial_to_Metric
from modules.Light import Light
from modules.Maritime_Measurements import Maritime_Measurements
from modules.Mass import Mass
from modules.Metric_to_Imperial import Metric_to_Imperial
from modules.OhmsLaw import OhmsLaw
from modules.Physical_Fitness import Physical_Fitness
from modules.PlaneAngle import PlaneAngle
from modules.Power import Power
from modules.Pressure import Pressure
from modules.Resistive_Capacitive_Parallel import Resistive_Capacitive_Parallel
from modules.Resistive_Capacitive_Series import Resistive_Capacitive_Series
from modules.Resistive_Inductive_Capacitive_Parallel import (
    Resistive_Inductive_Capacitive_Parallel,
)
from modules.Resistive_Inductive_Capacitive_Series import (
    Resistive_Inductive_Capacitive_Series,
)
from modules.Resistive_Inductive_Parallel import Resistive_Inductive_Parallel
from modules.Resistive_Inductive_Series import Resistive_Inductive_Series
from modules.Torque import Torque
from modules.Velocity import Velocity


MODULES = [
    ("Acceleration", Acceleration),
    ("Accounting", Accounting),
    ("Area", Area),
    ("Astronomic_units", Astronomic_units),
    ("Astronomic_Units", Astronomic_Units),
    ("Budget", Budget),
    ("Computer_Conversion", Computer_Conversion),
    ("Culinary", Culinary),
    ("Energy_or_Work", Energy_or_Work),
    ("Fuel_Economy", Fuel_Economy),
    ("GED_Practice", GED_Practice),
    ("Imperial_to_Imperial", Imperial_to_Imperial),
    ("Imperial_to_Metric", Imperial_to_Metric),
    ("Light", Light),
    ("Maritime_Measurements", Maritime_Measurements),
    ("Mass", Mass),
    ("Metric_to_Imperial", Metric_to_Imperial),
    ("OhmsLaw", OhmsLaw),
    ("Physical_Fitness", Physical_Fitness),
    ("PlaneAngle", PlaneAngle),
    ("Power", Power),
    ("Pressure", Pressure),
    ("Resistive_Capacitive_Parallel", Resistive_Capacitive_Parallel),
    ("Resistive_Capacitive_Series", Resistive_Capacitive_Series),
    ("Resistive_Inductive_Capacitive_Parallel", Resistive_Inductive_Capacitive_Parallel),
    ("Resistive_Inductive_Capacitive_Series", Resistive_Inductive_Capacitive_Series),
    ("Resistive_Inductive_Parallel", Resistive_Inductive_Parallel),
    ("Resistive_Inductive_Series", Resistive_Inductive_Series),
    ("Torque", Torque),
    ("Velocity", Velocity),
]


class TestModuleSmoke(unittest.TestCase):
    def assert_function_list(self, mapping):
        self.assertTrue(mapping)
        for key, value in mapping.items():
            self.assertIsInstance(key, str)
            if isinstance(value, OrderedDict):
                self.assert_function_list(value)
            else:
                self.assertTrue(callable(value))

    def test_module_metadata(self):
        for name, cls in MODULES:
            with self.subTest(module=name):
                instance = cls(name)
                self.assert_function_list(instance.function_list)


class TestAllowances(unittest.TestCase):
    def test_allowances_lists(self):
        allow = allowances()
        self.assertIn("q", allow.quit_allowances)
        self.assertIn("b", allow.back_allowances)
        self.assertIn("h", allow.help_allowances)


class TestNewModules(unittest.TestCase):
    def test_computer_conversion_bits_to_bytes(self):
        calc = Computer_Conversion("Computer_Conversion")
        calc.prompt = lambda args: [16.0]
        result, unit = calc.bits_to_bytes()
        self.assertEqual(result, 2.0)
        self.assertEqual(unit, "Bytes")

    def test_resistive_inductive_capacitive_parallel_impedance(self):
        calc = Resistive_Inductive_Capacitive_Parallel(
            "Resistive_Inductive_Capacitive_Parallel"
        )
        calc.prompt = lambda args: [2.0, 2.0, 2.0]
        result, unit = calc.form_1()
        self.assertEqual(result, "2.0")
        self.assertEqual(unit, "Impedance")

    def test_resistive_inductive_capacitive_series_total_volts(self):
        calc = Resistive_Inductive_Capacitive_Series(
            "Resistive_Inductive_Capacitive_Series"
        )
        calc.prompt = lambda args: [3.0, 4.0, 4.0]
        result, unit = calc.form_1()
        self.assertEqual(result, "3.0")
        self.assertEqual(unit, "Total Volts")


if __name__ == "__main__":
    unittest.main()
