import unittest
from src.countries import Countries


class CountriesTest(unittest.TestCase):
    def test_country_sort(self):
        country = Countries()
        countries = ["Bolivia", "Peru", "China", "Venezuela", "Estados Unidos"]
        result = country.sort(countries)
        self.assertEqual(result, 'Estados Unidos')

    def test_country_sort_empty_list(self):
        country = Countries()
        countries = []
        result = country.is_empty(countries)
        self.assertTrue(result, "Empty list")

    def test_country_only_one_country(self):
        country = Countries()
        countries = ["Paraguay"]
        result = country.only_one(countries)
        self.assertTrue(result, "Only one country in list")
