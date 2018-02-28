# Stat-Calculator
A python Pokemon stat calculator using pokeapi.  It’s fairly simple, though something tells me I should get used to writing documentation for the stuff I make, so here we go.  Data is gathered from https://pokeapi.co/

##Arguments
* `-n`, `--nature [nature]` - Sets the nature of the Pokemon you want
* `-ev`, `--EVs [HP, Atk, Def, SpA, SpD, Spe]` - Sets the EVs of the Pokemon.
* `-iv`, `--IVs [HP, Atk, Def, SpA, SpD, Spe]` - Sets the IVs of the Pokemon.
* `-l`, `--level [level]` - Sets the level of the pokemon

The `[name]` argument is positional, and must be called without a flag.  If the script is called with no arguments, it will walk you through the process manually, asking for each aspect one at a time.  Checking each argument might come in a later version, I’m unsure.
