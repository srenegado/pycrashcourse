# Ex 5-11
one_to_nine = [num for num in range(1,10)]

for num in one_to_nine:
    if num == 1:
        print("1rst")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")