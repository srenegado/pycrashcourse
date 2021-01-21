"""A simple class that models a restaurant."""

class Restaurant:
    """A simple class that models a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print the restaurant's information."""
        print(f"Restaurant name: {self.restaurant_name}\n"
              f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print that the restaurant is open."""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

