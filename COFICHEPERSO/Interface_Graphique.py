import tkinter

ig = tkinter.Tk()
ig.title("Création de Personnage Chronique oubliée")

#Création d'un interface centrée

x_screen = ig.winfo_screenwidth()
y_screen =ig.winfo_screenmmheight()
x_windows =800
y_windows =400
pos_x = (x_screen//2)-(x_windows//2)
pos_y = (y_screen//2)-(y_screen//2)
geo=f"{x_windows}x{y_windows}+{pos_x}+{pos_y}"
ig.geometry(geo)


#Création de 2 frames pour la création du perso

perso_frame = tkinter.Frame(ig)
perso_frame.grid()
valide_frame = tkinter.Frame(ig)
valide_frame.grid()

#Champs de crétion du perso

nom_joueur = tkinter.Label(perso_frame, text="Nom du joueur")
nom_joueur.grid(column=0,row=0,padx=20)

entree_joueur = tkinter.Entry(perso_frame)
entree_joueur.grid(column=1,row=0)

nom_perso = tkinter.Label(perso_frame, text="Nom du Hero")
nom_perso.grid(column=2,row=0,padx=20)

entree_nom_perso=tkinter.Entry(perso_frame)
entree_nom_perso.grid(column=3,row=0)

genre_choix = tkinter.IntVar() # pour une futur connection
radio_genre_1 = tkinter.Radiobutton(perso_frame,text="Homme",value=1)
radio_genre_2 = tkinter.Radiobutton(perso_frame,text="Femme",value=2)
radio_genre_3 = tkinter.Radiobutton(perso_frame,text="Autre",value=3)
radio_genre_1.grid(column=4,row=0,padx=100,sticky = "W")
radio_genre_2.grid(column=4,row=1,padx=100,sticky = "W")
radio_genre_3.grid(column=4,row=2,padx=100,sticky = "W")

race_label = tkinter.Label(perso_frame,text="Choix de la race")
race_label.grid(column=0,row=3)

race_choix = tkinter.IntVar() #pour une futur connection
radio_DE = tkinter.Radiobutton(perso_frame,text="Demi-Elfe",value=1)
radio_DO = tkinter.Radiobutton(perso_frame,text="Demi-Orque",value=2)
radio_EH = tkinter.Radiobutton(perso_frame,text="Elfe Haut",value=3)
radio_ES = tkinter.Radiobutton(perso_frame,text="Elfe Sylvain",value=4)
radio_Gn = tkinter.Radiobutton(perso_frame,text="Gnome",value=5)
radio_Ha = tkinter.Radiobutton(perso_frame,text="Halfelin",value=6)
radio_Hu = tkinter.Radiobutton(perso_frame, text="Humain",value=7)
radio_Na = tkinter.Radiobutton(perso_frame, text="Nain",value=8)
radio_DE.grid(column=0,row=4,sticky = "W")
radio_DO.grid(column=0,row=5,sticky = "W")
radio_EH.grid(column=0,row=6,sticky = "W")
radio_ES.grid(column=0,row=7,sticky = "W")
radio_Gn.grid(column=0,row=8,sticky = "W")
radio_Ha.grid(column=0,row=9,sticky = "W")
radio_Hu.grid(column=0,row=10,sticky = "W")
radio_Na.grid(column=0,row=11,sticky = "W")

# Validation des choix est sortie
Btn = tkinter.Button(valide_frame,text="OK",width=5,height=2)
Btn.grid(sticky="")

ig.mainloop()
