# 9-2. Three Restaurants:
# Start with your class from Exercise 9-1. Create three different instances
# from the class, and call describe_restaurant() for each instance.


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


def show_restaurant(restaurant):
    """Display information about an instance of the Restaurant class."""
    print()
    print(f"My restaurant is called {restaurant.restaurant_name}.")
    print(f"We serve {restaurant.cuisine_type} food.")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


restaurant1 = Restaurant("Wong's Tongs", "Chinese")
show_restaurant(restaurant1)

restaurant2 = Restaurant("Bill's Burgers", "good old 'merican")
show_restaurant(restaurant2)

restaurant3 = Restaurant("Ali's Alleys", "middle eastern")
show_restaurant(restaurant3)

print()
