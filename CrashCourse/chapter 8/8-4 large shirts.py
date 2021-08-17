# 8-4. Large Shirts:
# Modify the make_shirt() function so that shirts are large by
# default with a message that reads I love Python. Make a large
# shirt and a medium shirt with the default message, and a shirt
# of any size with a different message.


def make_shirt(size="large", message="I love Python"):
    """make_shirt(size, message)
    displays a text message of the text that will be printed on shirt
    """
    print(f"We will print '{message}' on a {size} size shirt.")


# call with default values
make_shirt()
make_shirt("medium")
make_shirt("small", "This is a shirt")

# call by position
make_shirt("large", "LA Rocks!!")
# call by keyword
make_shirt(message="I love feet", size="medium")
