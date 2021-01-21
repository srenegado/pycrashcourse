# Ex 11-1, 11-2

"""For 11-1. City, Country, and 11-2. Population."""

def city_country(city_name, country_name, population=''):
    """Returns 'City, Country - population n' for some number n."""
    if population:
        city_and_country = f"{city_name}, {country_name}".title()
        return f"{city_and_country} - population: {population}"
    else:
        city_and_country = f"{city_name}, {country_name}".title()
        return f"{city_and_country} - population: N/A"

    