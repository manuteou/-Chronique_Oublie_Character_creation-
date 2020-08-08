import tkinter
# from COFICHEPERSO import Personnages

ig = tkinter.Tk()
ig.title("Création de Personnage Chronique oubliée")


# Création d'un interface centrée

x_screen = ig.winfo_screenwidth()
y_screen = ig.winfo_screenmmheight()
x_windows = 800
y_windows = 400
pos_x = (x_screen//2)-(x_windows//2)
pos_y = (y_screen//2)-(y_screen//2)
geo = f"{x_windows}x{y_windows}+{pos_x}+{pos_y}"
ig.geometry(geo)


# Création de 2 frames pour la création du perso

perso_frame = tkinter.Frame(ig)
perso_frame.grid()
valide_frame = tkinter.Frame(ig)
valide_frame.grid()

# Champs de création du perso


nom_joueur = tkinter.Label(perso_frame, text="Nom du joueur")
nom_joueur.grid(column=0, row=0, padx=20)

entree_joueur = tkinter.StringVar()
joueur = tkinter.Entry(perso_frame, textvariable=entree_joueur)
joueur.grid(column=1, row=0)


nom_perso = tkinter.Label(perso_frame, text="Nom du Hero")
nom_perso.grid(column=2, row=0, padx=20)

entree_nom_perso = tkinter.StringVar()
nom_perso = tkinter.Entry(perso_frame, textvariable=entree_nom_perso)
nom_perso.grid(column=3, row=0)


genre_choix = tkinter.IntVar()
radio_genre_1 = tkinter.Radiobutton(perso_frame, text="Homme", value=1, variable=genre_choix)
radio_genre_2 = tkinter.Radiobutton(perso_frame, text="Femme", value=2, variable=genre_choix)
radio_genre_3 = tkinter.Radiobutton(perso_frame, text="Autre", value=3, variable=genre_choix)
radio_genre_1.grid(column=4, row=0, padx=100, sticky="W")
radio_genre_2.grid(column=4, row=1, padx=100, sticky="W")
radio_genre_3.grid(column=4, row=2, padx=100, sticky="W")


race_label = tkinter.Label(perso_frame, text="Choix de la race")
race_label.grid(column=0, row=3)

race_choix = tkinter.IntVar()
radio_DE = tkinter.Radiobutton(perso_frame, text="Demi-Elfe", value=1, variable=race_choix)
radio_DO = tkinter.Radiobutton(perso_frame, text="Demi-Orque", value=2, variable=race_choix)
radio_EH = tkinter.Radiobutton(perso_frame, text="Elfe Haut", value=3, variable=race_choix)
radio_ES = tkinter.Radiobutton(perso_frame, text="Elfe Sylvain", value=4, variable=race_choix)
radio_Gn = tkinter.Radiobutton(perso_frame, text="Gnome", value=5, variable=race_choix)
radio_Ha = tkinter.Radiobutton(perso_frame, text="Halfelin", value=6, variable=race_choix)
radio_Hu = tkinter.Radiobutton(perso_frame, text="Humain", value=7, variable=race_choix)
radio_Na = tkinter.Radiobutton(perso_frame, text="Nain", value=8, variable=race_choix)
radio_DE.grid(column=0, row=4, sticky="W")
radio_DO.grid(column=0, row=5, sticky="W")
radio_EH.grid(column=0, row=6, sticky="W")
radio_ES.grid(column=0, row=7, sticky="W")
radio_Gn.grid(column=0, row=8, sticky="W")
radio_Ha.grid(column=0, row=9, sticky="W")
radio_Hu.grid(column=0, row=10, sticky="W")
radio_Na.grid(column=0, row=11, sticky="W")

# Sortie de la boucle
Btn = tkinter.Button(valide_frame, text="Valider", width=5, height=2, command=ig.quit)
Btn.grid(sticky="")

ig.mainloop()

# recuperation des valeurs lorsque on ferme la fenettre
nj = joueur.get()
np = nom_perso.get()
gr = genre_choix.get()
rc = race_choix.get()
print(nj, np, gr, rc)
