from tkinter import *
from COFICHEPERSO.Interface_Graphique import Interface_graphique_perso
from COFICHEPERSO import Characters
import json
from random import randint

"""   
window = Tk()
roll = [randint(3, 18) for r in range(6)]
igp = Interface_graphique_perso(window, roll)
window.mainloop()
"""

# race_choice is just preselected for working on code without load gui
race_selection = "Demi-Elfes"
profile_selection = "Magicien"

#loading Characters_race
characters_race = []
with open("json files/description.json", "r") as write_file:
   characters_race = json.load(write_file)

# race's selection
for race in characters_race:
    if race_selection == race["race_name"]:
        race_choice = race

#loading Characters_profile
characters_profile = []
with open("json files/profiles.json", "r") as write_file:
    characters_profile = json.load(write_file)

# character's selection
for profile in characters_profile:
    if profile_selection == profile["profile_name"]:
        profile_choice = profile

# player's creation

attribut = {"for": 0, "dex": 0, "con": 0, "int": 0, "cha": 0, "sag": 0}
description = {"age": randint(((race["age"])["min"]), ((race["age"])["max"])),
               "taille": randint(((race["taille"])["min"]), ((race["taille"])["max"])),
               "poids": randint(((race["poids"])["min"]), ((race["poids"])["max"])),
               "genre": "autre"}

player = Characters.Character(attribut=attribut, description=description, profile=profile)
print(race["race_name"] == race_choice)
print(player.player, player.character_name, "\n", player.description, "\n", player.attribut, "\n", player.profile)
