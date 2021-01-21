# Ex 9-7
# In this exercise, show_privileges is a method of Moderator.

from user import User

class Moderator(User):
    """A subclass of User that models a moderator."""
    def __init__(self, first_name, last_name):
        """Initialize mod attributes."""
        super().__init__(first_name, last_name)
        self.privileges = [ 'can ban users', 'can time-out users', 
            'can set chat to slow-mode']

    def show_privileges(self):
        """Display the mod privileges"""
        print(f"Mod privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

mod = Moderator('John', 'Doe')
mod.show_privileges()

    