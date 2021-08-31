# 9-13. Dice:
# Make a class Die with one attribute called sides,
# which has a default value of 6. Write a method
# called roll_die() that prints a random number
# between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times. Make a
# 10-sided die and a 20-sided die. Roll each die
# 10 times.


class Die:

    from random import randint

    def __init__(self) -> None:

        # create a number of sides attripute
        self.sides = 0

    def roll_die(self, sides=6):
        """
        print a random number between 1 and
        the number of sides the die has.
        """
        self.sides = sides
        print(f"Number of sides: {sides}")
        print(f"Roll: {self.randint(1, self.sides)}")


# instantiate Die class
dice = Die()


def roll_die(count, sides=6):
    """
    Roll a die the specified number of times with the
    specified number of sides.
    """
    for x in range(1, count + 1):
        print(f"Roll number: {x}")
        dice.roll_die(sides)


# roll with default number of sides, 6
roll_die(10)

# roll 10 sided die 10 times
roll_die(10, 10)

# roll 20 sided die 10 times
roll_die(8, 20)
