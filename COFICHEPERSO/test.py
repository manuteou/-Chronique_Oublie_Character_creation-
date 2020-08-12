from tkinter import *
from COFICHEPERSO.Interface_Graphique import Interface_graphique_perso

class Character():
    def __init__(self,character, attribut, description):
        self.character = character
        self.attribut = attribut
        self.description = description


windows = Tk()
Interface_graphique_perso(windows)
main.mainloop()
test = Ig.value_catch.get()
character = {"nom_Joueur": Ig.value_catch.get(), "nom_hero": "bibi"}
attribut = {"for": 15, "endu": 12}
joueur = elfe(character, attribut)

print(test)
print(joueur.character["nom_Joueur"])