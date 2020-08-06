
class Caractéristiques:
    """ Classe qui definie les characteristique du personnage"""
    def __init__(self, force=0, dexterité=0, constitution=0, inteligence=0, sagesse=0, charisme=0):
        self.force = force
        self.dexterité = dexterité
        self.constitution = constitution
        self.inteligence = inteligence
        self.sagesse = sagesse
        self.charisme = charisme

    def get_force(self):
        return self.force

    def set_force(self, force):
        self.force = force

    def get_dexterité(self):
        return self.dexterité

    def set_dexterité(self, dexterité):
        self.dexterité = dexterité

    def get_constitution(self):
        return self.constitution

    def set_constitution(self, constitution):
        self.constitution = constitution

    def get_inteligence(self):
        return self.inteligence

    def set_inteligence(self, inteligence):
        self.inteligence = inteligence

    def get_sagesse(self):
        return self.sagesse

    def set_sagesse(self, sagesse):
        self.sagesse = sagesse

    def get_charisme(self):
        return self.charisme

    def set_charisme(self, charisme):
        self.charisme = charisme


