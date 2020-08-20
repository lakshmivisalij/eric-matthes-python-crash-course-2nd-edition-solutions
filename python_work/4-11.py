my_pizzas = ['margherita', 'cheese', 'corn']
friend_pizzas = my_pizzas[:]

my_pizzas.append('onion')
friend_pizzas.append('double cheese')

print("My favorite pizzas are:")

for my_pizza in my_pizzas:
	print(my_pizza)

print("\nMy friend's favorite pizzas are:")

for friend_pizza in friend_pizzas:
	print(friend_pizza)