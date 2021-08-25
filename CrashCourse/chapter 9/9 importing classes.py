# importing classes

# storing a single class in a file
# see car.py and my_car.py

# storing multiple classes in a file
# added battery and electric car classes to car.py
# see car.py, battery and electricar classes

# importing multiple classes from a module
# see my_cars.py, added import for electric cars

# importing and entire module
# uses dot notation to indicate class in use
# makes code easy to read
# avoids naming conflicts

# importing all the classes in a module
# from module_name import *
# NOT recommended
# it's unclear which classes are used from the module
# can lead to confusion with names in the file
# can create naming errors if import something with the same name
# better to import the entire module and use
# module_name.class_name notation


# importing a module into a module
# when a class in one module depends on a class in another module
# import the required class into the module that depends on it
# import the module containing the class depended on first

# using Aliases
# from module_name import class_name as alias
