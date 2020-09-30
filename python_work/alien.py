alien_0 = {}
alien_0['Color'] = 'Green'
alien_0['Points'] = 5


print(alien_0)

print(f"The color of the alien_0 is {alien_0['Color']}.")

alien_0['Color'] = 'Yellow'

print(f"The modified color of the alien_0 is {alien_0['Color']}.")

alien_0 = {'X-position': 0, 'Y-position': 25, 'Speed': 'Medium'}

if alien_0['Speed'] == 'Slow':
	alien_0['X-position'] += 1

elif alien_0['Speed'] == 'Medium':
	alien_0['X-position'] += 2

else:
	alien_0[X-position] += 3

print(alien_0['X-position'], alien_0['Speed'])

favorite_lang = {'jen': 'python',
				 'sarah': 'c',
				 'edward':'ruby',
				 'phil': 'python'}

print(favorite_lang)


lang = favorite_lang['sarah'].title()

print(f"Sarah's favorite lang is {lang}.")


langu = favorite_lang.get('Richards')
langua = favorite_lang.get('Viv', 'Key not present!').title()

print(f"Sarah's fav lang is {langu}")
print(f"Sarah's fav lang is {langua}")




