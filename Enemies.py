class Enemies:
    enemy_name = None
    enemy_health = 7
    enemy_attack = 3
    enemy_mana = 10

    def __init__(self, name="Filthy Pirate", health=7, attack=3, mana=10):
        self.enemy_health = health
        self.enemy_mana = mana
        self.enemy_attack = attack
        self.enemy_name = name

