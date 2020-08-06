import random
from COFICHEPERSO.Personnages import Personnages
from COFICHEPERSO.Caracteristiques import Caractéristiques

roll = [random.randint(3,18) for r in range(6)] # Dés lancées pour la valeurs des caractériqtiques du personnage


def attribution(valeur_choisie):
    """fonction qui permet d'attirbuer les valeurs du lancé de dé et d'effacer la valeur"""
    fin = True
    if valeur_choisie in roll:
            roll.remove(valeur_choisie)
            print("valeur attribuée")
            return valeur_choisie

    else:
        while fin:
            print(f"la valeur choisie doit etre parmis {roll}")
            valeur_choisie = int(input("Rentrez une valeur valide"))
            if valeur_choisie in roll:
                roll.remove(valeur_choisie)
                fin = False
        return valeur_choisie


print ("BIENVENUE SUR LE GENERATEUR DE PERSONNAGE CHRONIQUE OUBLIEE")



nom = input("Bonjour aventurier, quel est ton prénom :")
nom_hero = input("Quel nom veux tu donner à ton personnage :")
val = input(" Rentres le numero pour choisir ta race : \n \t 1 - Demi-Elfe\n"
             "\t 2 - Demi-Orques\n \t 3 - Elfe Haut\n \t 4 - Elfe Sylvain\n \t 5 - Gnome\n "
             "\t 6 - Halfelin\n \t 7 - Humain\n \t 8 - Nain \n")
genre = input ("Est tu de genre (M)asculine ou F(eminin) ou (A)utre ?")

debut = True
while debut:
    if val == 1:
        race = "Demi-Elfe"
        age = random.randint(20,100)
        poids = random.randint(40,80)
        taille = random.uniform(1.50,1.90)
        sag = 2
        con = -2
        debut = False
    elif val == 2:
        race = "Demi-Orques"
        age = random.randint(15,50)
        poids = random.randint(40, 80)
        taille = random.uniform(1.70, 2.10)
        str = 2
        inte = -2
        cha = -2
        debut = False
    elif val == 3:
        race = "Elfe-Haut"
        age = random.randint(15,50)
        poids = random.randint(40, 80)
        taille = random.uniform(1.70, 2.10)
        str = 2
        inte = -2
        debut = False
    elif val == 2:
        race = "Elfe-Sylvain"
        age = random.randint(15,50)
        poids = random.randint(40, 80)
        taille = random.uniform(1.70, 2.10)
        str = 2
        inte = -2
        debut = False
    elif val == 2:
        race = "Gnome"
        age = random.randint(15,50)
        poids = random.randint(40, 80)
        taille = random.uniform(1.70, 2.10)
        str = 2
        inte = -2
        debut = False
    elif val == 2:
        race = "Halflain"
        age = random.randint(15,50)
        poids = random.randint(40, 80)
        taille = random.uniform(1.70, 2.10)
        str = 2
        inte = -2
        debut = False
    elif val == 2:
        race = "Humain"
        age = random.randint(15,50)
        poids = random.randint(40, 80)
        taille = random.uniform(1.70, 2.10)
        str = 2
        inte = -2
        debut = False
    elif val == 2:
        race = "Nain"
        age = random.randint(15,50)
        poids = random.randint(40, 80)
        taille = random.uniform(1.70, 2.10)
        str = 2
        inte = -2
        debut = False


Joueur_Perso = Personnages(nom_personnage=nom,nom_joueur=nom_hero,race=race,age=age,poids=poids,taille=taille,
                           sexe=genre)

print(f"Le personnage {Joueur_Perso.get_nom_personnage() }, jouer par {Joueur_Perso.get_nom_joueur()},\ "
      f"tu vas tirer ses attributs")


print (f"Valeurs du lancé de dé : {roll}")
Joueur_Carac = Caractéristiques()
force = int(input("Quelle valeur pour la caracteristique force :"))
Joueur_Carac.set_force(attribution(force))


