# Ex 10-7

print("Simple Addition Calculator\n"
      "Enter 'quit' anytime to stop.")
while True:
    first_number = input("Enter a number: ")
    if first_number == 'quit':
        break
    second_number = input("Enter a number: ")
    if second_number == 'quit':
        break
    try:
        result = int(first_number) + int(second_number)
        print(f"{first_number} + {second_number} = {result}")
    except ValueError:
        print("Two numbers were not given as input.")
