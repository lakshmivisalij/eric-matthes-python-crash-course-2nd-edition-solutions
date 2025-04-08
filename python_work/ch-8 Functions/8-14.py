def make_car(name, model, **options):
    car = {}
    car['name'] = name.title()
    car['model'] = model.title()

    for key,value in options.items():
        car[key] = value

    return car

car = make_car('subaru', 'outback', color='blue'.title(), tow_package=True)
print(car)

my_old_accord = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(my_old_accord)