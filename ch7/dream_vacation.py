# Ex 7-10

prompt = "If you could visit one place in the world, where would you go?"
poll = {}

active_polling = True
print(f"Poll: {prompt}")
while active_polling:
    name = input("Name: ").lower()
    place = input("Answer: ").lower()
    poll[name] = place
    
    repeat = input("Are you the last person to respond? (yes/no) ").lower()
    if repeat == 'yes':
        active_polling = False

print("Polling Results: ")
for name, place in poll.items():
    print(f"{name.title()} voted for {place.title()}")

