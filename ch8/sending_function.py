# For Ex 8-16

def send_messages(messages, sent_messages):
    """
    Print a series of text messages and move them from 
    messages to sent_messages.
    """
    while messages:
        sent_message = messages.pop(0)
        print(sent_message)
        sent_messages.append(sent_message) 