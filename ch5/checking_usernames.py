# Ex 5-10
current_users = ['Takuraisan','darksider43','fluffalgee','critmaster','TacticalNash']
new_users = ['FluFFalgEe','TACTICALNASH','SquishFish','tyrantbard','fellabella']

# Create a copy of current_users wherein each username is lowercased.
# This is to make username checking case insensitive.
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print("Username has been taken. Please enter a new username.")
    else:
        print("Username is available.")
