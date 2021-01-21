# Ex 6-11
cities = {
    'vancouver': {
        'country': 'canada',
        'population': 675218,
        'fact': 'Expensive housing'
    },
    'burnaby': {
        'country': 'canada',
        'population': 249197,
        'fact': 'The city next to Vancouver'
    },
    'surrey': {
        'country': 'canada',
        'population': 518467,
        'fact': 'People get mugged here' 
    }
}

for city, city_info in cities.items():
    print(f"City: {city.title()}\n"
          f"\tCountry: {city_info['country'].title()}\n"
          f"\tPopulation: {city_info['population']}\n"
          f"\tFact: {city_info['fact']}")

