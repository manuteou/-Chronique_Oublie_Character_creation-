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

def profile_choix():
    """ fonction qui definie les profiles les bonus de profiles et equipements de profile"""
    pass

def race_choix():
    """ fonction qui definie la race est les bonus de races"""
    pass

def age_choix():
    """ foncition qui donne un age est correcte pour la race"""
    pass

def taille_choix():
    """fonction qui donne une taille correcte pour la race"""
    pass

def poids_choix():
    """ fonction qui donne un poids correcte pour la race"""
    pass

print ("BIENVENUE SUR LE GENERATEUR DE PERSONNAGE CHRONIQUE OUBLIEE")

Joueur_Perso = Personnages()

nom = input("Bonjour aventurier, quel est ton prénom :")
nom_hero = input("Quel nom veux tu donner à ton personnage :")
profile = input("Quel est ton profile :")
race = input("Quel est ta race :")
sexe = input("Quel est ton genre :")
age = input("Quel est ton age :")
taille = input("Quel est ta taille :")
poids = input("Quel est ton poids")

Joueur_Perso.set_nom_joueur(nom)
Joueur_Perso.set_nom_personnage(nom_hero)
Joueur_Perso.set_profile(profile)
Joueur_Perso.set_race(race)
Joueur_Perso.set_sexe(sexe)
Joueur_Perso.set_age(age)
Joueur_Perso.set_taille(taille)
Joueur_Perso.set_poids()

print(f"Le personnage {Joueur_Perso.get_nom_personnage() }, jouer par {Joueur_Perso.get_nom_joueur()} /"
      f"va tirer ses attributs")


print (f"Valeurs du lancé de dé : {roll}")
Joueur_Carac = Caractéristiques()
force = int(input("Quelle valeur pour la caracteristique force :"))
Joueur_Carac.set_force(attribution(force))


