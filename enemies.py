class Enemies:
    enemy_name = None
    enemy_health = 7
    enemy_attack = 3

    def __init__(self, name="Filthy Pirate", health=7, attack=3):
        self.enemy_health = health
        self.enemy_attack = attack
        self.enemy_name = name

