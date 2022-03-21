import unittest
from src.age import Age


class AgeTest(unittest.TestCase):
    def test_validate_age(self):
        age = Age()
        result = age.valid_age(10)
        self.assertTrue(result)

    def test_validate_age_invalid(self):
        age = Age()
        result = age.valid_age(-10)
        self.assertFalse(result)