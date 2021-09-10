"""
Write a class called Employee. 
The __init__() method should take in a first name, a last name, and an annual 
salary, and store each of these as attributes. Write a method called 
give_raise() that adds $5,000 to the annual salary by default but also accepts 
a different raise amount. 
"""


class Employee:
    """Store information about an employee."""

    def __init__(self, first_name, last_name, salary) -> None:
        """Create name and salary attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give a salary increase of 5000 or whatever is specified."""
        self.salary += amount

    def display_name(self):
        """Format the employee name and display it."""
        print(f"{self.first_name} {self.last_name}".title())

    def display_salary(self):
        """Show the employee's salary."""
        print(f"{self.salary}")
