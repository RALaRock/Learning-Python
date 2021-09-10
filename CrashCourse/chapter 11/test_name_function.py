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
    # functions that start with "test_" run automatically
    # name the test function test_name_name_of_function
    def test_first_last_name(self):
        """Do names like 'Bill Blast' work?"""
        # run the function in question
        # run the function we want to test passing appropriate test
        # values
        formatted_name = get_formatted_name("Bill", "Blast")
        # test the result against the expected result
        self.assertEqual(formatted_name, "Bill Blast")

    # add a test for names with middle names
    def test_first_last_middle_name(self):
        """Do names like Bill Blast Jones work?"""
        formatted_name = get_formatted_name("bill", "blast", "middle")
        self.assertEquals(formatted_name, "Bill Middle Blast")


# when a file is imported, Python runs the code as it's imported
# many testing frameworks import code to test
# this if statement checks to see if this file is the main program,
# in other words if this program was run directly from this file,
# not imported into another program to be run.
# if the special variable __name__ is set to __main__ this this
# program has been run directly from this file, not imported into
# another file or framework
# if the program were run from another file, __name__ would not
# be __main__, thus preventing this code from running during an
# import
if __name__ == "__main__":
    unittest.main()
