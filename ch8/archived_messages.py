# Ex 8-11
def send_messages(messages, sent_messages):
    """
    Print a series of text messages and move them from 
    messages to sent_messages.
    """
    while messages:
        sent_message = messages.pop(0)
        print(sent_message)
        sent_messages.append(sent_message)

messages = ["Hey", "You coming tonight?", "At John's place?"]
sent_messages = []

print("\nCalling sent_messages with a copy of messages:")
send_messages(messages[:]), sent_messages)

print("\nContents of messages:")
print(messages)

print("\nContents of sent_messages:")
print(sent_messages)
