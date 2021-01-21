# Ex 10-5

active = True
while active:
    print("(Enter 'quit' to stop polling.)")
    reason = input("Why do you like programming? ")
    if reason == 'quit':
        active = False
    else:
        with open('programming_poll.txt', 'a') as file_object:
            file_object.write(f"- {reason}\n")
