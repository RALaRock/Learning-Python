# 9-9. Battery Upgrade:
# Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery().
# This method should check the battery size and set the capacity
# to 100 if it isn’t already. Make an electric car with a default
# battery size, call get_range() once, and then call get_range() a
# second time after upgrading the battery. You should see an
# increase in the car’s range.


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


my_tesla = ElectricCar("tesla", "model s", 2020)

# get_descriptive_name() is a method in the Car class inherited in the
# ElectricCar class
print(my_tesla.get_descriptive_name())
# read_odometer() is a method in the Car class
my_tesla.read_odometer()
# describe_battery() is a method in the child class ElectricCar
# my_tesla.describe_battery()
# the above changed to below because method moved to battery class
# and battery class instantiated withing the ElectricCar class
my_tesla.battery.describe_battery()

# Overriding methods in the parent Car class
# define a method in the child class with the same name
# as a the method in the parent class
my_tesla.fill_gas_tank(16)
print(f"Gas tank level: {my_tesla.gas_tank_level}")

# show range for default battery size
my_tesla.battery.get_range()
# upgrade battery and show range
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
# set new battery size and show range, if possible
my_tesla.battery.set_battery_size(80)
my_tesla.battery.get_range()
