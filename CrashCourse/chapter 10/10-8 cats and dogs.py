# 10-8. Cats and Dogs:
# Make two files, cats.txt and dogs.txt. Store at least three names of cats in
# the first file and three names of dogs in the second file. Write a program
# that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound
# error, and print a friendly message if a file is missing. Move one of the
# files to a different location on your system, and make sure the code in
# the except block executes properly.

# create files if the files do not exist
filenames = ["cats.txt", "dogs.txt"]

# put some anima;s in each file
catnames = ["pus", "gweniverre", "fluffy"]
dognames = ["dog", "rex", "fido"]
for filename in filenames:
    # using open for write so that existing file(s) be overwritten
    with open(filename, "w") as file_obj:
        if filename == "cats.txt":
            names = catnames
        else:
            names = dognames
        for name in names:
            file_obj.write(name + "\n")

filenames = ["cats.txt", "dogs.txt", "notthere.txt"]

# read and display the files
for filename in filenames:
    try:
        with open(filename, "r") as file_obj:
            print(f"Filename: {filename}")
            for name in file_obj:
                print(name)
    except FileNotFoundError:
        print(f"Cannot find file: {filename}")
