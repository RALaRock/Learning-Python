# looping through lists

# for loop for doing the same action on every list item
magicians = ["alice", "sam", "don", "bill"]
for magician in magicians:
    print(f"{magician.title()} is very clever at fooling poeple!")
    print("We are looking forward to the next trick!\n")
print("\nThanks for being so entertaining.")

# indenting where it's not needed will cause a compiler error
# indenting one or more spaces is counted as indenting
# print('this is an indention test')

print()

# lists of numbers

# the range() function to generate numbers
# range(start value)
# range(start value, value to end at, not included in range)
# always increases from start value, so (10, 5) has value in range
for value in range(1, 5):
    print(value)

print(range(1, 5))  # range does not create a list
print(list(range(1, 5)))  # list() converts the range to a list

temp = range(1, 5)
# temp becomes a range object
print(temp)
# the temp range object is the same as the range statement
print(list(temp))

# range has an increment paramenter
for number in range(0, 100, 10):
    print(number)

# print a list of squares between 1 and 10
squares = []
for number in range(1, 11):
    squares.append(number ** 2)
print(squares)

# some statistical functions for lists
print(min(squares))
print(max(squares))
print(sum(squares))

# list comprehensions
# newlist = [expression for item in iterable if condition == True]

# example, squares of numbers from 1 to 10:
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# example, all fruits with names containing 'a':
fruits = ["apple", "plum", "banana", "orange"]
a_fruits = [x for x in fruits if "a" in x]
print(a_fruits)

# this creates newlist with all fruits in it
newlist = [x for x in fruits]
print(newlist)

# only numbers less than 5
print([x for x in range(10) if x < 5])

# the item can be changed before iteration
print([x.upper() for x in fruits])

# replace all values in fruits that have an a in the name with yech
print([x if "a" not in x else "yech" for x in fruits])

# working with parts of a list
# specific group of items in a list is called a slice
# slicing a list
# specify the index of the first and last elements of
# the list you want to work with
# syntax: listname[start item number, last item to get]
values = list(range(10))
print(values)
values.reverse()
aslice = values[3:6]  # [start index, number of items to get]
print(aslice)
print()

# omit first index, assumes 0
print(values[:4])
# omit number of items assumes last item
print(values[2:])
# to get the last items in a list use a negative starting index
print(values[-3:])
# it is possible to skip items by prividing an increment
print(values[0:8:2])

# can use slices to reduce the number of for loop iterations
for value in values[:3]:  # first three values only
    print(value)
for value in values[::3]:  # every third value only
    print(value)
print()

# copying an entire list, THIS DOES NOT WORK
# it only creates a new reference to the same object
newvalues = values
print(values)
print(newvalues)
newvalues.append(11)
print(values)  # note values and newvalues still the same
print(newvalues)
print()

# copying a list using a slice
# this does work and creates another list
newvalues = values[:]  # omitting index and count yiels entire list
print(values)
print(newvalues)
newvalues.append(12)
print(values)  # note values and newvalues NOT  still the same
print(newvalues)
print()
