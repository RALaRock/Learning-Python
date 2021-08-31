# stroring data
# using the json module
# json provides a way to dump simple Python data structures like
# lists and dictionaries into files and read them from files
# the json data format is not specific to Python and can be used
# to share data between programs
# javascript object notation format

# json.dump to store data and and json.load to retrieve it

# example, store some data using json
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers.json"

# create the file and fill it with data in json format
with open(filename, "w") as f:
    # json.dump(data, filehandle)
    json.dump(numbers, f)

# read the json file and print it
with open(filename, "r") as f:
    # json.dump(data, filehandle)
    numbers = json.load(f)
print(numbers)


# remember_me.py
# attempt to get the username from a file
# if the file not found, assume it's a new user
# prompt for the username then store it
# print a greeting
filename = "username.json"

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Enter your user name: ")
    with open(filename, "w") as f:
        json.dump(username, f)
        print(f"We will remember your username {username} for next time.")
else:
    print(f"Welcome back, {username}!")

# refactoring
#  moving code from the main module to
# one or more functions to improve readability
# and function


def get_stored_username():
    """
    Attempt to get saved user name.
    Return username or None
    """
    try:
        with open(filename, "r") as f:
            username = json.load(f)
    except FileNotFoundError:
        username = None
    return username


def get_new_username():
    """
    prompt for a new user name
    if one entered, save it
    return username or none
    """
    username = None
    while not username:
        username = input("Enter your user name: ")
        if username:
            # overwrites file if it already exists.
            with open(filename, "w") as f:
                json.dump(username, f)
            return username


def greet_user():
    """
    Greet the user by username.
    """
    username = get_stored_username()
    if username:
        print(f"Welcome back {username}.")
    else:
        get_new_username()
        print(f"We will remember your username '{username}' for next time.")


filename = "username.json"
greet_user()