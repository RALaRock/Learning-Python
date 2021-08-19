# 9-1. Restaurant:
# Make a class called Restaurant. The __init__() method for Restaurant
# should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two
# pieces of information, and a method called open_restaurant() that
# prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two
# attributes individually, and then call both methods.


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


restaurant = Restaurant("Wong's Tongs", "Chinese")
print(f"My restaurant is called {restaurant.restaurant_name}.")
print(f"We serve {restaurant.cuisine_type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
