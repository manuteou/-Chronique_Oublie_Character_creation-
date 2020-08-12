class Character():

    def __init__(self, player_name="Manu", character_name="Zorg", attribut={}, description={}, profile={}):
        self.player = player_name
        self.character_name = character_name
        self.attribut = attribut
        self.description = description
        self.profile = profile