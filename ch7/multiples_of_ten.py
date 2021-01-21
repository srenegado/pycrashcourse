# Ex 7-3

integer = input("Please enter an integer: ")
integer = int(integer)
if integer % 10 == 0:
    print(f"{integer} is a multiple of 10.")
else:
    print(f"10 does not divide {integer}.")