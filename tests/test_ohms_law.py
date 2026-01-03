import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.OhmsLaw import OhmsLaw


class TestOhmsLaw(unittest.TestCase):
    def test_volts_using_amps_and_resistance(self):
        calc = OhmsLaw("Ohms Law")
        calc.prompt = lambda args: [2.0, 5.0]
        result, unit = calc.form_voltsar()
        self.assertEqual(result, 10.0)
        self.assertEqual(unit, "Volts")


if __name__ == "__main__":
    unittest.main()
