# 7-9. No Pastrami:
# Using the list sandwich_orders from Exercise 7-8, make sure the
# sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli
# has run out of pastrami, and then use a while loop to remove all
# occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami
# sandwiches end up in finished_sandwiches.

# 7-8
# make a list of sandwich_orders
# fill it with various sandwiches
# make an empty list of finished_sandwiches
# print a message about making each sandwich
# move the ordered sandwiches to to the finished list
# print a message listing each finished sandwich

sandwich_orders = [
    "pastrami",
    "pastrami",
    "tuna",
    "italian sausage",
    "pastrami",
    "pb&j",
    "pastrami",
]
finished_orders = []
print("The deli has run out of pastrami.")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich != "pastrami":
        print(f"We are making your {current_sandwich} sandwich right now.")
        finished_orders.append(current_sandwich)
print("We made the entire order.")
for current_sandwich in finished_orders:
    print(f"\t{current_sandwich}")
