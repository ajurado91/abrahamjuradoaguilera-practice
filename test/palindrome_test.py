import unittest
from src.palindrome import Palindrome

class PalindromeTest(unittest.TestCase):

    def test_palindrome_true(self):
        palindrome = Palindrome()
        result = palindrome.check("oruro")
        self.assertTrue(result, "Is palindrome")

    def test_palindrome_false(self):
        palindrome = Palindrome()
        result = palindrome.check("Juan")
        self.assertFalse(result, "Is not palindrome")

    def test_palindrome_only_char(self):
        palindrome = Palindrome()
        result = palindrome.is_only_char("a ")
        self.assertTrue(result, "It is a char")

    def test_palindrome_empty(self):
        palindrome = Palindrome()
        result = palindrome.is_empty(" ")
        self.assertTrue(result, "Empty string")