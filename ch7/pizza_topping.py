# Ex 7-4

prompt = "What pizza toppings would you like?\n(Enter 'quit' when you're done) "

pizza_toppings = []
active = True
while active:
    topping = input(prompt)
    if topping == 'quit': # Then the customer has ended their order.
        # So print each ordered topping.
        print("Okay, so you ordered: ")
        if pizza_toppings:
            for pizza_topping in pizza_toppings:
                print(pizza_topping)
        else:
            print("Nothing!")

        # Then confirm that the order is correct.
        confirmation = input("Is this correct? (yes/no) ")
        confirmation.lower()

        # Check if a yes/no response is given.
        if confirmation == 'yes' or confirmation == 'no':
            not_yes_or_no = False
        else:
            not_yes_or_no = True
        
        # Keep asking for a yes/no response.
        while not_yes_or_no:
            confirmation = input("Sorry, is this order correct? (yes/no) ")
            confirmation.lower()
            if confirmation == 'yes' or confirmation == 'no':
                not_yes_or_no = False

        if confirmation == 'yes': # Then we're done.
            print("Thank you for ordering!")
            active = False
        elif confirmation == 'no': # We need to take their order again.
            print("Sorry about that.")
            # So clear the previous wrong order.
            del pizza_toppings
            pizza_toppings = []
    else:
        # Add the topping to the list of ordered toppings.
        print(f"Okay, I'll add {topping.lower()}.")
        pizza_toppings.append(topping.lower())
    