import unittest
from src.reverse import Reverse

class ReverseTest(unittest.TestCase):
    def test_reverse(self):
        reverse = Reverse()
        result = reverse.to_invert("hola")
        self.assertEquals(result, "aloh")

    def test_reverse_empty(self):
        reverse = Reverse()
        result = reverse.is_empty("")
        self.assertTrue(result, "Empty string")

    def test_reverse_only_char(self):
        reverse = Reverse()
        result = reverse.is_only_char("v")
        self.assertTrue(result, "It is a char")