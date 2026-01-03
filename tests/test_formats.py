import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules import formats


class TestFormats(unittest.TestCase):
    def test_commas(self):
        self.assertEqual(formats.commas(1234567), "1,234,567")

    def test_money(self):
        self.assertEqual(formats.money(12.3), "$12.30")
        self.assertEqual(formats.money(-12.3), "$-12.30")


if __name__ == "__main__":
    unittest.main()
