def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("I have a "+ animal_type + ".")
    print("My "+ animal_type + "'s name is " + pet_name.title() + ".\n")

describe_pet('hamster', 'harry')
describe_pet("dog", 'willie')
describe_pet('harry', 'hamster')

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet( pet_name='harry',animal_type='hamster',)