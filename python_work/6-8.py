
pets = []

nalli = {'animal': 'dog', 'name': 'nalli', 'owner': 'amma' }
pets.append(nalli)
krishna = {'animal': 'dog', 'name' :'krishna', 'owner':'visali'}
pets.append(krishna)

for pet in pets:
	print('\n Animal is a ' + pet['animal'].title()+'. Name is '+pet['name']+'. Owner is '+ pet['owner'].title()+'.')
