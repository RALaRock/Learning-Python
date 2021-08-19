# 9-5. Login Attempts:
# Add an attribute called login_attempts to your User class from
# Exercise 9-3 (page 162). Write a method called increment_login_
# attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets
# the value of login_attempts to 0.
# Make an instance of the User
# class and call increment_login_attempts() several times. Print the
# value of login_attempts to make sure it was incremented properly,
# and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.age = 0
        self.height = 0
        self.eye_color = ""
        self.username = self.first_name[0].lower() + self.last_name.lower()
        self.password = ""
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Frank", "Beets")
print(user.username)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"The user: {user.username} made {user.login_attempts} login attempts.")
user.reset_login_attempts()
print(f"The user: {user.username} made {user.login_attempts} login attempts.")

user.describe_user()
