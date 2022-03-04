def make_album(artist_name, album_title, number_of_songs=None):
    '''Returns a dictionary of information on an album'''
    album = {'artist': artist_name, 'title': album_title}
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

while True:
    print("\nPlease input album's artist and title:")
    print("(enter 'q' to exit at any time)")

    name = input("Enter the artist's name: ")
    if name == 'q':
        break

    album_title = input("Enter the album title")
    if album_title == 'q':
        break

    album_information = make_album(name, album_title)
    print(album_information)

