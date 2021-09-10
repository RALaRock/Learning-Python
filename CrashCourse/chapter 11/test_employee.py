"""Tests for the Employee class.
    test_give_default_raise() and 
    test_give_custom_raise(). Use the setUp() method so you don’t have to
    create a new employee instance in each test method
"""
import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):
    """Test case for the Employee class"""

    def setUp(self):
        first_name = "Randall"
        last_name = "Clipodorn"
        salary = 45000
        self.an_employee = Employee(first_name, last_name, salary)

    def test_give_default_raise(self):
        """test case for default raise"""
        self.an_employee.give_raise()
        self.assertEqual(50000, self.an_employee.salary)

    def test_give_custom_raise(self):
        """test case for custom raise"""
        a_raise = 10
        new_salary = self.an_employee.salary + a_raise
        self.an_employee.give_raise(a_raise)
        self.assertEqual(new_salary, self.an_employee.salary)


if __name__ == "__main__":
    unittest.main()
