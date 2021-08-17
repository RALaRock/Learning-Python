# dictionary is a composite data type like a list
# both are mutable, items can be changed
# both are dynamic, can change size
# both can be nested, both can contain other lists or dictionaries
# lists and dictionary differ
# list elements are accessed by their index in the list
# dictionary elements are accessed by their keys
# a dictionary is also called an associative array
# it is a collection of key-value pairs
# dictionary keys must be unique with no repeats

# defining a dictionary, enclose comma separated list in curly braces
# a semi colon separates each key value pair
# d = {
#     key: value,
#     key: value,
#     key: value, # include the trailing comma to maintain this format
# }

# adding new key-value pairs
alien_0 = {"color": "green", "points": 5}

# nesting
# storing a list of values in a dictionary or
# storing a dictionary in a list
# storing lists in lists or dictionaries in dictionaries
print()

# manuly creating aliens
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "red", "points": 15}
alien_2 = {"color": "yellow", "points": 25}
alien_3 = {"color": "black", "points": 35}

# dictionaries in a list
# useful when list items need to store multiple items with key values

# create a bunch of aliens
# initialize list
aliens = []
print(type(aliens))
# populate list with dictionary items
points = 0
for alien_number in range(30):
    points = points + 1
    new_alien = {"color": "green", "points": points, "speed": "slow"}
    aliens.append(new_alien)
# print the firts five items in the list using a list slice
for alien in aliens[:5]:
    print(alien)

# change the color of one alien for testing
print()
aliens[2]["color"] = "red"
print(aliens[2])

# set the first three aliens to yellow color, medium speed
print()
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
for alien in aliens[:5]:
    print(alien)

print()
print(f"The total number of aliens is {len(aliens)}.")

# lists in a dictionary

# useful when one or more of the elements of the dictionary need to store
# multiple items
print()
# pizza is a dictionary in which the second element is a list of toppings
pizza = {"crust": "thin", "toppings": ["mushrooms", "pepperoni", "extra cheese"]}
print(f"You ordered a {pizza['crust'].upper()} crust with the " "following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

# dictionary within a dictionary
# useful when
print()

# users dictionary with username as the key and a dictionary of user
# attributes as the value
# note the structure of the values dictionary remains consistent
# this is not required by python, but using different key names
# for each user would make this difficult to work with
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
# print out the dictionary of users
for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    fullname = f"{userinfo['first']} {userinfo['last']}"
    location = f"{userinfo['location']}"
    print(f"\tFullname: {fullname}")
    print(f"\tLocation: {location}")
print()

