import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.FormulaBase import FormulaBase


class TestFormulaBase(unittest.TestCase):
    def test_pluralize_irregular(self):
        base = FormulaBase("test")
        self.assertEqual(base.pluralize(2, "Foot"), "Feet")
        self.assertEqual(base.pluralize(1, "Foot"), "Foot")

    def test_prec(self):
        base = FormulaBase("test")
        self.assertEqual(base.prec(3.14159, 2), "3.14")


if __name__ == "__main__":
    unittest.main()
