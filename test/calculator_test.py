import unittest
from src.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 2)
        self.assertEqual(4, result)
