"""
Module with class to describe user account.
"""


class User:
    """
    Define characteristics for a user.
    """

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.username = self.first_name[0].lower() + self.last_name.lower()
        self.password = ""
        self.login_attempts = 0

    def describe_user(self):
        """
        Describe the user.
        """
        print(f"I am {self.first_name} {self.last_name}.")
        print(f"My user name is {self.username}.")
        print(f"My password is {self.password}.")
        print()

    def greet_user(self):
        """
        Display a greeting to the user.
        """
        print(f"Hi {self.first_name}!")
        print()

    def increment_login_attempts(self):
        """
        Track the number of login attempts to this user's account
        """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """
        Reset the number of login attempts to zero.
        """
        self.login_attempts = 0
