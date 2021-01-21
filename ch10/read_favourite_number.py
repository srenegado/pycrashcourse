# Ex 10-11

import json

filename = 'favourite_number.json'
with open(filename) as f:
    favourite_number = json.load(f)
    print(f"I know your favourite number! It's {favourite_number}.")