# user input and while loops

# input() function
answer = input("Enter something...")
print(answer)

# input() returns a string, if you want a number the result must be
# cast to the appropriate type
answer = input("How old are you? ")
if answer == "":
    answer = 0
elif int(answer) >= 21:
    print("You can drink here.")
else:
    print("You are not old enough to drink here.")

# modulo operator returns the remainder of a division
print(5 % 2)

# while loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# use a FLAG variable for a while loop
# that should exit based on multiple conditions
flag = True
prompt = "Enter something to display or enter 'quit' to stop. "
while flag:
    message = input(prompt)
    if message.lower() == "quit":
        flag = False
    else:
        print(message)
print("This is after the end of the first while loop.")

# using BREAK to exit a loop
# BREAK exits loop immediately withou executing any other statements
# in the loop, resumes execution next statement after loop
prompt = "Enter something to else display or enter 'quit' to stop. "
while True:
    message = input(prompt)
    if message.lower() == "quit":
        break
    elif message == "":  # blank answer quits too
        break
    else:
        print(message)
print("This is after the end of the second while loop.")

# using CONTUNUE in a loop
# stops loop execution and returns to the start of the loop
# print only the odd numbers
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print("after while loop")

# using while loops with lists and dictionaries
# avoid making chnages to a list or dictionary while iterating through it
# using a for loop
# if changes to the list or dictionary is required, use a while loop instead

# moving items from one list to another
# create a list of new, unverified users to a web site
# once verified move the new user to the verified list
unverified_users = ["alice", "bill", "sam", "penny"]
verified_users = []

while unverified_users:
    current_user = unverified_users.pop()
    print(f"Verifying user: {current_user.title()}.")
    verified_users.append(current_user)

print("\nThe following users have been confirmed...")
for current_user in verified_users:
    print(f"\t{current_user.title()}")

# removing all instances of a specific value from a list
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
while "cat" in pets:
    pets.remove("cat")
print(pets)

