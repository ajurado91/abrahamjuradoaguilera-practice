import unittest
from src.sort_average import Sort

class SortTest(unittest.TestCase):
    def test_sort_max(self):
        sort = Sort()
        result = sort.max_value([1, 2, 3])
        self.assertEquals(result, 3)

    def test_sort_min(self):
        sort = Sort()
        result = sort.min_value([1, 2, 3])
        self.assertEquals(result, 1)

    def test_sort_average(self):
        sort = Sort()
        result = sort.average_value([5, 1, 3])
        self.assertEquals(result, 3)

    def test_sort_equals(self):
        sort = Sort()
        result = sort.order([1, 1, 1])
        self.assertTrue(result, "All equals")

    def test_sort_nan(self):
        sort = Sort()
        result = sort.nan_value([1, "a", 3])
        self.assertTrue(result, "Invalid number")

    def test_sort_empty(self):
        sort = Sort()
        result = sort.is_empty([])
        self.assertTrue(result, "Empty list")