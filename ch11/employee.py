# Ex 11-3

class Employee:
    """A simple class modelling an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize employee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Add on to the employee's annual salary."""
        self.annual_salary += raise_amount