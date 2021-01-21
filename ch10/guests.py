# Ex 10-3

guest_name = input("Enter full name: ")
with open('guest.txt', 'w') as file_object:
    file_object.write(guest_name)
