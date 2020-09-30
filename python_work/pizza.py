pizza = {'crust':'thick', 'toppings': ['onion', 'extra cheese']}

#summarize the order
print(f"You ordered a pizza with {pizza['crust'].title()} crust and with the toppings of - ")
for topping in pizza['toppings']:
	print('\t'+topping.title())


fav_langs = {'jen':['c', 'ruby'],
'phil': ['scala', 'c#', 'c'],
'edward': ['c', 'python'], 
'sarah':['c'],}

for name,langs in fav_langs.items():
	print(f"{name.title()}'s favorite languages are: ")
	for lang in langs:
		print(f"\t{lang.title()}")
	

