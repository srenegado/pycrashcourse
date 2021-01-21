# For Ex 7-4

def print_order(order):
    """Prints items from an order."""
    print("Okay, so you ordered: ")
    if order:
        for item in order:
            print(item)
    else:
        print("Nothing!")


def yes_or_no():
    """Returns a yes/no response."""
    confirmation = input("Is this correct? (yes/no) ").lower()

    # Check if a yes/no response is given.
    if confirmation == 'yes' or confirmation == 'no':
        return confirmation
    else: # Keep asking for a yes/no response.
        while True:
            confirmation = input("Sorry, is this order correct? (yes/no) ").lower()
            if confirmation == 'yes' or confirmation == 'no':
                break
    return confirmation


def clear_order(pizza_toppings):
    """Clear a pizza order."""
    print("Sorry about that.")
    # So clear the previous wrong order.
    while pizza_toppings:
        del pizza_toppings[0]


def add_topping(topping, pizza_toppings):
    """Add the topping to the order."""
    print(f"Okay, I'll add {topping.lower()}.")
    pizza_toppings.append(topping.lower())