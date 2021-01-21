# Ex 8-7

def make_album(artist_name, album_title, number_of_songs=0):
    """Return a dictionary containing an album's name and its artist."""
    album_info = {'artist name': artist_name, 'album title': album_title}
    if number_of_songs:
        album_info['number of songs'] = number_of_songs
        return album_info
    else:
        return album_info

print(make_album('takayan', "Let's meet in our dream"))
print(make_album('MF DOOM', "MM...FOOD"))
print(make_album('ALI', "Lost in Paradise", 1))