def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('- ' + topping)

