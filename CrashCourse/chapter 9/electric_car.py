"""
Module to describe an electric car.
"""

# import car2 module which only contains Car class
from car2 import Car


# create an attribute class for Battery
class Battery:
    """
    Creating a sub class for a part of a battery powered car.
    Parent class: Car()
    """

    # using a optional parameter battery_size
    # can instantiate with or without battery_size
    # defaults to 75 if argument not provided in call
    def __init__(self, battery_size=75):
        # initialize battery attributes
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a description of the battery size."""
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """Print out the cars range based on battery size."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 0

        if range:
            print(f"This car can go about {range} miles on a full charge.")
        else:
            print(f"Unknown range for {self.battery_size}-kwh battery.")

    def set_battery_size(self, battery_size):
        self.battery_size = battery_size

    def upgrade_battery(self):
        """
        Check battery size and set the capacity to 100 if
        it is not already 100.
        """
        if self.battery_size != 100:
            self.battery_size = 100


# create a subclass of Car for electric cars
class ElectricCar(Car):

    # the init method of the child class takes in info needed to
    # create a parent class instance
    def __init__(self, make, model, year):
        """Initialiize the attributes from the parent class"""
        """super() is a function that runs a method in a parent class"""
        super().__init__(make, model, year)

        self.battery = Battery()

    # override the fill_gas_tank method in the car class
    def fill_gas_tank(self, added_gas):
        print("Electric cars do not need gas.")
