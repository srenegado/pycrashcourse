# Ex 10-4

while True:
    guest_name = input("Enter full name:\n(Enter 'quit' to stop) ")
    if guest_name == 'quit':
        break
    else:
        print(f"Hi, {guest_name}! Please, take a seat.")
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f"{guest_name} has arrived.\n")
    