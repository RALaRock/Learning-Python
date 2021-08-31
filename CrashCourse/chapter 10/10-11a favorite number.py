"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate
 program that reads in this value and prints the message, “I know your
  favorite number! It’s _____.”
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


new_favorite_number()
