class Player:
    player_name="Jørgen"
    player_health = 20
    player_mana = 10
    player_attack = 5
    player_bagslots = 2

    def __init__(self, name="Jørgen", health=20, mana=10, attack=5, bagslots=2):
        self.player_name = name
        self.player_health = health
        self.player_mana = mana
        self.player_attack = attack
        self.player_bagslots = bagslots
