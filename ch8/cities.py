# Ex 8-5

def describe_city(city_name, country_name='Canada'):
    """Prints a string of form "City is in Country.""""
    print(f"{city_name.title()} is in {country_name.title()}.")

describe_city('Reykjavik','Iceland')
describe_city('Toronto')
describe_city(city_name='New York', country_name='USA')
    