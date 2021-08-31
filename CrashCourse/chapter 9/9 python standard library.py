# can use any library using the import command at the top of a file

# generate a random integer between two integers
from random import randint

print(randint(1, 6))

# randomly choose an element from a tuple
from random import choice

atuple = ["ted", "sam", "carl", "ed"]
print(choice(atuple))

# the random module is NOT suitable for security applications
