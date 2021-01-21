# Ex 7-4
from pizza_topping_functions import *

prompt = "What pizza toppings would you like?\n(Enter 'quit' when you're done) "
pizza_toppings = []

while True:
    topping = input(prompt)
    if topping == 'quit': # Then the customer has ended their order.
        # So print each ordered topping.
        print_order(pizza_toppings)
        # Then ask the customer if their order is correct or not
        confirmation = yes_or_no()
        
        if confirmation == 'yes':
            print("Thank you for ordering!")
            break
        else: # We need to restart their order.
            clear_order(pizza_toppings)
    else: # Add the topping to the list of ordered toppings.
        add_topping(topping, pizza_toppings)
    