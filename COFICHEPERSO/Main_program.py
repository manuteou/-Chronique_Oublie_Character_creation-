from tkinter import *
from COFICHEPERSO.GUI import GUI,GUI_Intro
from COFICHEPERSO.Character_Class import Character
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
with open("json files/races_list.json", "r") as write_file:
   characters_race = json.load(write_file)

# race's selection
for race in characters_race:
    if race_selection == race["race_name"]:
        race_choice = race

#loading Characters_profile
characters_profile = []
with open("json files/profiles_list.json", "r") as write_file:
    characters_profile = json.load(write_file)

# character's selection
for profile in characters_profile:
    if profile_selection == profile["profile_name"]:
        profile_choice = profile

# player's creation
player = Character()
player.age = randint(race_choice["age"]["min"], race_choice["age"]["max"])
player.poids = randint(race_choice["taille"]["min"], race_choice["taille"]["max"])
player.taille = randint(race_choice["taille"]["min"], race_choice["taille"]["max"])

print(player.age)


