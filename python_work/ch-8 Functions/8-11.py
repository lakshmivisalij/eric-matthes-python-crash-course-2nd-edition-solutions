def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Add 'the Great!' to each magician's name."""
    greatmagicians=[]
    for i in range(len(magicians)):
        greatmagicians.append( magicians[i] +' the Great')
    return greatmagicians



magicians = ['Harry', 'Katrina', 'Sanjay', 'Visali']
show_magicians(magicians)

"""Calling the function make_great() with a copy of the list of magicians’ names."""
greatmagicians = make_great(magicians[:])
show_magicians(greatmagicians)
show_magicians(magicians)
