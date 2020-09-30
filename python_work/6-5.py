rivers = {'nile': 'egypt', 'godavari': 'india', 'ganga':'india', 'mississippi': 'united states'}

for river in rivers:
	print(f"The {river.title()} runs through {rivers[river].title()}.")

for river in rivers:
	print(f"{river.title()}", end=" ")

for country in rivers.values():
	print(country.title(), end = " ")

