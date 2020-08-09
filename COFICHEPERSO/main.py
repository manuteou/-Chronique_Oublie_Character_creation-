# Programme principal
from COFICHEPERSO import Personnages
from COFICHEPERSO import Caracteristiques_Old
from COFICHEPERSO import Interface_Graphique
from tkinter import *
import random

# lancement de la fenetre graphique d'introduction

def fenetre(image):

    canvas = Canvas(main,heigh=400,width=800)
    canvas.create_image(400,300, image=image)
    canvas.create_text(400,70, text="CHRONIQUES OUBLIEES\n Generateur de Personnage",font=("Helvetica",40))
    canvas.pack(expand=YES)


main = Tk()
image = PhotoImage(file="Persos.png").subsample(2)
main.geometry("800x600")
main.title("Création de Personnage CO")
fenetre(image)
Btn = Button(main, text="Suite", width=5, height=2, command=main.destroy)
Btn.pack()
main.mainloop()

# lancement de la  fenetre graphique du personnage

ig_perso = Tk()
ig_perso.title("Création de Personnage CO")
ig_perso.minsize(700,360)
interface = Interface_Graphique.Interface_graphique_perso(ig_perso)
ig_perso.mainloop()

# on recupere les champs dans des variables
nom_joueur = interface.joueur.get()
nom_personnage = interface.nom_perso.get()
genre = interface.genre_choix.get()
race_choix = interface.race_choix.get()

# on detruit la fenetre
ig_perso.destroy()

# On ouvre la fenetre pour les attributs
ig_att = Tk()
ig_att.title("Création du Personnage CO")
ig_att.minsize(700,360)
interface = Interface_Graphique.Interface_Graphique_attribut(ig_att)
ig_att.mainloop()
force =  interface.force.get()
dexterité = interface.dexterité.get()
constitution = interface.constitution.get()
inteligence = interface.inteligence.get()
charisme = interface.charisme.get()
sagesse = interface.sagesse.get()

# On detruit la fentre
ig_att.destroy()

# Attribution des valeurs dans le personnage

#Boucles qui definissent les bonus d'attributs, la taille, le poids et l'age du personnage
if race_choix == 1:
    joueur = Personnages.Demi_Elfe(nom_joueur, nom_personnage, genre, 80, 40, 20, 100, 1.5, 1.9)
    joueur.caracteristiques(force, dexterité, constitution, inteligence ,sagesse, charisme)
elif race_choix == 2:
    joueur = Personnages.Demi_Orques(nom_joueur, nom_personnage, genre, 80, 40, 15, 50, 1.7, 2.1)
    joueur.caracteristiques(force, dexterité, constitution, inteligence, sagesse, charisme)
elif race_choix == 3:
    joueur = Personnages.Elfes_Hauts(nom_joueur, nom_personnage, genre, 70, 40, 80, 400, 1.5, 1.8)
    joueur.caracteristiques(force, dexterité, constitution, inteligence, sagesse, charisme)
elif race_choix == 4:
    joueur = Personnages.Elfes_Sylvains(nom_joueur, nom_personnage, genre, 60, 30, 50, 300, 1.4, 1.7)
    joueur.caracteristiques(force, dexterité, constitution, inteligence ,sagesse, charisme)
elif race_choix == 5:
    joueur = Personnages.Gnomes(nom_joueur, nom_personnage, genre, 50, 30, 40, 250, 1, 1.2)
    joueur.caracteristiques(force, dexterité, constitution, inteligence, sagesse, charisme)
elif race_choix == 6:
    joueur = Personnages.Halfelins(nom_joueur, nom_personnage, genre, 30, 20, 20, 100, .8, 1)
    joueur.caracteristiques(force, dexterité, constitution, inteligence, sagesse, charisme)
elif race_choix == 7:
    joueur = Personnages.Humains(nom_joueur, nom_personnage, genre, 120, 40, 18, 100, 1.5, 2)
    joueur.caracteristiques(force, dexterité, constitution, inteligence, sagesse, charisme)
elif race_choix == 8:
    joueur = Personnages.Nains(nom_joueur, nom_personnage, genre, 100, 50, 40, 200, 1.15, 1.35)
    joueur.caracteristiques(force, dexterité, constitution, inteligence, sagesse, charisme)

