"""As expected, imports at the top.  I'll be explaining what the are next to them."""
from sys import argv            #Commandline arguments.  Only needed for the initial check.
from pprint import pprint       #"Pretty" print.  It formats lists and dicts and such to be much easier to read in the console

import argparse                 #handles commandline flags and arguments
import Pokemon                  #Pokemon.py, just the class file
import maths                    #maths.py, the calculate_stats function

"""Originally I had thought I would need *a lot* more in that class and maths.py, but I ended up shortening it
to one line.  The fact they aren't part of the main file is just a remnant of that."""

#Checks to see if there are any commandline args.  Since the file is always argv[0], if just the file is called,
#the length is one
if len(argv) == 1:

    #this looks messy, but is simple in concept.  Takes inputs, sets them to lowercase or integers if needed
    name = input('Enter Pokémon\'s name: ').lower()
    nature = input('Enter Pokémon\'s nature: ').lower()
    level = int(input('Enter Pokémon\'s level: '))
    print('Enter the following stats in the order of: HP, Attack, Defense, Special Attack, Special Defense, and Speed')

    '''These next lines are a bit tricky. It creates an unnamed list and calls the map function.
    What that does is iterates through the list in the second arg, casting all the elements to the type
    of the first argument.  The .split() is to actually make it a list, as the input itself is a string
    of space separated characters, as long as the user can follow directions.'''

    list_evs = list(map(int, input('Enter the Pokémon\'s EVs (space separated.): ').split()))
    list_ivs = list(map(int, input('Enter the Pokémon\'s IVs (space separated.): ').split()))

    #Here I just turn the list into a correctly formatted dicttionary
    evs = {"hp":list_evs[0], "attack":list_evs[1], "defense":list_evs[2], "special-attack":list_evs[3], "special-defense":list_evs[4], "speed":list_evs[5]}
    ivs = {"hp":list_ivs[0], "attack":list_ivs[1], "defense":list_ivs[2], "special-attack":list_ivs[3], "special-defense":list_ivs[4], "speed":list_ivs[5]}

    #Usermon is whatever Pokemon they enter.
    Usermon = Pokemon.Pokemon(name, nature, level)

    #I explain this function in maths.py
    maths.calculate_stats(Usermon, evs, ivs)
else:
    """I won't lie, this was my first time handling commandline args, so a lot of this was new to me too.
    Basically, I created an ArgumentParser object named parser, and just called add_arguments for whatever
    I needed.  'name' is a positional argument, so it doesn't need a flag but is required.  
    
    'metavar' is what comes up upon an error regarding commandline args or if the user calls -h/--help.
    
    'type' is the type to cast to, obviously.
    
    'nargs' = number of args that flag needs afterwards"""

    parser = argparse.ArgumentParser(description="Handle Pokemon from commandline")
    parser.add_argument('name', metavar="[name]", type=str)
    parser.add_argument('-ev', '--EVs', metavar='EV', type=int, nargs=6)
    parser.add_argument('-iv', '--IVs', metavar='IV', type=int, nargs=6)
    parser.add_argument('-n', '--nature', metavar='nature', type=str, nargs=1)
    parser.add_argument('-l', '--level', metavar='level', type=int, nargs=1)

    #parses all of the arguments into  a list of their respective types and stores them in args
    args = parser.parse_args()
    
    """The Usermon object.  This had some pitfalls I needed to workaround, as shown.
    Firstly, I needed to cast 'name' to a string in order to use .lower() on it, as a case check.
    For some reason, no matter what I did, nature failed unless I formed a new string with it on the fly,
    so I used a blank string and joined nature to it.
    Since level was a list, I had to  call the first element."""
    Usermon = Pokemon.Pokemon(str(args.name).lower(), ''.join(args.nature), args.level[0])

    #More dict-making, whoo! ^-^
    evs = {"hp":args.EVs[0], "attack":args.EVs[1], "defense":args.EVs[2], "special-attack":args.EVs[3], "special-defense":args.EVs[4], "speed":args.EVs[5]}
    ivs = {"hp":args.IVs[0], "attack":args.IVs[1], "defense":args.IVs[2], "special-attack":args.IVs[3], "special-defense":args.IVs[4], "speed":args.IVs[5]}

    #again, explained in maths.py
    maths.calculate_stats(Usermon, evs, ivs)

