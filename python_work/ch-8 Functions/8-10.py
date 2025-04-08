def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    for i in range(len(magicians)):
        magicians[i] += ' the Great'



magicians = ['Harry', 'Katrina', 'Sanjay', 'Visali']
show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)