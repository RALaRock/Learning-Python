# 9-4. Number Served:
# Start with your program from Exercise 9-1 (page 162). Add an attribute
# called number_served with a default value of 0. Create an instance
# called restaurant from this class. Print the number of customers
# the restaurant has served, and then change this value and print it
# again.
# Add a method called set_number_served() that lets you set
# the number of customers that have been served. Call this method
# with a new number and print the value again.
# Add a method called
# increment_number_served() that lets you increment the number of
# customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in,
# say, a day of business.


class Restaurant:
    """
    Describes the attributes of a restaurant.
    """

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


restaurant = Restaurant("Wong's Tongs", "Chinese")
print(f"My restaurant is called {restaurant.restaurant_name}.")
print(f"We serve {restaurant.cuisine_type} food.")
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Number served: {restaurant.number_served}.")
restaurant.number_served = 102
print(f"Number served: {restaurant.number_served}.")

restaurant.set_number_served(39)
print(f"Number served: {restaurant.number_served}.")

restaurant.increment_number_served(10)
print(f"Number served: {restaurant.number_served}.")
