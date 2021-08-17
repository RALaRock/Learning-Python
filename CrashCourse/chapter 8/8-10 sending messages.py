# 8-10. Sending Messages:
# Start with a copy of your program from Exercise 8-9. Write a function
# called send_messages() that prints each text message and moves each
# message to a new list called sent_messages as it’s printed. After calling
# the function, print both of your lists to make sure the messages were
# moved correctly.


def send_messages(messages, sent_messages):
    """send (print) each message in list
    move printed messages to sent list
    """
    while messages:
        current = messages.pop()  # this will reverse the order
        print(f"{current}")  # simulate sending message
        sent_messages.append(current)


def show_messages(messages):
    if messages:
        for message in messages:
            print(f"{message}")
    else:
        messages.append("empty list")
    print()


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
sent_messages = []

send_messages(messages, sent_messages)
print(messages)
print(sent_messages)
