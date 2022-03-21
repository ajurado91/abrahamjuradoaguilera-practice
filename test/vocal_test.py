import unittest
from src.vocal import Vocal


class VocalTest(unittest.TestCase):
    def test_is_vocal(self):
        vocal = Vocal()
        result = vocal.is_vocal("a")
        self.assertTrue(result)

    def test_is_consonant(self):
        vocal = Vocal()
        result = vocal.is_consonant("g")
        self.assertTrue(result)

    def test_is_number(self):
        vocal = Vocal()
        result = vocal.is_number(5)
        self.assertTrue(result)

    def test_is_empty(self):
        vocal = Vocal()
        result = vocal.is_empty("")
        self.assertTrue(result)


