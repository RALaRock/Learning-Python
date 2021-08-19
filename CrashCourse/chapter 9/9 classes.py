# creating and using classes
# dog class
# properties: age, name
# methods: sit, roll over
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to command"""
        print(f"{self.name} rolled over.")


# a function that is part of a class is a method
# the __init__() method runs when new instance of class is created
# the self parameter of the __init__() method is required, must be  the
# first parameter, is a reference to the instance of the class. The self
# parameter is passed to all methods in the class when they are called..
# when an instance of a class is created self is passed automatically.
# Only specify the other parameters.
# Any variable prefaced with 'self.' is available to every module in the
# class

# instantiating a class
my_dog = Dog("Willie", 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.roll_over()
my_dog.sit()
print()
print()


# inhertitance
# create a Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.odometer_reading = 0
        self.gas_tank_level = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, added_gas):
        self.gas_tank_level = added_gas
        print(f"The gas tank has {added_gas} gallons in it.")


# if a class is used in another class, the used class must be before
# the using class in the code stream


class Battery:
    """Creating a sub class for a part of a battery powered car"""

    # using a variable parameter battery_size
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
            print(
                f"Unknown battery size ({self.battery_size}) specified. Range unknown."
            )

    def set_battery_size(self, battery_size):
        self.battery_size = battery_size


# create a subclass of Car
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialiize the attributes from the parent class"""
        """super() is a function that runs a function in a parent class"""
        super().__init__(make, model, year)

        # replace battery methods with those from the Battery class
        # create an instance of the Battery class with a default battery size
        # of 75 since a value for battery size is not passed here
        self.battery = Battery()
        # attributes in the child class
        # self.battery_size = 75

    # replace battery methods with those from the Battery class
    # moved to Battery class
    # def describe_battery(self):
    #   """Print a statement describing the battery."""
    #   print(f"This car has a {self.battery_size}-kwh battery.")

    # this replaces the method in the Car parent class
    # left the added_gas parameter so that call does not fail if
    # the argument is provided as it is in the Car class
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
# the above changed to this because method moved to battery class
# and battery class instantiated withing the ElectricCar class
my_tesla.battery.describe_battery()

# Overriding methods in the parent Car class
# define a method in the child class with the same name
# as a the method in the parent class
my_tesla.fill_gas_tank(16)
print(f"Gas tank level: {my_tesla.gas_tank_level}")

my_tesla.battery.get_range()
my_tesla.battery.set_battery_size(100)
my_tesla.battery.get_range()
my_tesla.battery.set_battery_size(110)
my_tesla.battery.get_range()
