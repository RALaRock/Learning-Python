"""
10-3. Guest: 
Write a program that prompts the user for their name. When they respond, 
write their name to a file called guest.txt.
"""

name = input("Enter your name: ") + "\n"

filename = "guest.txt"
with open(filename, "a") as file_object:
    file_object.write(name.title())
