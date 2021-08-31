# 10-9. Silent Cats and Dogs: 
# Modify your except block in Exercise 10-8 to fail silently if either file is 
# missing.

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
        pass
