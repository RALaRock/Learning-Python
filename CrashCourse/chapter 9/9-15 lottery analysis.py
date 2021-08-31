# 9-15. Lottery Analysis: You can use a loop to see how hard it
# might be to win the kind of lottery you just modeled. Make a
# list or tuple called my_ticket. Write a loop that keeps pulling
# numbers until your ticket wins. Print a message reporting
# how many times the loop had to run to give you a winning
# ticket.

from random import choice


def winning_value(choices, length=4):
    """Build a winning lottery string of specified length."""

    # a list to hold the winning value characters
    winner = []
    winnerstr = ""

    # build a winning 4 element list
    for x in range(1, length + 1):
        winner.append(choice(numbersandletters))

    # assemble the winning value as a string
    for x in winner:

        if type(x) == str:
            chr = x.upper()
        else:
            chr = str(x)

        winnerstr += chr

    return winnerstr


# possible characters that appear on the ticket
numbersandletters = ["a", "b", "c", "d", "e", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ticketnumber to match
ticketnumber = "ABCD"
# number of times to match the ticketnumber
numberoftries = 4

iterations = 0
successes = 0
totalcount = 0
averagecount = 0

# count the number of times must generate a number until match found
for x in range(1, numberoftries + 1):

    # look for a match for the ticket and
    # count the number of tries until match found
    count = 0
    value = ""
    while value != ticketnumber:
        value = winning_value(numbersandletters, len(ticketnumber))
        count += 1

    # display the winning value message
    print(
        f"For try #{x}, it took {count} number of tries to match the ticket "
        + f"number: {ticketnumber}."
    )

    successes = x
    totalcount += count

    print(f"Iterations: {count}.")
    print(f"Total iterations: {totalcount}.")


averagecount = totalcount / successes

# display the winning value message
print(
    f"For {numberoftries} attempts, it took an average of {averagecount} "
    + f"number of tries to match the ticket number: {ticketnumber}."
)
