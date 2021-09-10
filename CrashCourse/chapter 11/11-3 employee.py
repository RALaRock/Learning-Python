"""
11-3. Employee: 
Write a class called Employee. 
The __init__() method should take in a first name, a last name, and an annual 
salary, and store each of these as attributes. Write a method called 
give_raise() that adds $5,000 to the annual salary by default but also accepts 
a different raise amount. Write a test case for Employee. 
Write two test methods, test_give_default_raise() and 
test_give_custom_raise(). Use the setUp() method so you don’t have to create 
a new employee instance in each test method. 
Run your test case, and make sure both tests pass.
"""

# create Employee class
# see employee.py
# test it here
from employee import Employee

an_employee = Employee("Rocky", "Smith", 100000)
an_employee.display_name()
an_employee.display_salary()
an_employee.give_raise()
an_employee.display_salary()
an_employee.give_raise(5)
an_employee.display_salary()

# test it using unittest, see test_employee.py
