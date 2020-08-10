# Programme principal
from COFICHEPERSO import Personnages
from COFICHEPERSO.Interface_Graphique import Interface_graphique_perso,Interface_graphique_Introduction
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

    # On fabrique le joueur
    if interface.genre_choix.get() == 1:
        genre = "Homme"
    elif interface.genre_choix.get() == 2:
        genre = "femme"
    elif interface.genre_choix.get() == 3:
        genre = "Autre"


    if interface.race_choix.get() == 1:
        joueur = Personnages.Demi_Elfe(interface.joueur.get(), interface.nom_perso.get(), genre, 80, 40, 20, 100, 1.5, 1.9,
                                       int(interface.force.get()), int(interface.dexterite.get()), int(interface.constitution.get()) - 2, int(interface.intelligence.get()), int(interface.sagesse.get()) + 2, int(interface.charisme.get()))
    elif interface.race_choix.get() == 2:
        joueur = Personnages.Demi_Orques(interface.race_choix.get(), interface.nom_perso.get(), genre, 80, 40, 15, 50, 1.7, 2.1,
                                         int(interface.force.get()) + 2, int(interface.dexterite.get()), int(interface.constitution.get()), int(interface.intelligence.get()) - 2, int(interface.sagesse.get()), int(interface.charisme.get()) - 2)
    elif interface.race_choix.get() == 3:
        joueur = Personnages.Elfes_Hauts(interface.race_choix.get(), interface.nom_perso.get(), genre, 70, 40, 80, 400, 1.5, 1.8,
                                         int(interface.force.get()) - 2, int(interface.dexterite.get()), int(interface.constitution.get()), int(interface.intelligence.get()), int(interface.sagesse.get()), int(interface.charisme.get()) + 2)
    elif interface.race_choix.get() == 4:
        joueur = Personnages.Elfes_Sylvains(interface.race_choix.get(), interface.nom_perso.get(), genre, 60, 30, 50, 300, 1.4, 1.7,
                                            int(interface.force.get()), int(interface.dexterite.get()), int(interface.constitution.get()) - 2, int(interface.intelligence.get()), int(interface.sagesse.get()) + 2, int(interface.charisme.get()))
    elif interface.race_choix.get() == 5:
        joueur = Personnages.Gnomes(interface.race_choix.get(), interface.nom_perso.get(), genre, 50, 30, 40, 250, 1, 1.2,
                                    int(interface.force.get()) - 2, int(interface.dexterite.get()), int(interface.constitution.get()), int(interface.intelligence.get()) + 2, int(interface.sagesse.get()), int(interface.charisme.get()))
    elif interface.race_choix.get() == 6:
        joueur = Personnages.Halfelins(interface.race_choix.get(), interface.nom_perso.get(), genre, 30, 20, 20, 100, .8, 1,
                                       int(interface.force.get()) - 2, int(interface.dexterite.get()) + 2, int(interface.constitution.get()), int(interface.intelligence.get()),int(interface.sagesse.get()), int(interface.charisme.get()))
    elif interface.race_choix.get() == 7:
        joueur = Personnages.Humains(interface.race_choix.get(), interface.nom_perso.get(), genre, 120, 40, 18, 100, 1.5, 2,
                                     int(interface.force.get()), int(interface.dexterite.get()), int(interface.constitution.get()), int(interface.intelligence.get()), int(interface.sagesse.get()), int(interface.charisme.get()))
    elif interface.race_choix.get() == 8:
        joueur = Personnages.Nains(interface.race_choix.get(), interface.nom_perso.get(), genre, 100, 50, 40, 200, 1.15, 1.35,
                                   int(interface.force.get()), int(interface.dexterite.get()) - 2, int(interface.constitution.get()) + 2, int(interface.intelligence.get()), int(interface.sagesse.get()), int(interface.charisme.get()))

    ig_perso.destroy()

    return joueur


def creation_pdf(pdf):
    """ Generation du pdf"""

    image = Path("fiche_perso.png")
    pdf.drawImage(image, 0, 0)
    pdf.drawString(400, 668, str(joueur.nom_personnage),)
    pdf.drawString(145, 668, str(joueur.nom_heros))

    pdf.drawString(220, 623, str(joueur.race))
    pdf.drawString(343, 623, joueur.genre)
    pdf.drawString(420, 623, str(f"{joueur.taille:0.2f}"))
    pdf.drawString(391, 623, str(joueur.age))
    pdf.drawString(470, 623, str(joueur.poids))

    pdf.drawString(80, 560, str(joueur.force))
    pdf.drawString(80, 538, str(joueur.dexterite))
    pdf.drawString(80, 515, str(joueur.constitution))
    pdf.drawString(80, 492, str(joueur.intelligence))
    pdf.drawString(80, 470, str(joueur.sagesse))
    pdf.drawString(80, 450, str(joueur.charisme))


# lancement de la fenetre graphique d'introduction pour faire jolie
main = Tk()
image = PhotoImage(file="Persos.png").subsample(2)
Interface_graphique_Introduction(main, image)
main.mainloop()

# On genere le joueur
joueur = generation_perso()

# création du pdf
nom_pdf = str(joueur.nom_personnage) + "_" + str(joueur.nom_heros) + ".pdf"
pdf = canvas.Canvas(nom_pdf)
creation_pdf(pdf)
pdf.showPage()
pdf.save()
