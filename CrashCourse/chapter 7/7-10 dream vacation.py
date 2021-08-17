# 7-10. Dream Vacation: Write a program that polls users about
# their dream vacation. Write a prompt similar to If you could
# visit one place in the world, where would you go? Include a
# block of code that prints the results of the poll.

# init
destination = ""
count = 0
prompt = "If you could travel to anywhwer in the world, where would you want to go? "
destinations = {}

# do poll, ask where people want to go
while True:

    # ask poll question
    destination = input(f"{prompt} (enter nothing or 'quit' to stop) ")

    # check for quit
    if destination == "" or destination.lower() == "quit":
        break

    # count the answers
    if destinations.get(destination):  # use get() to return none if new destination
        destinations[destination] += 1
    else:
        destinations[destination] = 1  # new destination

# display poll results
for destination in destinations:
    count = destinations[destination]
    print(f"{count} people want to go to {destination.title()}.")
