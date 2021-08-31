"""
10-4. Guest Book: 
Write a while loop that prompts users for their name. When they enter their 
name, print a greeting to the screen and add a line recording their visit in a 
file called guest_book.txt. Make sure each entry appears on a new line in the 
file.
"""

filename = "guest_book.txt"

while True:
    name = input("Enter your name (or nothing to quit): ").title()
    if not name:
        break

    print(f"Hi {name}!")

    with open(filename, "a") as file_object:
        file_object.write(name + "\n")
