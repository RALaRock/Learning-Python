# using the unittest module to test functions and classes

# a unit test verifies one specific aspect of a function behavior is correct
# a test case is a collection of unit tests
# a test case with full coverage includes full range of unit tests covering
# all the possible ways to use the function

# testing functions

# to write a test case:
# import the unittest module
# import the function you want to test
# create a class that inherits from unittest.TestCase
# write a series of methods to test the functions behavior

# see example at:
#       name_function.py          - module contains get_formatted_name()
#       test_name_function.py  - module for testing get_formatted_name()
#       names.py                       - program that uses get_formatted_name()

# testing classes

# assert methods in the unittest.TestCase class

"""
Assert Methods Available from the unittest Module 
Method                         Use 
assertEqual(a, b)           Verify that a == b 
assertNotEqual(a, b)    Verify that a != b 
assertTrue(x)                 Verify that x is True 
assertFalse(x)                Verify that x is False 
assertIn(item, list)        Verify that item is in list
"""

# using the setUp() method in unittest
# when the setUp() method is included in the TestCase class
# it is run before each method starting with 'test_'
# it is used to reduce repetition of code in each test
# any objects created in the setUp() method are available
# in every  test_ method
