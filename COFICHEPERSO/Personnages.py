from random import randint, uniform


class Nom:
    """Classe qui definie les info nominatifs du joueur"""

    def __init__(self, nom_personnage, nom_heros, genre):
        self.nom_personnage = nom_personnage
        self.nom_heros = nom_heros
        self.genre = genre


class Caracteristiques:
    """ Classe qui definie les attributs du personnage"""

    def __init__(self, force, dexterite, constitution, intelligence, sagesse, charisme):
        self.force = force
        self.dexterite = dexterite
        self.constitution = constitution
        self.intelligence = intelligence
        self.sagesse = sagesse
        self.charisme = charisme


class Physique:
    """Classe qui definie le physique du personnage"""

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


# Classes filles qui regroupent les classes mere et rajoutent la race

class Demi_Elfe(Nom, Physique, Caracteristiques):

    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max,
                 force, dexterite, constitution, intelligence, sagesse, charisme):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        Caracteristiques.__init__(self, force, dexterite, constitution, intelligence, sagesse, charisme)
        self.race = "Demi-Elfe"
        self.calcul_poids(p_min,p_max)
        self.calcul_age(a_min,a_max)
        self.calcul_taille(t_min,t_max)

class Demi_Orques(Nom, Physique, Caracteristiques):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max,
                 force, dexterite, constitution, intelligence, sagesse, charisme):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        Caracteristiques.__init__(self, force, dexterite, constitution, intelligence, sagesse, charisme)
        self.race = "Demi-Orques"
        self.calcul_poids(p_min, p_max)
        self.calcul_age(a_min, a_max)
        self.calcul_taille(t_min, t_max)

class Elfes_Hauts(Nom, Physique, Caracteristiques):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max,
                 force, dexterite, constitution, intelligence, sagesse, charisme):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        Caracteristiques.__init__(self, force, dexterite, constitution, intelligence, sagesse, charisme)
        self.race = "Elfes Hauts"
        self.calcul_poids(p_min, p_max)
        self.calcul_age(a_min, a_max)
        self.calcul_taille(t_min, t_max)

class Elfes_Sylvains(Nom, Physique, Caracteristiques):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max,
                 force, dexterite, constitution, intelligence, sagesse, charisme):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        Caracteristiques.__init__(self, force, dexterite, constitution, intelligence, sagesse, charisme)
        self.race = "Elfes Sylvains"
        self.calcul_poids(p_min, p_max)
        self.calcul_age(a_min, a_max)
        self.calcul_taille(t_min, t_max)

class Gnomes(Nom, Physique, Caracteristiques):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max,
                 force, dexterite, constitution, intelligence, sagesse, charisme):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        Caracteristiques.__init__(self, force, dexterite, constitution, intelligence, sagesse, charisme)
        self.race = "Gnomes"
        self.calcul_poids(p_min, p_max)
        self.calcul_age(a_min, a_max)
        self.calcul_taille(t_min, t_max)

class Halfelins(Nom, Physique, Caracteristiques):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max,
                 force, dexterite, constitution, intelligence, sagesse, charisme):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        Caracteristiques.__init__(self, force, dexterite, constitution, intelligence, sagesse, charisme)
        self.race = "Halfelins"
        self.calcul_poids(p_min, p_max)
        self.calcul_age(a_min, a_max)
        self.calcul_taille(t_min, t_max)

class Humains(Nom, Physique, Caracteristiques):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max,
                 force, dexterite, constitution, intelligence, sagesse, charisme):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        Caracteristiques.__init__(self, force, dexterite, constitution, intelligence, sagesse, charisme)
        self.race = "Humains"
        self.calcul_poids(p_min, p_max)
        self.calcul_age(a_min, a_max)
        self.calcul_taille(t_min, t_max)

class Nains(Nom, Physique, Caracteristiques):
    def __init__(self, nom_personnage, nom_heros, genre, p_max, p_min, a_min, a_max, t_min, t_max,
                 force, dexterite, constitution, intelligence, sagesse, charisme):
        Nom.__init__(self, nom_personnage, nom_heros, genre)
        Physique.__init__(self, p_max, p_min, a_min, a_max, t_min, t_max)
        Caracteristiques.__init__(self, force, dexterite, constitution, intelligence, sagesse, charisme)
        self.race = "Nains"
        self.calcul_poids(p_min, p_max)
        self.calcul_age(a_min, a_max)
        self.calcul_taille(t_min, t_max)