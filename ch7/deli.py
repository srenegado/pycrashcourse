# Ex 7-8
sandwich_orders = ['bahn mi', 'blt', 'ham and cheese', 'vegetarian', 'cold cuts']
finished_sandwiches = []

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