# Ex 3-7
guests = ['John', 'Joe', 'Jack']
print(f"{guests[0]}! DINNER NOW!")
print(f"{guests[1]}! COME HERE!")
print(f"{guests[2]}! YOU TOO!")
print(f"Wait, we got a bigger table")
guests.insert(0, 'Steve')
guests.insert(2, 'Jae')
guests.append('Joseph')
print(f"{guests[0]}! DINNER NOW!")
print(f"{guests[1]}! COME HERE!")
print(f"{guests[2]}! YOU TOO!")
print(f"{guests[3]}! DIDN'T FORGET ABOUT YOU!")
print(f"{guests[4]}! YEP!")
print(f"{guests[5]}! please? uwu")
print(f"Oh... this is awkward. We couldn't get the bigger table.")
dropped_guest1 = guests.pop(0)
print(f"Sorry, {dropped_guest1}. Gotta make room.")
dropped_guest2 = guests.pop(0)
print(f"Sorry, {dropped_guest2}. Gotta make room.")
dropped_guest3 = guests.pop(0)
print(f"Sorry, {dropped_guest3}. Gotta make room.")
dropped_guest4 = guests.pop(0)
print(f"Sorry, {dropped_guest4}. Gotta make room.")
print(f"YO, {guests[0]}! {guests[1]}! Guess what? You're still invited.")
del guests[0]
del guests[0]
print(guests)

