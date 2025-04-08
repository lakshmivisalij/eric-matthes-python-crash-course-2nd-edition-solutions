def greet_user(username):
    """Display a simple greeting."""
    print("Hello " + username.title() + "!" )


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name+ ' ' + last_name
    return full_name.title()


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("I have a "+ animal_type + ".")
    print("My "+ animal_type + "'s name is " + pet_name.title() + ".\n")
