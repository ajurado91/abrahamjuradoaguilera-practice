import unittest
from src.binary import Binary


class BinaryTest(unittest.TestCase):
    def test_decimal_to_binary(self):
        binary = Binary()
        result = binary.convert(2)
        self.assertEqual(result, "10")

    def test_nan_binary(self):
        binary = Binary()
        result = binary.nan_binary("1F")
        self.assertTrue(result, "Not a number")

    def test_empty_binary(self):
        binary = Binary()
        result = binary.is_empty("")
        self.assertTrue(result, "Empty")


