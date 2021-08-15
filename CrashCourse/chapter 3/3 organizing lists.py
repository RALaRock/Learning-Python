# methods for organizing lists

# sort() method permanently changes list order
cars = ["bmw", "ford", "dodge", "chevy", "merc"]
print(cars)
cars.sort()
print(cars)
# reverse order
cars.sort(reverse=True)
print(cars)

# sorting temporarily using the sorted() function
print(sorted(cars))  # sort order changed
print(cars)  # sort order of original list not changed

print()
print(cars)

# what happens when case varies?
cars = ["BMW", "Ford", "dodge", "chevy", "Merc"]
print(sorted(cars))
# capitalized letters are grouped together first

# reversing the order of a list, this is not a sort
cars.reverse()
print(cars)
# this permanently reverses the order of the list

print()

# finding the length of a list
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# use len() funciton
print(len(test_list))
# using for loop
count = 0
for i in test_list:
    count += 1

print(count)
