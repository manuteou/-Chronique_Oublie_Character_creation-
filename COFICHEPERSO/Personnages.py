from random import randint, uniform
from  COFICHEPERSO import Caractéristiques

class Nom:
    def __init__(self, nom_personnage, nom_heros,genre):
        self.nom_personnage = nom_personnage
        self.nom_heros = nom_heros
        self.genre = genre
        self.caracteristiques = Caractéristiques()


class Physique:
    def __init__(self, p_max, p_min, a_min, a_max, t_min, t_max):
        self.p_max = p_max
        self.p_min = p_min
        self.a_min = a_min
        self.a_max = a_max
        self.t_min = t_min
        self.t_max = t_max
        self.poids = 0
        self.age = 0
        self.taille = 0

    def calcul_poids(self, p_min, p_max):
        self.poids = randint(p_min, p_max)

    def calcul_age(self, a_min, a_max):
        self.age = randint(a_min, a_max)

    def calcul_taille(self, t_min, t_max):
        self.taille = uniform(t_min, t_max)


class Demi_Elfe(Nom,Physique):
    def __init__(self, nom_personnage, nom_heros,genre,p_max, p_min, a_min, a_max, t_min, t_max):
        Nom.__init__(self,nom_personnage,nom_heros,genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        self.race = "Demi-Elfe"



class Demi_Orques(Nom,Physique):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        self.race = "Demi-Orques"



class Elfes_Hauts(Nom,Physique):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        self.race = "Elfes Hauts"



class Elfes_Sylvains(Nom,Physique):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        self.race = "Elfes Sylvains"



class Gnomes(Nom,Physique):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        self.race = "Gnomes"


class Halfelins(Nom,Physique):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        self.race = "Halfelins"



class Humains(Nom,Physique):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        self.race = "Humains"


class Nains(Nom,Physique):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        self.race = "Nains"






