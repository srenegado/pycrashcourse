# Ex 10-6

first_number = input("Enter a number: ")
second_number = input("Enter a number: ")
try:
    result = int(first_number) + int(second_number)
    print(f"{first_number} + {second_number} = {result}")
except ValueError:
    print("Two numbers were not given as input.")
