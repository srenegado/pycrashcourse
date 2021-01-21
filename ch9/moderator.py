""" A set of classes that represents a moderator."""

from user import User

class Privileges:
    """A simple class that represents a list of privileges."""
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Display the mod privileges."""
        print(f"Mod privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Moderator(User):
    """A subclass of User that models a moderator."""
    def __init__(self, first_name, last_name):
        """Initialize mod attributes."""
        super().__init__(first_name, last_name) 
        self.privileges = Privileges(['can ban users', 
            'can time-out users', 'can set chat to slow-mode'])