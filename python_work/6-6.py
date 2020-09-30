people_poll = ['sarah', 'kiran', 'edward', 'rosaline', 'phil', 'pirrip', 'mark']

favorite_languages = {'jen':'python', 'sarah':'c', 'edward': 'ruby', 'phil': 'python'}

for person in people_poll:
	if person in favorite_languages.keys():
		print(person.title() +", Thanks for taking the poll!")

	else:
		print(f"{person.title()}, Please take the poll!")
