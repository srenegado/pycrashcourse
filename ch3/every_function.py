# Ex 3-10
manga = ['Jujutsu Kaisen', 'Haikyuu', 'Dr. Stone', 'Black Clover', "Komi Can't Communicate"]

print(manga[0].lower())
print(manga[1].upper())
manga.append('My Hero Academia')
print(f"Appended: {manga[5]} \nNew list:\n{manga}\n")
manga.insert(2, 'One Punch Man')
print(f"Inserted at index-2: {manga[2]}\nNew list:\n{manga}\n")
del manga[0]
print(f"Item removed, new list:\n{manga}\n")
popped_manga = manga.pop(0)
print(f"{popped_manga} removed, new list:\n{manga}\n")
removed_manga = 'Dr. Stone'
manga.remove(removed_manga)
print(f"{removed_manga} removed, new list:\n{manga}\n")


