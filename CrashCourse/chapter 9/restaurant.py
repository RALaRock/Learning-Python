"""
A module that contains classes to describe restaurants.
"""


class Restaurant:
    """
    Describes the attributes of a restaurant.
    """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints a description of the restaurant."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} eatery.")

    def open_restaurant(self):
        """Sets the restaurant state to open."""
        print(f"{self.restaurant_name} is open.")
