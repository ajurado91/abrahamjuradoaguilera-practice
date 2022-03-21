import unittest
from src.max import Max


class MaxTest(unittest.TestCase):
    def test_max_number(self):
        max = Max()
        values = [1, 2, 3]
        result = max.max_value(values)
        self.assertEquals(result, 3)

    def test_max_number_equals(self):
        max = Max()
        result = max.equal_value([5, 5, 5])
        self.assertTrue(result)

    def test_max_number_nan(self):
        max = Max()
        result = max.nan_value(["l", 5, 2])
        self.assertTrue(result)

