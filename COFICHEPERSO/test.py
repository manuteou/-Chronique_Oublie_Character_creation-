from tkinter import *
from COFICHEPERSO.Interface_Graphique import Interface_graphique_perso
from random import randint
import json

class Character():

    def __init__(self, character, attribut, description):
        self.character = character
        self.attribut = attribut
        self.description = description
"""        
window = Tk()
roll = [randint(3, 18) for r in range(6)]
igp = Interface_graphique_perso(window, roll)
window.mainloop()
"""
 # use for create a jion files for working with it after, will be delete a the end
"""
characters_race = {"race": "Demi-Elfes", "age": {"min":40,"max":200}, "poids":{"min":30,"max":70}}
with open("characters_race.json", "a") as write_file:
    json.dump(characters_race, write_file, separators=(",", ":"))
"""
# aim is for open json files and select the race for traitements
race_choice = "Humain"

characters_race = []
with open("characters_race.json", "r") as write_file:
   characters_race = json.load(write_file)
   for row in write_file:
       characters_race.append([row])

#for i in characters_race:
    #if race_choice in characters_race[i]:
        #print(characters_race)


"""
character = {"nom_Joueur": igp.joueur.get(), "nom_hero": ""}
attribut = {"for": 0, "dex": 0, "con": 0, "int": 0, "cha": 0, "sag": 0}
description = {"age": 0, "taille": 0, "poids": 0, "genre": "autre"}

player = Character(character, attribut, description)

print(test)
print(player.character["nom_Joueur"])
"""