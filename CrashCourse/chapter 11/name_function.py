# this one works
# def get_formatted_name(first, last):
#    """Generate a neatly formatted full name."""
#    full_name = f"{first} {last}"
#   return full_name.title()


# modifying function such that it will fail the unit test
# for first name, last name
# def get_formatted_name(first, middle, last):
#    """Generate a neatly formatted full name."""
#    full_name = f"{first} {middle} {last}"
#    return full_name.title()

# The above fails testing with this:


# modifying function such that it will pass the unit test
# for first name, last name and have and optional middle
# name
def get_formatted_name(first, last, middle=""):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
