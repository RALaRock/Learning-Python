# make a list of the first 10 cubes

values = []
for value in range(1, 11):
    values.append(value ** 3)

print(values)

# using list comprehension
values = [x ** 3 for x in range(1, 11)]
print(values)
