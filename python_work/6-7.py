people =  []

person = {'first name': 'Adilaks', 'last name': 'Jayanthi', 'age' : 28, 'city':'Bangalore',}
people.append(person)


person = {'first name': 'Visali', 'last name': 'Jayanthi', 'age' : 14, 'city':'Trivandrum'}
people.append(person)
       
person = {'first name': 'Akash', 'last name': 'Jha', 'age' : 10, 'city':'Delhi'}
people.append(person)

for person in people:
	fullname = f"{person['first name']} {person['last name']}"
	age = person['age']
	city = person['city']

	print(fullname.title() + ' is of age '+ str(age) + ', and from city, '+ city+'.')


