import math             #the py3 standard math library
import Pokemon          #Pokemon.py


"""This beast.  You're gonna have to go on bulbapedia for the innerworkings of all the algorithms, but
I got it working at the very least.  Took me *way* longer than it should have, but it works.  I'm happy.
This is, I feel, where a lot of the 'advanced' Python things I learned come into play, but they're really
simple in concept, and probably could be handled a lot better."""


#The types after the colon don't really do anything, just convey to the IDE and IDLE what type to expect
#for each argument.
def calculate_stats(Pokemon: Pokemon.Pokemon, evs: dict, ivs: dict):

    #empty dict just to have something declared
    final_stats = {}

    #Pretty self explanitory.  I use evs{} as the base since if the code made it this far, it's probably
    #a fully formatted dict of every stat I will need.  Handles HP separately due to a different algorithm.
    for stat in evs:
        if stat == "hp":
            if Pokemon.name == "shedinja":
                hp = 1
            else:
                hp = math.floor((int((2 * Pokemon.hp + ivs['hp'] + int(evs['hp'] / 4)) * Pokemon.level) / 100) + Pokemon.level + 10)
            final_stats['hp'] = hp
        else:
            #temp var for.. some reason.  Too scared to take it out.  I'm tired of working on this thing.
            temp = int((int((2 * Pokemon.stats[stat] + ivs[stat] + int(evs[stat]/4)) * Pokemon.level) / 100) + 5)
            final_stats[stat] = temp
    
    #accounts for nature here.  I'm actually slightly proud of this one, even if it did give me some trouble.
    for x in Pokemon.nature:
        if Pokemon.nature[x] == "null":
            break
        if x == "increased_stat":
            final_stats[Pokemon.nature[x]] = int(final_stats[Pokemon.nature[x]] * 1.1)
        if x == "decreased_stat":
            final_stats[Pokemon.nature[x]] = int(final_stats[Pokemon.nature[x]] * 0.9)
    print(final_stats)
