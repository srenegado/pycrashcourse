# Ex 6-5
rivers = {'nile': 'egypt', 'st. lawrence': 'canada', 'yellow': 'china'}

for river, country in rivers.items():
    print(f"The {river.title()} River runs through {country.title()}.")

print("Rivers:")
for river in rivers:
    print(f"\t{river.title()}")

print("Countries:")
for country in rivers.values():
    print(f"\t{country.title()}")