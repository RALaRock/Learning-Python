# 9-3. Users:
# Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that
# prints a summary of the user’s information. Make another method
# called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both
# methods for each user.


class User:
    def __init__(
        self, first_name, last_name, age, height, eye_color, username, password
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.eye_color = eye_color
        self.username = username
        self.password = password

    def describe_user(self):
        print(f"I am {self.first_name} {self.last_name}.")
        print(f"I am {self.age} years old and {self.height} centimeters tall.")
        print(f"My eyes are {self.eye_color}.")
        print(f"My user name is {self.username}.")
        print(f"My password is {self.password}.")
        print()

    def greet_user(self):
        print(f"Hi {self.first_name}!")
        print()


def show_user(user):
    """Display information about the user."""
    user.describe_user()
    user.greet_user()


bob = User("Bob", "Smith", 28, 76, "brown", "bsmith", "password")
show_user(bob)

hank = User("Hank", "Jones", 40, 58, "green", "hjones", "password")
show_user(hank)

fred = User("Fred", "Anderson", 12, 46, "blue", "fanderson", "password")
show_user(fred)
