# Ex 5-9
#usernames = ['admin','darksider43','fluffalgee','critmaster','TacticalNash']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}! Welcome to the world of Heratross.")
else:
    print("We need to find some users!")
