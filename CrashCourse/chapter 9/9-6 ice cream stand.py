# 9-6. Ice Cream Stand:
# An ice cream stand is a specific kind of restaurant. Write a class
# called IceCreamStand that inherits from the Restaurant class you
# wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either
# version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream
# flavors. Write a method that displays these flavors. Create an
# instance of IceCreamStand, and call this method.


class Restaurant:
    """Describes the attributes of a restaurant."""

    # create the class attributes when this class is instantiated
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints a description of the restaurant."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} eatery.")

    def open_restaurant(self):
        """Sets the restaurant state to open."""
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, increment):
        self.number_served += increment


class IceCreamStand(Restaurant):
    """Describe an ice cream restaurant based on Restaraunt class"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry"]

    def describe_flavors(self):
        if self.flavors:
            print("We offer these flavors: ")
            for flavor in self.flavors:
                print(flavor)
        else:
            print("There are no flavors at this time.")


my_ice_cream_parlor = IceCreamStand("Blockos", "Dessert")
my_ice_cream_parlor.describe_restaurant()
my_ice_cream_parlor.describe_flavors()
