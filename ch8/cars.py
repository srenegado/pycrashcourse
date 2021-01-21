# Ex 8-14
def make_car(manufacturer, model_name, **car_info):
    """Build a dictionary containing information about a car."""
    car_info['manufacter'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

example_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(example_car)