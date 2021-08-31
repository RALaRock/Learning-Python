"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate
 program that reads in this value and prints the message, “I know your
  favorite number! It’s _____.”
"""

import json


def load_favorite_number():
    """
    Retrieve favorite number from a json file if it exists.
    """
    filename = "favorite_number.json"
    try:
        with open(filename, "r") as f:
            number = json.load(f)
        print(f"Your favorite number is: {number}")
    except FileNotFoundError:
        print(f"Cannot find the file: {filename}.")


load_favorite_number()
