# using the title method
name = "ada lovelace"
print(name.title())

# f formatting strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# newlines and tabs
newline = "\n"
tab = "\t"
print(f'{tab}"line 1"{newline}{tab}"line 2"')

# stripping whitespace
test_string = " this is a test string    with extra whitespace  "

test_string_spaces_stripped = test_string.lstrip()  # left end
print(test_string_spaces_stripped)
test_string_spaces_stripped = test_string.rstrip()  # right end
print(test_string_spaces_stripped)
test_string_spaces_stripped = test_string.strip()  # both ends
print(test_string_spaces_stripped)
print("\n")

# what removes extra spaces in the middle?
# using the re.sub() method
import re

print(test_string)
# strip extra spaces from middle of string
# ' +' is a pattern meaning any number of the space characters
# replace any number of space characters with a single space
res = re.sub(" +", " ", test_string)
# strip spaces from beginning and end of string
res = res.strip()
print(res)
print("\n")

# using split() and join()
# use split() to convert the string into a list
# use join to combine the list into a string with spaces
# this also removes extra white spaces from start, end and middle
test_string = " this is a test string    with extra whitespace  "
print(test_string)
print(test_string.split())
res = " ".join(test_string.split())
print(res)
print("\n")
