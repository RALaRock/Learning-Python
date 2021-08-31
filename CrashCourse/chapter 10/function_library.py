# some useful functions
"""
A collection of useful functions.
"""


# format and return a full name
def full_name(first, last, middle=""):
    """return a properly formatted full name"""
    if first and middle and last:
        fullname = f"{first} {middle} {last}"
    elif first and last:
        fullname = f"{first} {last}"
    else:
        fullname = ""

    return fullname.title()


# function strips leading, training and extra spaces in a string
# returns the space stripped string
def strip_all_spaces(string):
    """strips leading, training and extra spaces in a string"""
    return " ".join(string.split())


# end def


#  remove all occurences of an item from a list
def remove_items(test_list, item):
    """remove all occurences of an item from a list"""
    # using list comprehension to perform the task
    res = [i for i in test_list if i != item]

    return res


# end def


# replace an item in a list with another item
# needs error checking for empty list and olditem not existing
# EX: print(list_replace(guests, noshow, replacement))
def list_replace(items, olditem, newitem):
    items[items.index(olditem)] = newitem
    return items


# end def

# test if a string value can be converted into a float
def str_is_float(val=""):
    """test if a string value can be converted into a float"""
    if type(val) == str:
        try:
            float(val)
        except ValueError:
            return False
        else:
            return True
    else:
        return False


# end def

# test if a string value can be converted into an integer
def str_is_int(val=""):
    """test if a string value can be converted into an integer"""
    if type(val) == str:
        try:
            int(val)
        except ValueError:
            return False
        else:
            return True
    else:
        return False


# end def


def str_is_number(val):
    """test if a string value can be converted into a number"""
    if str_is_float(val):
        return True
    if str_is_int(val):
        return True
    return False


# end def
