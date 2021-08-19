# 9-7. Admin:
# An administrator is a special kind of user. Write a class
# called Admin that inherits from the User class you wrote
# in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). Add
# an attribute, privileges, that stores a list of strings like
# "can add post", "can delete post", "can ban user", and so
# on. Write a method called show_privileges() that lists the
# administrator’s set of privileges. Create an instance of Admin,
# and call your method.


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        self.username = self.first_name[0].lower() + self.last_name.lower()
        self.password = ""
        self.login_attempts = 0

    def describe_user(self):
        print(f"I am {self.first_name} {self.last_name}.")
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


class Admin(User):
    """Describe admin type of user."""

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.priviledges = [
            "add post",
            "delete post",
            "ban user",
            "create user",
            "delete user",
        ]

    def show_priviledges(self):
        print(f"{self.username} has the following priviledges:")
        if self.priviledges:
            for priviledge in self.priviledges:
                print(priviledge)
        else:
            print("No priviledges have been granted this user.")


this_admin = Admin("Jackson", "Browne")
this_admin.describe_user()
this_admin.show_priviledges()
