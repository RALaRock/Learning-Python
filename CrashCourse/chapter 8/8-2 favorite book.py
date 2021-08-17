# 8-2. Favorite Book:
# Write a function called favorite_book() that accepts one parameter,
# title. The function should print a message, such as One of my favorite
# books is Alice in Wonderland. Call the function, making sure to include
# a book title as an argument in the function call.


def favorite_book(title):
    """Print a message about a favorite book."""

    if title:
        print(f"One of my favorite books is {title.title()}.")
    else:
        print("No title parameter passed to function.")


favorite_book("The Idiot")

try:
    favorite_book()
except:
    print("Missing parameter in: favorite_book()")
    