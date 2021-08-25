# module level docstring
"""
A class that can be used to represent a car.
"""


class Car:
    def __init__(self, make, model, year):
        # these parameters are passed when class instantiated
        self.make = make
        self.model = model
        self.year = year

        # these parameters are not passed, have default values,
        # can be manipulated as part of the class
        self.odometer_reading = 0
        self.gas_tank_level = 0

    # these are methods within the class
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        """
        Set the odometer to a given value.
        Reject a change that rolls back the miles.
        """
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back the mileage.")

    # this method has  required parameter, miles
    def increment_odometer(self, miles):
        self.odometer_reading += miles

    # this method has a required parameter, added_gas
    def fill_gas_tank(self, added_gas):
        self.gas_tank_level = added_gas
        print(f"The gas tank has {added_gas} gallons in it.")
