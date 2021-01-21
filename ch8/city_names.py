# Ex 8-6
def city_country(city_name, country_name):
    """Returns a string of form "City, Country""""
    return f"{city_name}, {country_name}".title()

print(city_country('vancouver', 'canada'))
print(city_country('paris', 'france'))
print(city_country('boston', 'usa'))

