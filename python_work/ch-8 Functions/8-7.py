def make_album(name, title, num=''):
    album = {'artist_name': name, 'album_title': title}
    if num:
        album['num_of_tracks']= num
    return album

album1 = make_album('Jimi hendrix', 'In the moonlight')
print(album1)

album2 = make_album('Jimi Hendrix', 'Love in the air')
print(album2)

album3 = make_album('Enrique', "Somebody's me", 3)
print(album3)