# exceptions
# when Python finds a state when it does not know what to do
# it raises and exception object
# if the exception is not handled in the program a traceback
# error is generated that includes the exception information
# exceptions are handled through try - except blocks
# try asks Python to try something and, if it fails, the except
# code is run

# handing the ZeroDivisionError exception
"""
try:
    print(5 / 0)
except ZeroDivisionError:
    print("Can't divide by zero.")

try:
    # code that might cause an exception error
except exceptionerror1:
    # code to run if the exception happens
except exceptionerror2:
    # can have several specifid exceptions
except (tuple, of, exeptions):
    # can pass a tuple of exceptions
else:
    # code to run if and exception error DOES NOT happen
finally:
    # code run whether is an exception or not

# https://www.askpython.com/python/python-exception-handling
"""

# handling file not found exception
filename = "alice.txt"
try:
    # specify the file encoding here or get UnicodeDecodeError
    with open(filename, encoding="utf-8") as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print(f"File {filename} not found.")
except UnicodeDecodeError:
    print("Unicode error reading in file.")
except:  # avoid using except without specific error
    pass  # used to take no action if an unknown error occurs
else:
    # count the number of words in the file
    words = contents.split()
    numwords = len(words)
    print(f"There are approximately {numwords} words in {filename}.")
