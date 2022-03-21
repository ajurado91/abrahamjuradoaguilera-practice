import unittest
from src.long_string import Long


class LongStringTest(unittest.TestCase):
    def test_long_string(self):
        long = Long()
        result = long.long_string("")
        self.assertEqual(result, 0)

    def test_long_space(self):
        long = Long()
        result = long.long_string(" ")
        self.assertTrue(result, "Empty string")