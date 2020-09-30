favorite_languages = {'jen':'python', 'sarah':'c', 'edward': 'ruby', 'phil': 'python'}

for name, lang in favorite_languages.items():
	print('\nKeys: '+ name.title())
	print('Values: '+ lang.title())

for name in favorite_languages.keys():
	print('\nKeys: ' + name.title())

for name in favorite_languages:
	print('\n'+name.title(), end=' ')


friends = ['phil', 'sarah']

for name in favorite_languages:
	print("\n" +name.title())
	if name in friends:
		lang = favorite_languages[name].title()
		print(f"{name.title()}'s favorite language is {lang}.")


for name in sorted(favorite_languages):
	print(f"{name.title()}'s fav lang is {favorite_languages[name].title()}.")


print("The list of favorite languages is: ")
for lang in favorite_languages.values():
	print(lang.title(), end = " ")

print("\nUsing set():")

for lang in set(favorite_languages.values()):
	print(lang.title(), end = " ")


set1 = {'python', 'c', 'c++', 'c', 'ruby', 'python'}
print(f"\n{set1}")

