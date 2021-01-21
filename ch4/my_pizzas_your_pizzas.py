# 4-11

pizzas = ['Cheese', 'Pepperoni', 'Hawaiian']
friend_pizzas = pizzas[:]
pizzas.append('Sardines')
friend_pizzas.append('Vegetarian')

print(f"My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print(f"My friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

