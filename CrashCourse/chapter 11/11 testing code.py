# using the unittest module to test functions and classes

# a unit test verifies one specific aspect of a function behavior is correct
# a test case is a collection of unit tests
# a test case with full coverage includes full range of unit tests covering
# all the [pssob;e ways to use the function

# a passing test
# import the unittest module
import unittest

# import the function to test
from name_function import get_formatted_name

#  instantiate a unit test class for the function that inherits from unittest
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    # test unit method names start with test_
    # any method whose name starts with test_ will automatically run
    # when the associated function is run

    # create a unit test , a method that verifys one aspect of the function
    def test_first_last_name(self):
        """Do names like 'Bill Blast' work?"""
        # run the function in question
        formatted_name = get_formatted_name("Bill", "Blast")
        # test the result against the expected result
        self.assertEqual(formatted_name, "Bill Blast")


#
if __name__ == "__main__":
    unittest.main()
