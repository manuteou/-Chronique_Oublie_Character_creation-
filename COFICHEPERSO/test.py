from tkinter import *

class elfe():
    def __init__(self,character,attribut):
        self.character = character
        self.attribut = attribut
class grap():
    def __init__(self,main):

        self.main = main
        self.main.geometry("800x600")
        self.value = StringVar()
        self.value_catch = Entry(self.main, textvariable=self.value)
        self.value_catch.pack()
        self.Btn = Button(self.main, text="sortie", command=quit)
        self.Btn.pack()

main = Tk()
Ig = grap(main)
main.mainloop()
test = Ig.value_catch.get()
character = {"nom_Joueur": Ig.value_catch.get(), "nom_hero": "bibi"}
attribut = {"for": 15, "endu": 12}
joueur = elfe(character, attribut)

print(test)
print(joueur.character["nom_Joueur"])