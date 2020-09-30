cities = {'Bangalore' :
           {'country': 'india', 'population' : '3 million', 'fact':'garden city'},
          'Jaipur':
           {'country': 'india', 'population': '1 million', 'fact':'pink city'},
           'Delhi':
           {'country': 'india', 'population': '4 million', 'fact':'most polluted city in india'}, }

for city, abouts in cities.items():

	print(f"The city {city.title()} is in ", end ='')

	country = abouts['country']
	pop = abouts['population']
	fact = abouts['fact']

	print(country.title() + '. It has a population of about '+abouts['population']+ '. One fact about this city is that it is called '+abouts['fact'].title()+'.\n')



