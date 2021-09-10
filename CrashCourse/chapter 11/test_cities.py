# import the testing module
import unittest

# import the function to be tested
from city_functions import get_formatted_city_country


# create a class that inherits from unittest
class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    # create a test case for the function
    def test_city_country(self):
        formatted_string = get_formatted_city_country("santiago", "chile")
        self.assertEqual(formatted_string, "Santiago, Chile.")

    # create a test case for the function
    def test_city_country_population(self):
        formatted_string = get_formatted_city_country("santiago", "chile", 5000000)
        self.assertEqual(formatted_string, "Santiago, Chile - population 5000000.")


# run the unittest if this is run directly from this file
if __name__ == "__main__":
    unittest.main()
