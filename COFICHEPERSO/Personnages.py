from COFICHEPERSO.Caracteristiques import Caractéristiques

class Personnages:
    """" Class qui definie le type  du personnage et son aspect physique"""
    def __init__(self,nom_personnage ,nom_joueur ,race,profile = 'Dieu',niveau = 0,sexe = 'MF',age = 1 ,taille = 2,poids = 10):
        self.nom_personnage = nom_personnage
        self.nom_joueur = nom_joueur
        self.profile = profile
        self.niveau = niveau
        self.race = race
        self.sexe = sexe
        self.age = age
        self.taille = taille
        self.poids = poids
        self.caracteristique = Caractéristiques


    def get_nom_personnage(self):
        return self.nom_personnage

    def set_nom_personnage(self, nom_personnage):
        self.nom_personnage = nom_personnage

    def get_nom_joueur(self):
        return self.nom_joueur

    def set_nom_joueur(self, nom_joueur):
        self.nom_joueur = nom_joueur

    def get_profile(self):
        return self.profile

    def set_profile(self,profile):
        self.profile = profile

    def get_niveau(self):
        return self.niveau

    def set_niveau(self,niveau):
        self.niveau = niveau

    def _get_race(self):
        return self.race

    def set_race(self,race):
        self.race = race

    def get_sexe(self):
        return self.sexe

    def set_sexe(self,sexe):
        self.sexe = sexe

    def get_age(self):
        return self.profile

    def set_age(self,age):
        self.age = age

    def get_taille(self):
        return self.taille

    def set_taille(self,taille):
        self.taille = taille

    def _get_poids(self):
        return self.poids

    def set_poids(self,poids):
        self.poids = poids







