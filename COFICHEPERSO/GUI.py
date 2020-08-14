from pathlib import Path
from tkinter import *
import json
from random import randint


class GUI(Frame):
    """
        Graphique class for character selection
                                                """

    def __init__(self, window, roll, race_list, profile_list):
        Frame.__init__(self, window)
        self.grid()
        self.roll = roll
        self.race_list = race_list
        self.profile_list = profile_list

        # player's name entry
        self.player_name = Label(self, text="Nom du joueur")
        self.player_name.grid(column=0, row=0)

        self.player_variable = StringVar()
        self.player_name_entry = Entry(self, textvariable=self.player_variable)
        self.player_name_entry.grid(column=0, row=1)
        # player's hero name entry
        self.hero_name = Label(self, text="Nom du Hero")
        self.hero_name.grid(column=1, row=0)

        self.hero_variable = StringVar()
        self.hero_name_entry = Entry(self, textvariable=self.hero_variable)
        self.hero_name_entry.grid(column=1, row=1)

        # Race's selection by list
        self.race_label = Label(self, text="Race")
        self.race_label.grid(column=0, row=2)

        self.lb_race = Listbox(self, bd=3, exportselection=0)
        for i, race in enumerate(race_list, 1):
            self.lb_race.insert(i, race["race_name"])
        self.lb_race.grid(column=0, row=3)

        # Profile's selection
        self.profile_label = Label(self, text="Profile")
        self.profile_label.grid(column=1, row=2)

        self.lb_profile = Listbox(self, bd=3, exportselection=0)
        for i, row in enumerate(profile_list, 1):
            self.lb_profile.insert(i, row["profile_name"])
        self.lb_profile.grid(column=1, row=3)

        self.roll_dice_label = Label(self, text="<Lancé des dés>")
        self.roll_dice_label.grid(columnspan=2, row=10)
        self.roll_dice_value = Label(self, text=self.roll, font=",25")
        self.roll_dice_value.grid(columnspan=2, row=11)

        attribut = ["Force", "Dexterité", "Constitution", "Intelligence", "Charisme", "Sagesse"]
        row = 3
        for i in attribut:
            row += 1
            self.attribut_label = Label(self, text=i)
            self.attribut_label.grid(column=0, row=row)

        # champs pour taper les valeurs
        self.Grab_Str = IntVar()
        self.Str_Value = Entry(self, textvariable=self.Grab_Str)
        self.Str_Value.grid(column=1, row=4)

        self.Grab_Dex = IntVar()
        self.Dex_Value = Entry(self, textvariable=self.Grab_Dex)
        self.Dex_Value.grid(column=1, row=5)

        self.Grab_Con = IntVar()
        self.Con_Value = Entry(self, textvariable=self.Grab_Con)
        self.Con_Value.grid(column=1, row=6)

        self.Grab_Int = IntVar()
        self.Int_Value = Entry(self, textvariable=self.Grab_Int)
        self.Int_Value.grid(column=1, row=7)

        self.Grab_Sag = IntVar()
        self.Sag_Value = Entry(self, textvariable=self.Grab_Sag)
        self.Sag_Value.grid(column=1, row=8)

        self.Grab_Cha = IntVar()
        self.Cha_Value = Entry(self, textvariable=self.Grab_Cha)
        self.Cha_Value.grid(column=1, row=9)

        self.bonus_label = Label(self, text="Bonus de race")
        self.bonus_label.grid(column=3, row=2)
        self.lb_bonus = Listbox(self, bd=1, exportselection=0, bg='grey', selectbackground='grey')
        i = 1
        for racial_bonus in race_list:
            modif = ""
            i += 1
            for stat, value in racial_bonus["modif"].items():
                if value != 0:
                    modif += f"{stat} {value}  "
            self.lb_bonus.insert(i, modif)
        self.lb_bonus.grid(column=3, row=3)

        self.info_life = Label(self, text="Dé VIE")
        self.info_life.grid(column=4, row=2)
        self.life_lb = Listbox(self, bd=3, exportselection=0, bg='grey', selectbackground='grey')
        for i, row in enumerate(profile_list, 1):
            self.life_lb.insert(i, row["life_dice"])
        self.life_lb.grid(column=4, row=3)

        self.get_gender_value = IntVar()
        self.gender_label = Label(self, text="Genre      =>")
        self.gender_label.grid(column=3, row=4)
        gender = ["Homme", "Femme ", "Autre    "]
        row = 1
        for i in gender:
            row += 3
            self.gender_rb = Radiobutton(self, text=i, value=row, anchor="e", padx=20, variable=self.get_gender_value)
            self.gender_rb.grid(column=4, row=row)

        # Sortie de la boucle
        self.Btn = Button(self, text="Valider et generer PDF", command=self.quit)
        self.Btn.grid(column=1, row=12)
        self.Btn = Button(self, text="Quitter", command=self.destroy)
        self.Btn.grid(column=0, row=12)


class GUI_Intro ():

    def __init__(self, main, image):
        self.main = main
        self.image = image
        self.main.geometry("800x600")
        self.main.title("Création de Personnage CO")
        self.canvas = Canvas(self.main, heigh=400, width=800)
        self.canvas.create_image(400, 300, image=self.image)
        self.canvas.create_text(400, 70, text="CHRONIQUES OUBLIEES\n Generateur de Personnage", font=("Helvetica", 40))
        self.canvas.pack()
        self.Btn = Button(self.main, text="Suite", width=5, height=2, command=main.destroy)
        self.Btn.pack()

