# Ex 9-5

from user import User

user = User('Scott', 'Renegado')
for nth_attempt in range(10):
    user.increment_login_attempts()
    
print(f"Number of login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Resetting login attempts...\n"
      f"Number of login attempts: {user.login_attempts}")

