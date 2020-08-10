# Programme principal
from COFICHEPERSO import Personnages
from COFICHEPERSO.Interface_Graphique import Interface_graphique_perso
from tkinter import *
from reportlab.pdfgen import canvas
from pathlib import Path
from random import randint


def fenetre(image):
    """fonction qui definie l'introduction """
    canvas = Canvas(main, heigh=400, width=800)
    canvas.create_image(400, 300, image=image)
    canvas.create_text(400, 70, text="CHRONIQUES OUBLIEES\n Generateur de Personnage", font=("Helvetica", 40))
    canvas.pack(expand=YES)


def generation_perso():
    """ fonction qui genere un joueur"""
    # lancement de la  fenetre graphique du personnage
    ig_perso = Tk()
    ig_perso.title("Création de Personnage CO")
    ig_perso.minsize(700, 360)
    roll = [randint(3, 18) for r in range(6)]
    interface = Interface_graphique_perso(ig_perso, roll)
    ig_perso.mainloop()

    # on recupere les variables
    race_choix = interface.race_choix.get()
    nom_joueur = interface.joueur.get()
    nom_personnage = interface.nom_perso.get()
    genre = interface.genre_choix.get()
    force = int(interface.force.get())
    dexterite = int(interface.dexterite.get())
    constitution = int(interface.constitution.get())
    intelligence = int(interface.intelligence.get())
    charisme = int(interface.charisme.get())
    sagesse = int(interface.sagesse.get())

    # On fabrique le joueur
    if race_choix == 1:
        joueur = Personnages.Demi_Elfe(nom_joueur, nom_personnage, genre, 80, 40, 20, 100, 1.5, 1.9,
                                       force, dexterite, constitution - 2, intelligence, sagesse + 2, charisme)
    elif race_choix == 2:
        joueur = Personnages.Demi_Orques(nom_joueur, nom_personnage, genre, 80, 40, 15, 50, 1.7, 2.1,
                                         force + 2, dexterite, constitution, intelligence - 2, sagesse, charisme - 2)
    elif race_choix == 3:
        joueur = Personnages.Elfes_Hauts(nom_joueur, nom_personnage, genre, 70, 40, 80, 400, 1.5, 1.8,
                                         force - 2, dexterite, constitution, intelligence, sagesse, charisme + 2)
    elif race_choix == 4:
        joueur = Personnages.Elfes_Sylvains(nom_joueur, nom_personnage, genre, 60, 30, 50, 300, 1.4, 1.7,
                                            force, dexterite, constitution - 2, intelligence, sagesse + 2, charisme)
    elif race_choix == 5:
        joueur = Personnages.Gnomes(nom_joueur, nom_personnage, genre, 50, 30, 40, 250, 1, 1.2,
                                    force - 2, dexterite, constitution, intelligence + 2, sagesse, charisme)
    elif race_choix == 6:
        joueur = Personnages.Halfelins(nom_joueur, nom_personnage, genre, 30, 20, 20, 100, .8, 1,
                                       force - 2, dexterite + 2, constitution, intelligence, sagesse, charisme)
    elif race_choix == 7:
        joueur = Personnages.Humains(nom_joueur, nom_personnage, genre, 120, 40, 18, 100, 1.5, 2,
                                     force, dexterite, constitution, intelligence, sagesse, charisme)
    elif race_choix == 8:
        joueur = Personnages.Nains(nom_joueur, nom_personnage, genre, 100, 50, 40, 200, 1.15, 1.35,
                                   force, dexterite - 2, constitution + 2, intelligence, sagesse, charisme)

    ig_perso.destroy()

    return joueur


def creation_pdf(pdf):
    """ Generation du pdf"""

    image = Path("fiche_perso.png")
    pdf.drawImage(image, 0, 0)
    pdf.drawString(400, 668, joueur.nom_personnage)
    pdf.drawString(145, 668, joueur.nom_heros)
    #pdf.drawString(30, 720, joueur.genre)
    #pdf.drawString(30, 710, joueur.taille)
    #pdf.drawString(30, 700, joueur.age)
    #pdf.drawString(30, 690, joueur.poids)
    #pdf.drawString(30, 680, joueur.force)
    #pdf.drawString(30, 670, joueur.dexterite)
    #pdf.drawString(30, 660, joueur.constitution)
    #pdf.drawString(30, 650, joueur.charisme)
    #pdf.drawString(30, 640, joueur.sagesse)


# lancement de la fenetre graphique d'introduction
main = Tk()
image = PhotoImage(file="Persos.png").subsample(2)
main.geometry("800x600")
main.title("Création de Personnage CO")
fenetre(image)
Btn = Button(main, text="Suite", width=5, height=2, command=main.destroy)
Btn.pack()
main.mainloop()

joueur = generation_perso()

# création du pdf
nom_pdf = joueur.nom_personnage + "_" + joueur.nom_heros + ".pdf"
pdf = canvas.Canvas(nom_pdf)
creation_pdf(pdf)
pdf.showPage()
pdf.save()
