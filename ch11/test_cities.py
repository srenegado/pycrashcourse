# Ex 11-1

import unittest
from city_functions import city_country

class CityCountryTest(unittest.TestCase):
    """Test cases for city_country()."""

    def test_city_country(self):
        """Do pairs like 'santiago' and 'pair' work?"""
        example_string = city_country('santiago', 'chile') 
        self.assertEqual(example_string, 'Santiago, Chile - population: N/A')

    def test_city_country_population(self):
        """Do triplets like 'santiago', 'chile', '5000000' work?"""
        example_string = city_country('santiago', 'chile', '5000000')
        self.assertEqual(example_string, 'Santiago, Chile - population: 5000000')

if __name__ == '__main__':
    unittest.main()