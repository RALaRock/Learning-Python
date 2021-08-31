"""
10-12. Favorite Number Remembered: 
Combine the two programs from Exercise 10-11 into one file. If the number is
already stored, report the favorite number to the user. If not, prompt for
the user’s favorite number and store it in a file. Run the program twice to
see that it works.
"""

import json
from function_library import str_is_int


def new_favorite_number():
    """
    Prompt for a person's favorite number.
    Store the numer using json.
    """
    number = input("Enter your favorite integer: ")
    if str_is_int(number):
        filename = "favorite_number.json"
        with open(filename, "w") as f:
            json.dump(number, f)
        return number


def load_favorite_number():
    """
    Retrieve favorite number from a json file if it exists.
    """
    filename = "favorite_number.json"
    try:
        with open(filename, "r") as f:
            number = json.load(f)
        return number
    except FileNotFoundError:
        return None


# check if favorite number exists, if so, display it, if not, get it
number = load_favorite_number()
if number:
    print(f"Your favorite number is: {number}")
else:
    number = new_favorite_number()
    print(f"Your favorite number '{number}' has been saved.")
