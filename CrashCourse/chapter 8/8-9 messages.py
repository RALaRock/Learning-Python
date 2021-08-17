# 8-9. Messages:
# Make a list containing a series of short text messages. Pass
# the list to a function called show_messages(), which prints
# each text message.


def show_messages(messages):
    for message in messages:
        print(f"{message}")


messages = [
    "message 1",
    "message 2",
    "message 3",
    "message 4",
    "message 5",
    "message 6",
    "message 7",
    "message 8",
]

show_messages(messages)
