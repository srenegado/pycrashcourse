# Ex 8-8

def make_album(artist_name, album_title, number_of_songs=0):
    """Returns a dictionary containing an album's title and its artist"""
    album_info = {'artist name': artist_name, 'album title': album_title}
    if number_of_songs:
        album_info['number of songs'] = number_of_songs
        return album_info
    else:
        return album_info

while True:
    print("(Enter 'q' to quit anytime)")
    artist = input("Enter an artist's name: ")
    if artist == 'q':
        break
    album = input("Enter their album name: ")
    if album == 'q':
        break
    print(make_album(artist, album))