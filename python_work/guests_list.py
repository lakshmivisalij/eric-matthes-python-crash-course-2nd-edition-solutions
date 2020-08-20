#3-4
guests = ['subba rao sir', 'perumal sir', 'satyanarayana sir']
print(f"Dear {guests[0].title()}, You are invited for Dinner.")
print(f"Dear {guests[1].title()}, You are invited for Dinner.")
print(f"Dear {guests[2].title()}, You are invited for Dinner.")

#3-5
print(f"{guests[1].title()} won't be able to make it to Dinner.")

guests[1] = 'sri hari sir'
print(f"Dear {guests[0].title()}, You are invited for Dinner.")
print(f"Dear {guests[1].title()}, You are invited for Dinner.")
print(f"Dear {guests[2].title()}, You are invited for Dinner.")

#3-6
print("Found a bigger dining table!")

guests.insert(0,'sandeep')
guests.insert(2, 'maddy')
guests.append('rama')

print(f"Dear {guests[0].title()}, You are invited for Dinner.")
print(f"Dear {guests[1].title()}, You are invited for Dinner.")
print(f"Dear {guests[2].title()}, You are invited for Dinner.")
print(f"Dear {guests[3].title()}, You are invited for Dinner.")
print(f"Dear {guests[4].title()}, You are invited for Dinner.")
print(f"Dear {guests[5].title()}, You are invited for Dinner.")

#3-7

print("Only two seats available for Dinner!")

guest_removed = guests.pop()
print(f"Sorry {guest_removed.title()} that you cannot be invited!")

guest_removed = guests.pop()
print(f"Sorry {guest_removed.title()} that you cannot be invited!")

guest_removed = guests.pop()
print(f"Sorry {guest_removed.title()} that you cannot be invited!")

guest_removed = guests.pop()
print(f"Sorry {guest_removed.title()} that you cannot be invited!")

print(f"Dear {guests[0].title()}, You are invited for Dinner")
print(f"Dear {guests[1].title()}, You are invited for Dinner")

del guests[0]
del guests[0]

print(guests)









