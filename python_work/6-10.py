fav_nums = {'visali': [18, 1, 2, 56, 7],
			'pavani': [5, 9, 11],
			'amma': [15, 2],
			'nalli': [1, 4, 22],
			'krishna': [9, 30, 31, 17, 14, 6, 12]}

for person, nums in fav_nums.items():
	print(f"{person.title()}'s favorite numbers - ", end = ' ')
	for num in nums:
		print(num, end = ' ')
	print('\n')