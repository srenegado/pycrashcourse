"""A class that represents a user."""

class User:
    """A simple class modelling a user's profile and analytics."""

    def __init__(self, first_name, last_name):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name= last_name
        self.login_attempts = 0

    def describe_user(self):
        """Print out the user's first and last name."""
        print(f"First name: {self.first_name}\n"
              f"Last name: {self.last_name}")

    def greet_user(self):
        """Print the user a greeting message."""
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increment login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Set login attempts equal to 0."""
        self.login_attempts = 0