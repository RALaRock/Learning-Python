"""
10-13. Verify User: 
The final listing for remember_me.py assumes either that the user has already 
entered their username or that the program is running for the first time. We 
should modify it in case the current user is not the person who last used the 
program. Before printing a welcome back message in greet_user(), ask the user 
if this is the correct username. If it’s not, call get_new_username() to get the 
correct username.
"""

import json


def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def set_stored_username(username):
    """Set stored username."""
    filename = "username.json"
    with open(filename, "w") as f:
        json.dump(username, f)


def greet_user():
    """
    Greet the user by name.
    Ask if the username stored is correct,
    if not prompt for a new user name.
    """
    username = get_stored_username()
    if username:
        # if they enter a user name, update it
        answer = input(f"Please enter your user name [{username}]: ")
        if answer:
            set_stored_username(answer)
            print(f"Welcome {answer}!")
        else:
            print(f"Welcome back {username}!")


greet_user()
