# Ex 10-13

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def verify_username(username):
    """Return a boolean value based on if user validates the given username."""
    while True:
        yes_or_no = input(f"Are you {username}? (yes/no) ").lower()
        if yes_or_no == 'yes' or yes_or_no == 'no':
            break
    if yes_or_no == 'yes':
        return True
    elif yes_or_no == 'no':
        return False


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verification = verify_username(username)
        if verification: 
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
