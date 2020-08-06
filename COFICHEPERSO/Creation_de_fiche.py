from pprint import pprint
import random
from COFICHEPERSO.Personnages import Personnages
from COFICHEPERSO.Caracteristiques import Caractéristiques

roll = [random.randint(3,18) for r in range(6)] # Dés lancées pour la valeurs des caractériqtiques du personnage

str= dex= con= inte= sag= cha = 0

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
genre = input ("Est tu de genre (M)asculine ou F(eminin) ou (A)utre ?")
val = int(input(" Rentres le numero pour choisir ta race : \n \t 1 - Demi-Elfe\n"
             "\t 2 - Demi-Orques\n \t 3 - Elfe Haut\n \t 4 - Elfe Sylvain\n \t 5 - Gnome\n "
             "\t 6 - Halfelin\n \t 7 - Humain\n \t 8 - Nain \n"))


debut = True
while debut: # Définition de la race qui permet de generer les autres valeurs du perso ainsi que les bonus de classe
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
        age = random.randint(80,400)
        poids = random.randint(40, 70)
        taille = random.uniform(1.50, 1.80)
        str = -2
        cha = 2
        debut = False
    elif val == 4:
        race = "Elfe-Sylvain"
        age = random.randint(50,300)
        poids = random.randint(30, 60)
        taille = random.uniform(1.40, 1.70)
        str = -2
        dex = 2
        debut = False
    elif val == 5:
        race = "Gnome"
        age = random.randint(40,250)
        poids = random.randint(30, 50)
        taille = random.uniform(1, 1.20)
        str = -2
        inte = 2
        debut = False
    elif val == 6:
        race = "Halflain"
        age = random.randint(20,100)
        poids = random.randint(20, 30)
        taille = random.uniform(0.80, 1)
        str = -2
        dex = 2
        debut = False
    elif val == 7:
        race = "Humain"
        age = random.randint(18,100)
        poids = random.randint(40, 120)
        taille = random.uniform(1.50, 2.00)
        debut = False
    elif val == 8:
        race = "Nain"
        age = random.randint(40,200)
        poids = random.randint(50, 100)
        taille = random.uniform(1.15, 1.35)
        con = 2
        dex = -2
        debut = False
    else:
        val = int(input("Mauvaise valeur, rentrez une chiffre valable : "))


Joueur_Perso = Personnages(nom_personnage=nom,nom_joueur=nom_hero,race=race,age=age,poids=poids,taille=taille,
                           sexe=genre)

print(f"Le personnage {Joueur_Perso.get_nom_personnage() }, jouer par {Joueur_Perso.get_nom_joueur()},\ "
      f"tu vas tirer ses attributs")

#Attribution des characteristiques
Joueur_Perso.caracteristique = Caractéristiques()
print (f"Valeurs du lancé de dé : {roll}")
choix = int(input("Quelle valeur pour la caracteristique force :"))
Joueur_Perso.caracteristique.set_force(attribution(choix)+str)
print (f"Valeurs du lancé de dé : {roll}")
choix = int(input("Quelle valeur pour la caracteristique Dexterité :"))
Joueur_Perso.caracteristique.set_dexterité(attribution(choix)+dex)
print (f"Valeurs du lancé de dé : {roll}")
choix = int(input("Quelle valeur pour la caracteristique Constitution :"))
Joueur_Perso.caracteristique.set_constitution(attribution(choix)+con)
print (f"Valeurs du lancé de dé : {roll}")
choix = int(input("Quelle valeur pour la caracteristique Intelligence :"))
Joueur_Perso.caracteristique.set_inteligence(attribution(choix)+inte)
print (f"Valeurs du lancé de dé : {roll}")
choix = int(input("Quelle valeur pour la caracteristique Sagesse :"))
Joueur_Perso.caracteristique.set_sagesse(attribution(choix)+sag)
print (f"Valeurs du lancé de dé : {roll}")
choix = int(input("Quelle valeur pour la caracteristique Charisme :"))
Joueur_Perso.caracteristique.set_charisme(attribution(choix)+cha)


pprint(Joueur_Perso)
