# reading a file and printing it
# NOTE:
# had to change settings.json
# "python.terminal.executeInFileDir": false, to true
# for this to find the file
# with is a wrapper that automatically closes the open
# file when the with code block completes
# open('filename') as file_object
# filename is the full filename if the file is not in the
# current working directory
# file_object is an object handle to the file
# the read() method within the file_object
# returns the entire file as a single string
# with an extra blank line at the end

# with open("pi_digits.txt") as file_object:
#    contents = file_object.read()
#
# print(contents)

# using rstrip() removes the extra line from the
# file that is returned by the read() method
# print(contents.rstrip())

# to open files in other folders and directories
# must provide the file path
# a relative file path indicates a path relative to
# the file path of the currently running program
# following is a relative path:
with open("text_files/pi_digits.txt") as file_object:
    contents = file_object.read()

print(contents.rstrip())

# can also use an absolute path
with open(
    "c:/Users/Robert/Python/learning/Learning-Python/CrashCourse/chapter 10/text_files/pi_digits.txt"
) as file_object:
    contents = file_object.read()

print(contents.rstrip())

# reading files line by line
# using a for loop
filename = "c:/Users/Robert/Python/learning/Learning-Python/CrashCourse/chapter 10/text_files/pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# making a list of lines from a file
# when the with block is used the file closes at the end of the with block
# one way to retain ability to access file contents is to copy it into a list
filebuffer = []
with open(filename) as file_object:
    for line in file_object:
        filebuffer.append(line)

for line in filebuffer:
    print(line.rstrip())

# better way is to use readlines()
filebuffer = []
with open(filename) as file_object:
    filebuffer = file_object.readlines()

for line in filebuffer:
    print(line.rstrip())

# working with a files contents
# build a single string of pi removing the spaces and line feeds
pi_string = ""
for line in filebuffer:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

# files are read in as strings, if you want to convert parts of a
# file to integer use the int() function. To convert to float use
# float()

# large files with a million digits
# the same exact code with work with a million digit file
filename = "C:/Users/Robert/Python/learning/Learning-Python/CrashCourse/Crash Course Book 2 resources/chapter_10/pi_million_digits.txt"

filebuffer = []
with open(filename) as file_object:
    filebuffer = file_object.readlines()

# print the first 50 lines of the file
counter = 0
for line in filebuffer:
    counter += 1
    print(f"Line ({counter}) - {line.rstrip()}")
    # bail out after printing 50 lines
    if counter == 50:
        break

# print the first 50 digits of pi using slicing
filebuffer = []
with open(filename) as file_object:
    filebuffer = file_object.readlines()
pi_string = ""
for line in filebuffer:
    pi_string += line
print(f"{pi_string[:52]}...")
print(len(pi_string))

# does a birthdate appear anywhere in the first million digits of pi?
birthday = input("Enter your birthday in the format: mmddyy: ")
if birthday in pi_string:
    print("The birthday is there!")
else:
    print("Birthday not found. Poo.")

# writing to a file

# writing to an empty file
filename = "programming.txt"
with open(filename, "w") as file_object:
    file_object.write("I love programming.")

# can open a file in read, 'r', write, 'w', append, 'a' or
# read and write, 'r+' mode
# read is the default if not specified
# open creates the file if it does not exist
# open erases existing file of same name if opened in write mode
# Python only writes strings to files. Must convert numbers to strings

# writing multiple lines
# the write method does not add newlines to a file
# must add newlines, '\n', as needed
# writing to an empty file
filename = "programming.txt"
with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("A second line of text to add to the file.\n")

with open(filename, "a") as file_object:
    file_object.write("Appending a third line.\n")
