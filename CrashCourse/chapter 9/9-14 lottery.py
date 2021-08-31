# 9-14. Lottery:
# Make a list or tuple containing a series of 10 numbers and
# five letters. Randomly select four numbers or letters from
# the list and print a message saying that any ticket matching
# these four numbers or letters wins a prize.

from random import choice

# possible characters that appear on the ticket
numbersandletters = ["a", "b", "c", "d", "e", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# a list to hold the winning value characters
winner = []
# the winning value characters converted to a space delimited string
winning_value = ""

# build a winning 4 element list
for x in range(1, 5):
    winner.append(choice(numbersandletters))

# assemble the winning value as a string
for x in winner:

    if type(x) == str:
        chr = x.upper()
    else:
        chr = str(x)

    winning_value += chr

# display the winning value message
print(f"Tickets that match this:{winning_value} are winners!")
