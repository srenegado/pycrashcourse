# Ex 3-8
locations = ['Japan', 'South Korea', 'Singapore', 'Paris', 'Italy']
print(locations)
print(f"Temporarily sorted: {sorted(locations)}\n")
print(f"Raw list: {locations}\n")

print(f"Temporarily reverse-sorted: {sorted(locations, reverse=True)}\n")
print(f"Raw list: {locations}\n")

locations.reverse()
print(f'Permanently reversed: {locations}\n')
locations.reverse()
print(f"Permanently reversed: {locations}\n")
locations.sort()
print(f"Permanently sorted: {locations}\n")
locations.sort(reverse=True)
print(f"Reverse alphabetical order: {locations}\n")