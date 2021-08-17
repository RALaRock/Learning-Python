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

# passing by value
# use the [:] slice operator on the list to create a copy
unprinted = ["phone", "robot", "dice"]
printed = []
print(f"unprinted: {unprinted}")
print(f"printed: {printed}")
print_models(unprinted[:], printed)
print(f"unprinted: {unprinted}")
print(f"printed: {printed}")

# passing an arbitrary number of arguments
# the * causes the arguments to be converted into a tuple
# tuples are ordered and unchangeable
# expect to see *args to indicate arbitrary number of arguments
def pizza(*toppings):
    print(toppings)


pizza("sauce")
pizza("cheese", "mushrooms", "pepperoni")
print()

# passing arbitrary number of arguments of unknown type
# using a ** causes the arguments to be converetd into a dictionary
# use this when need different argument data types like string and integer
# expect to see **kwargs to indicate arbitrary number of keyword arguments
def build_user(first, last, **user_info):
    """**user_data is and arbitrary dictionary of key value pairs"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


print(build_user("rocky", "raccoon", location="forest", type="rodent"))
print()
print(build_user("rocky", "raccoon", location="forest", type="rodent", age=100))
print()


# storing functions in modules
# store functions in separate files called modules
# a module is a file containing functions with a .py extension

# import an entire module
# import every function in the module, pizza.py
import pizza

# to use the module function preface with the name of the module
# followed by a period followed by the function name
# modulename.functionname(parameters)
pizza.make_pizza(16, "pepperoni")
pizza.make_pizza(16, "pepperoni", "peppers", "extra sauce", "beef", "boogers")

# import specific functions rather than the whole module
# use from modulename import functioname, functionname, functionname, ...
# importing specific functions, don't need to specifiy the module with dot

# using AS to give a function an alias
# useful when the name of a function might conflict with another name
# of if the function name is long and you want to shorten it
# from modulename import functionname as alias

# using AS to give a module an alias
# import modulename as alias

# import all functions in a module
# use the * modifier
# from modulename import *
# imports all the functions making it possible to not use modulename.functionname
# notation
# risky with 3rd party modules since might end up with naming conflicts
# best to import just the desire functions or use the dot notation

# styling functions and modules
# use descriptive names with lower case letters and underscores between words
# include a comment that describes the module and/or function purpose
