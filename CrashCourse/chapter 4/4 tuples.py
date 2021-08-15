
# working with tuples
# an immutable list is called a tuple
# immutable means cannot change the list

cube_dimensions = (4, 10, 2)  # length, width, depth
# access the elements of the tuple using indexes like lists
cube_length = cube_dimensions[0]
cube_width = cube_dimensions[1]
cube_depth = cube_dimensions[2]
print('length is ' + str(cube_length))

# can't change the elements of a tuple, this causes an error
# cube_dimensions[0] = 12

# tuples are defined by the presence of a comma
# to define a single element tuple add a comma
atuple = (12,)
print(atuple)

# loop through tuple
print(cube_dimensions)
for dimension in cube_dimensions:
    print(dimension)

# can't change items in a tuple, but can change entire tuple
cube_dimensions = (4, 3, 12)
print(cube_dimensions)
for dimension in cube_dimensions:
    print(dimension)
