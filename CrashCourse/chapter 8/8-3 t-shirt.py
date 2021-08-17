# 8-3. T-Shirt:
# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function
# should print a sentence summarizing the size of the shirt and the
# message printed on it. Call the function once using positional
# arguments to make a shirt. Call the function a second time using
# keyword arguments.


def make_shirt(size, message):
    """make_shirt(size, message)
    displays a text message of the text that will be printed on shirt
    """
    print(f"We will print '{message}' on a {size} size shirt.")


# call by position
make_shirt("large", "LA Rocks!!")
# call by keyword
make_shirt(message="I love feet", size="medium")
