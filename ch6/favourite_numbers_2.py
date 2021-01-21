# Ex 6-10
favourite_numbers = {
    'Nanami': [3,7],
    'Senku': [10000000000],
    'John': [12, 436, 432],
    'Jack': [65, 343, 3424, 2434, 2],
    'Joe': [13,2,3]
}

for name, numbers in favourite_numbers.items():
    print(f"{name.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")