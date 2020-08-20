#sorting permanently using sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

#sorting temporarily using sorted() method
cars2 = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars2)

print("\nHere is the sorted list:")
print(sorted(cars2))

print("\nHere is the original list again:")
print(cars2)

print("\nHere is the sorted list in reverse order:")
print(sorted(cars2, reverse = True))

print("\nHere is the original list again:")
print(cars2)