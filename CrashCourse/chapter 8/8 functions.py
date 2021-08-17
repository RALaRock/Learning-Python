# def function_name(parameters):
#    """ docstring """
#    #code to execute
# function_name(parameters)

# positional arguments
# passed in the same order as defined

# keyword arguments
# passed as variable name and value

# lists and dictionary arguments
# passing multiple values in one variable

# argument passing types
def animal(animal_type, animal_name):
    print(f"I have a {animal_type} named {animal_name}.")


# positional
animal("hamster", "harry")

# keyword arguments
# define the parameter name in the call, order does not matter
# the function definition parameters don't change, but
# the call to the function includes the parameter name
animal(animal_name="harry", animal_type="hamster")

# default values for parameters
# default argument value used if no argument passed
def describe_pet(name, animal_type="dog"):
    print(f"I have a {animal_type} named {name}.")


# uses the default value for the animal type
describe_pet("sammy")

# note: the keyword arguments must be after the positional arguments

# return values
def full_name(first, last, middle=""):
    """return a properly formatted full name"""
    if first and middle and last:
        fullname = f"{first} {middle} {last}"
    elif first and last:
        fullname = f"{first} {last}"
    else:
        fullname = ""

    return fullname.title()


# passing a list to a function
def greet_users(users):
    for name in users:
        print(f"Hello {name}.")
    users = ["bambam"]


users = ["fred", "barney", "wilma", "betty"]
greet_users(users)
print(users)


# lists are passed to functions by reference
# changes made to lists in a function have scope outside the function
def print_models(unprinted, printed):
    while unprinted:
        current = unprinted.pop()
        print(current)
        printed.append(current)


unprinted = ["phone", "robot", "dice"]
printed = []
print(f"unprinted: {unprinted}")
print(f"printed: {printed}")
print_models(unprinted, printed)
print(f"unprinted: {unprinted}")
print(f"printed: {printed}")
