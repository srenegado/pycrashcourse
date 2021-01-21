# Ex 6-8
pets = {
    'misto': {
        'kind': 'cat',
        'owner': 'vea' 
    },
    'temmie': {
        'kind': 'dog',
        'owner': 'lily',
    },
    'peepo': {
        'kind': 'cat',
        'owner': 'peter'
    }
}
for pet, pet_info in pets.items():
    print(f"Pet: {pet.title()}\n"
          f"Kind: {pet_info['kind'].title()}\n"
          f"Owner: {pet_info['owner'].title()}\n")