#More imports! ^-^

import requests #A very simple http request library.  Built in to py3
import json # Needed to handle .json data, obviously.
import sys #System calls.  I use it for sys.exit() incase the user has a typo.
from pprint import pprint #Pretty print again.  I just luvs it.

class Pokemon():
    """So... this class.  I'll get into the complicated stuff after, but I handle basically everything needed
    in the constructor.  Hence why __init__ is the only function here."""

    #class variables.
    pokemon_base_url = "http://pokeapi.co/api/v2/pokemon/"
    nature_base_url = "http://pokeapi.co/api/v2/nature/"
    stats = {}
    name = ""
    nature = {}
    hp = int        #Just a tip since I dunno how you do this in Lua, but this is how you give a variable
    level = int     #a type but no value.

    #constructor method.  Any additional args here besides 'self' are required to make an object of this type
    def __init__(self, name, nature, level):
        self.level = level

        #an example of the requests library.  I love how clean it is.  Request to dict in one line. ^^
        r = requests.get(self.pokemon_base_url + name).json()

        #handles a 404 since pokeapi is weird with it.
        if r == {"detail":"Not found."}:
            print("Invalid Name.  Exiting...")
            sys.exit()
        else:
            #self.<varname> lets you access class vars from within the class itself
            self.name = name
            
            """This part is pretty simple.  I create a temp_dict to hold the stats list,
            then assign all that into the self.stats{} and self.hp variables."""
            temp_dict = r['stats']
            for x in temp_dict:
                if x['stat']['name'] == 'hp':
                    self.hp = x['base_stat']
                else:
                    self.stats[x['stat']['name']] = x['base_stat']

        #Again, one line.  I love this. ^^
        r = requests.get(self.nature_base_url + nature).json()
        if r == {"detail":"Not found."}:
            print("Invalid nature.  Exiting...")
            sys.exit()
        else:
            #You saw some of this.  But this is how I parse a neutral nature from one that has stat changes.
            #Works well, for what I need it to do. ^^
            try:
                self.nature['increased_stat'] = r['increased_stat']['name']
                self.nature['decreased_stat'] = r['decreased_stat']['name']
            except TypeError:
                self.nature['increased_stat'] = 'null'
                self.nature['decreased_stat'] = 'null'