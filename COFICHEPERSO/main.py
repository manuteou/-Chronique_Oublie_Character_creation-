# Programme principal
from COFICHEPERSO import Personnages
from COFICHEPERSO import Caracteristiques
from COFICHEPERSO import Interface_Graphique
from tkinter import *
import random

# lancement de la fenetre graphique

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
