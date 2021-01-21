# Ex 7-9

sandwich_orders = ['bahn mi', 'blt', 'pastrami', 'ham and cheese', 
                   'pastrami', 'vegetarian', 'cold cuts', 'pastrami']
finished_sandwiches = []

print("Sorry, we've run out of pastrami.")
pastrami = True
while pastrami:
    if 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    else:
        pastrami = False

active_orders = True
while active_orders:
    if sandwich_orders:
        sandwich = sandwich_orders.pop()
        print(f"I made your {sandwich} sandwich.")
        finished_sandwiches.append(sandwich)
    else:
        active_orders = False

print("Here are all the sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")
