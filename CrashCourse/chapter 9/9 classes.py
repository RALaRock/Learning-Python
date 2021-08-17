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