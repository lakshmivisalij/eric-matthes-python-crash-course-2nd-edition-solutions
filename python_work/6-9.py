fav_places = {'paul': ['NewYork', 'Rajahmundry', 'Bangalore'],
              'visali': ['Bangalore'],
              'antony': ['Berlin', 'Paris']}

for name, places in fav_places.items():
	print('\nName is ' + name.title(), end =' and favorite places are ')
	for place in places:
		print(place, end = ' ')