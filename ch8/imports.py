# Ex 8-16

#import sending_function
#from sending_function import send_messages
#from sending_function import send_messages as sm
#import sending_function as sf
from sending_function import *
messages = ["Hey", "You coming tonight?", "At John's place?"]
sent_messages = []

print("\nCalling sent_messages:")
#sending_function.send_messages(messages, sent_messages)
#send_messages(messages, sent_messages)
#sm(messages, sent_messages)
#sf.send_messages(messages, sent_messages)
send_messages(messages, sent_messages)

print("\nContents of messages:")
print(messages)

print("\nContents of sent_messages:")
print(sent_messages)