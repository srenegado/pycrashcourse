# Ex 6-9

favourite_places = {
    'john': ['hobby shop', 'computer store'],
    'eve': ['ski resort', 'coffee shop'],
    'june': ['cat cafe', 'bubble tea shop']
}

for name, places in favourite_places.items():
    print(f"{name.title()}'s favourite places are "
          f"the {places[0]} and the {places[1]}.")

