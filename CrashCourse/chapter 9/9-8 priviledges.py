# 9-8. Privileges:
# Write a separate Privileges class. The class should have one attribute,
# privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make a Privileges
# instance as an attribute in the Admin class. Create a new instance of
# Admin and use your method to show its privileges.


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


class Priviledges:
    def __init__(self) -> None:

        # priviledges attribute
        self.priviledges = [
            "add post",
            "delete post",
            "ban user",
            "create user",
            "delete user",
        ]

    def show_priviledges(self):
        # print(f"{self.username} has the following priviledges:")
        if self.priviledges:
            print("This account has the following priviledges:")
            for priviledge in self.priviledges:
                print(f"\t{priviledge}")
        else:
            print("No priviledges have been granted this user.")


class Admin(User):
    """
    Describe admin type of user.
    """

    def __init__(self, first_name, last_name):
        # this instantiates the user class
        super().__init__(first_name, last_name)

        self.priviledges = Priviledges()


this_admin = Admin("Jackson", "Browne")
this_admin.describe_user()
this_admin.priviledges.show_priviledges()
