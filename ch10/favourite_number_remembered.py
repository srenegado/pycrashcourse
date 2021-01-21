# Ex 10-12

import json

def get_stored_favourite_number():
    """Return the user's favourite number (if available)."""
    filename = 'favourite_number.json'
    try:
        with open(filename) as f:
            favourite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favourite_number
    

def get_new_favourite_number():
    """
    Record the user's favourite number to a new file 
    and return that number.
    """
    filename = 'favourite_number.json'
    favourite_number = input("What is your favourite number? ")
    with open(filename, 'w') as f:
        json.dump(favourite_number, f)
    return favourite_number


def say_favourite_number():
    """Tell the user what their favourite number is."""
    favourite_number = get_stored_favourite_number()
    if favourite_number:
        print(f"I know your favourite number! It's {favourite_number}.")
    else:
        favourite_number = get_new_favourite_number()
        print(f"I'll remember that {favourite_number} is your "
              f"favourite number the next time you ask!")

    
say_favourite_number()