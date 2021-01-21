# Ex 10-11

import json

filename = 'favourite_number.json'
favourite_number = input("What is your favourite number? ")
with open(filename, 'w') as f:
    json.dump(favourite_number, f)
