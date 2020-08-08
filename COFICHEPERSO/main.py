# Programme principal
from COFICHEPERSO import Personnages
from COFICHEPERSO import Caracteristiques
from COFICHEPERSO import Interface_Graphique
import tkinter
import random


# lancement de la fenetre graphique
ig_perso = tkinter.Tk()
ig_perso.title("Création de Personnage Chronique oubliée")
interface = Interface_Graphique.Interface_graphique_perso(ig_perso)
ig_perso.mainloop()

# on recupere les champs dans des variables
nom_joueur = interface.joueur.get()
nom_personnage = interface.nom_perso.get()
genre = interface.genre_choix.get()
race_choix = interface.race_choix.get()

# on detruit la fenetre
ig_perso.destroy()

if race_choix == 1:
    race = "Demi-Elfe"
    age = random.randint(20, 100)
    poids = random.randint(40, 80)
    taille = random.uniform(1.50, 1.90)
    sag = 2
    con = -2
elif race_choix == 2:
    race = "Demi-Orques"
    age = random.randint(15, 50)
    poids = random.randint(40, 80)
    taille = random.uniform(1.70, 2.10)
    str = 2
    inte = -2
    cha = -2
elif race_choix == 3:
    race = "Elfe-Haut"
    age = random.randint(80, 400)
    poids = random.randint(40, 70)
    taille = random.uniform(1.50, 1.80)
    str = -2
    cha = 2
elif race_choix == 4:
    race = "Elfe-Sylvain"
    age = random.randint(50, 300)
    poids = random.randint(30, 60)
    taille = random.uniform(1.40, 1.70)
    str = -2
    dex = 2
elif race_choix == 5:
    race = "Gnome"
    age = random.randint(40, 250)
    poids = random.randint(30, 50)
    taille = random.uniform(1, 1.20)
    str = -2
    inte = 2
elif race_choix == 6:
    race = "Halflain"
    age = random.randint(20, 100)
    poids = random.randint(20, 30)
    taille = random.uniform(0.80, 1)
    str = -2
    dex = 2
elif race_choix == 7:
    race = "Humain"
    age = random.randint(18, 100)
    poids = random.randint(40, 120)
    taille = random.uniform(1.50, 2.00)
elif race_choix == 8:
    race = "Nain"
    age = random.randint(40, 200)
    poids = random.randint(50, 100)
    taille = random.uniform(1.15, 1.35)
    con = 2
    dex = -2

#création du joueur
joueur= Personnages.Personnages(nom_personnage=nom_personnage, nom_joueur=nom_joueur, race=race, age=age, poids=poids,
                                 taille=taille, sexe=genre)
