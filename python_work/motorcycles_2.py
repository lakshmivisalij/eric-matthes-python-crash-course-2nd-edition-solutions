motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

last_owned = motorcycles.pop()
print(f'The last motorcycle I owned was a {last_owned.title()}.')

first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

print(motorcycles)
print(motorcycles[0].title())
