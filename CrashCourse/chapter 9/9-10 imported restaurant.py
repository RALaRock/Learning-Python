# 9-10. Imported Restaurant:
# Using your latest Restaurant class, store it in a module.
# Make a separate file that imports Restaurant. Make a
# Restaurant instance, and call one of Restaurant’s
# methods to show that the import statement is working properly.

from restaurant import Restaurant as RES


def show_restaurant(restaurant):
    """Display information about an instance of the Restaurant class."""
    print()
    print(f"My restaurant is called {restaurant.restaurant_name}.")
    print(f"We serve {restaurant.cuisine_type} food.")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()


restaurant1 = RES("Wong's Tongs", "Chinese")
show_restaurant(restaurant1)

restaurant2 = RES("Bill's Burgers", "good old 'merican")
show_restaurant(restaurant2)

restaurant3 = RES("Ali's Alleys", "middle eastern")
show_restaurant(restaurant3)

print()
