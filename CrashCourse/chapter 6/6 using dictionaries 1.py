# dictionary is a composite data type like a list
# both are mutable, items can be changed
# both are dynamic, can change size
# both can be nested, both can contain other lists or dictionaries
# lists and dictionary differ
# list elements are accessed by their index in the list
# dictionary elements are accessed by their keys
# a dictionary is also called an associative array
# it is a collection of key-value pairs

# defining a dictionary, enclose comma separated list in curly braces
# a semi colon separates each key value pair
# d = {
#     key: value,
#     key: value,
#     key: value, # include the trailing comma to maintain this format
# }

# baseball team locations and names
mlb_teams = {
    "Colorado": "Rockies",
    "Bostom": "Red Sox",
    "Minnesota": "Twins",
    "Los Angeles": "Dodgers",
}
print(type(mlb_teams))
print(mlb_teams)


# adding new key-value pairs
alien_0 = {"color": "green", "points": 5}
print(alien_0)
print("alient points: " + str(alien_0["points"]))
# adds two key value pairs to dictionary
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# starting with and empty dictionary
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# modify a key value pair
alien_0["points"] = 12
print(alien_0["points"])

alien_0["speed"] = "medium"
print(alien_0["speed"])

# removing a key value pair using del
# permanently removes the pair
del alien_0["points"]
print(alien_0)

# using multiple lines to define a dictionary
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print(favorite_languages)
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")

# using get() to access values
# getting values using [] has a problem if the key does not exist
# print(favorite_languages['noexistentkey'])
# using get( keynane to get, what to return if key doesn't exist)
# provides a means to handle a non existent key
print(alien_0.get("speed", "key does not exist"))  # key exists
print(alien_0.get("points", "key does not exist"))  # key missing
# if second argument in get() left off returns non if key not found
print(alien_0.get("points"))  # key missing


# using the dict() function
# d = dict([
#     (key, value),
#     (key, value),
#    (key, value),
# ])
mlb_teams = dict(
    [
        ("Colorado", "Rockies"),
        ("Bostom", "Red Sox"),
        ("Minnesota", "Twins"),
        ("Los Angeles", "Dodgers"),
    ]
)
print(mlb_teams)

# if key values are simple strings can define it like this
mlb_teams = dict(
    Colorado="Rockies",
    Bostom="Red Sox",
    Minnesota="Twins",
    LosAngeles="Dodgers",  # this would not work if space in Los Angeles
)
print(mlb_teams)

# but don't really need the dict() methond, can do this instead
mlb_teams = {
    "Colorado": "Rockies",
    "Bostom": "Red Sox",
    "Minnesota": "Twins",
    "Los Angeles": "Dodgers",
}
print(mlb_teams)

# dictionary elements are NOT accessed by numerical index
# they are accessed by key value by specifying they key in square brackets
print(mlb_teams["Los Angeles"])

# to add an entry to a dictionary specify a new key value pair
mlb_teams["Kansas City"] = "Royals"
print(mlb_teams)

# to change a value
mlb_teams["Kansas City"] = "Chiefs"
print(mlb_teams)

# to delete an entry
del mlb_teams["Kansas City"]
print(mlb_teams)

# errors if cannpt find the key
# print(mlb_teams[1]) # this raises a can't find key error
# print(mlb_teams['Georgia']) # this raises the same error

# keys can be integers or any other immutable data type
# keys and values do not need to be the same data type
d = {0: "a", 1: "b", 2: "c", "one": 1, "two": 2}
print(d["one"])

# but don't really need the dict() methond, can do this instead
mlb_teams = {
    "Colorado": "Rockies",
    "Bostom": "Red Sox",
    "Minnesota": "Twins",
    "Los Angeles": "Dodgers",
    "Los Angeles": "Dodgers dodgers",  # this duplicate reassigns the value
}

for keyname in mlb_teams:
    print(mlb_teams[keyname])

# looping through dictionaries
# can loop through key value pairs, keys or values

# looping through all key-value pairs
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

# looping through all the key-value pairs
# using for key, value in dictionay.items():
print()
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
print(user_0.items())

# this does the same thing
print()
for key in user_0:
    print(f"\nKey: {key}")
    value = user_0[key]
    print(f"Value: {value}")
print(user_0.items())

# using keys() method to work just the keys
print()
for name in favorite_languages.keys():
    print(name.title())

# since keys is the default behavior for looping so this
# works the same way
print()
for name in favorite_languages:
    print(name.title())

# use keys() to determine if a key is in a dictionary
print()
if "erin" not in favorite_languages.keys():
    print("Erin is not in the dictionary.")
# keys() returns a list of all the keys
print(favorite_languages.keys())

# looping through keys in a particular order
# from python 3.7 the order is returned in the order added
# this is methods to change the order
print()
# sorted
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# looping through values in a dictionary using the values() method
print()
print("The followin glanguages have been mentioned:")
for value in favorite_languages.values():
    print(value.title())
# this returns all values including repeats
# to get rid of repeats use a set which is a list without repeats
print()
for value in set(favorite_languages.values()):
    print(value)

# sets are like a list of dictionary keys in that they don't allow duplicates
# except sets don't have key value pairs
# sets look similar to dictionaries, they use curly braces
print()
fruits = {"banana", "apple", "banana", "orange", "apple"}
print(fruits)  # duplicates removed

# nesting
# storing a list of values in a dictionary or
# storing a dictionary in a list
# storing lists in lists or dictionaries in dictionaries
print()


exit()
