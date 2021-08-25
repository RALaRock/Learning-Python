"""
Properties that account users have.
Used by the User2 module
"""

# need this because the Admin class depends on User
from user2 import User


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
