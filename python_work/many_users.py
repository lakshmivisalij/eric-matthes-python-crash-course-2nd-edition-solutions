users = {'aeinstein': 
                     {'fname' : 'albert', 'lname': 'einstein', 'location':'princeton'},
          'mcurie':
                     {'fname': 'madam', 'lname': 'curie', 'location':'paris'}, 

                     }

for username, user_info in users.items():
	print(f"\nUsername: {username.title()}")
	fullname = f"{user_info['fname']} {user_info['lname']}"
	location = user_info['location']

	print(f"User-info: {fullname.title()} \t {location.title()}")


