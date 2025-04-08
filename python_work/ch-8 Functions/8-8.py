def make_album(name, title, num=''):
    album = {'artist_name': name, 'album_title': title}
    if num:
        album['num_of_tracks']= num
    return album

while True:
    print('Enter your album details here:')
    print("(Enter 'q' at any time to quit.)")

    name = input('Enter artist name: ')
    if name == 'q':
        break

    title = input('Enter album title: ')
    if name == 'q':
        break

    num = input('Enter num of tracks:')
    if num == 'q':
        break
    if num == '':
        num = ''
    album = make_album(name,title,num)
    print(album)





