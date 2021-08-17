# 8-11. Archived Messages:
# Start with your work from Exercise 8-10. Call the function send_messages()
# with a copy of the list of messages. After calling the function, print both of
# your lists to show that the original list has retained its messages.


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

# passing a copy of messages
send_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)