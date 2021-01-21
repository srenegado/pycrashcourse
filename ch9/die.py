"""A class that represents a die."""

from random import randint

class Die:
    """A simple class modelling a die."""
    def __init__(self, sides=6):
        """Die attributes."""
        self.sides = sides

    def roll_die(self):
        """Print a random number in [1,sides]."""
        print(f"{randint(1,self.sides)}")
