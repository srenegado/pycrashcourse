"""A class that represents an ice cream stand."""
from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """A subclass that models an ice cream stand."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def display_flavours(self):
        """Display available flavours."""
        print(f"Available flavours: {self.flavours}")

    def add_flavours(self, *flavours):
        """Add an arbitrary amount of flavour to the list of flavours."""
        for flavour in flavours:
            self.flavours.append(flavour.lower())
    

