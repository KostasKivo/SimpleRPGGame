import random
from Enemies import *
import sys

# 4 random events
random_events = ["Lucky in your misfortune, you found an oasis while wandering. You rested there and restored\n "
                 "your health and mana.\n",
                 "While trying to find your way home a snake bit you. You camped for some hours to rest. You lost\n"
                 "3 health and 2 mana\n",
                 "Hearing some voices in the distance you start to run, you arrive at the place but you see only some\n"
                 "skeletons.Your sanity is vanishing slsowly ... You have to find your way back!\n",
                 "Hearing some voices in the distance you start to run, you arrive at the place and you find a better\n"
                 "sword...Someone is helping you...\n"]

# 4 random events
random_fights = ["In the distance you see a bulky pirate , you gather your remaining strength to seem as intimidating\n"
                 "as possible.\n",
                 "You hear a wounded pirate resting on a tree , a perfect timing for an ambush...\n",
                 "An arrow just passes your head , wounding your ear , you take out your sword as fast as possible\n"
                 "and rush your enemy.\n",
                 "While grunting from your exhaustion you hear someone approach you from the back, you see a filthy \n"
                 "pirate ready for a fight.\n"]


def opening_menu():
    answer = input(
        "\nGreetings traveller,\n"   
        "Press 1 to start game,\n"     
        "press 2 to exit\n")

    if answer == "1":
        # print("Nice one")
        return 1
    elif answer == "2":
        # print("Nice two")
        return 2


def enemy_encounter(player, enemy):

    while enemy.enemy_health > 0 and player.player_health > 0:

        answer = fight_menu()

        if answer == "1":
            damage_phase(player, enemy, "p")
        elif answer == "2":

            answer = spell_menu()

            if int(answer) == 1 and player.player_mana >= 3:
                player.player_mana -= 3
                damage_phase(player, enemy, "s")
            elif int(answer) == 2 and player.player_mana >= 2:
                player.player_mana -= 2
                damage_phase(player, enemy, "s")
            elif int(answer) == 3 and player.player_mana >= 1:
                player.player_mana -= 1
                damage_phase(player, enemy, "h")
            else:
                print("Not enough mana!\n")

    if enemy.enemy_health <= 0:
        print(enemy.enemy_name + " fainted.\n"
                                 "You have ", player.player_health, " health.\n")
        return
    elif player.player_health <= 0:
        print(player.player_name + " fainted.\n "
                                   "Game over!\n\n\n\n\n\n\n\n\n")
        opening_menu()


def fight_menu():
    answer = input(
        "Press 1 to attack"
        "\n press 2 to use magic\n")
    return answer


def events_chooser(event_float, event_num, player):
    if event_float < 0.5:

        if event_num == 0:
            print(random_events[event_num])
            player.player_health += 20
            player.player_mana += 10
            print("--------------------------------------------\n")
        elif event_num == 1:
            print(random_events[event_num])
            player.player_health -= 3
            player.player_mana -= 2
            print("--------------------------------------------\n")
            player_has_died(player)
        elif event_num == 2:
            print(random_events[event_num])
            print("--------------------------------------------\n")
        elif event_num == 3:
            print(random_events[event_num])
            player.player_attack += 2
            print("--------------------------------------------\n")

    elif event_float >= 0.5:

        if event_num == 0:
            print(random_fights[event_num])
            enemy = Enemies("Bulky Pirate", 10, 5)
            enemy_encounter(player, enemy)
            print("--------------------------------------------\n")
        elif event_num == 1:
            print(random_fights[event_num])
            enemy = Enemies("Ambushing Pirate", 5, 7)
            enemy_encounter(player, enemy)
            print("--------------------------------------------\n")
        elif event_num == 2:
            print(random_fights[event_num])
            enemy = Enemies("Ambushing Pirate", 5, 7)
            enemy_encounter(player, enemy)
            print("--------------------------------------------\n")
        elif event_num == 3:
            print(random_fights[event_num])
            enemy = Enemies("Scared Pirate", 5, 3)
            enemy_encounter(player, enemy)
            print("--------------------------------------------\n")


def player_has_died(player):
    if player.player_health <= 0:
        print(player.player_name + " fainted.\n ")
        sys.exit("Game over!\n\n\n\n\n\n\n")


def spell_menu():
    answer = input(
        "Press 1 for fireball, costs 3 mana"
        "\n Press 2 for ice crystals, costs 2 mana"
        "\n Rress 3 to heal, costs 1 mana\n")
    return answer


def damage_phase(player, enemy, damage_type_string):

    player_damage = None
    damage_overview = None

    if damage_type_string == "p":
        player_damage = random.randint(player.player_attack - 2, player.player_attack)
        damage_overview = "{} attacked and dealt {} damage."
    elif damage_type_string == "s":
        player_damage = random.randint(player.player_magic_attack - 2, player.player_magic_attack)
        damage_overview = "{} attacked and dealt {} damage."
    elif damage_type_string == "h":
        player_heal = random.randint(player.player_health, 20)

        if player.player_health >= 20:
            damage_overview = "{} already had max health."
            print(damage_overview.format(player.player_name))

            # Not the best solution
            enemy_damage = random.randint(enemy.enemy_attack - 2, enemy.enemy_attack)
            print(enemy.enemy_name + " attacked and dealt ", enemy_damage, " damage.\n")
            player.player_health -= enemy_damage
            return

        elif player.player_health < 20:
            damage_overview = "{} healed for {} points of health.\n"
            print(damage_overview.format(player.player_name, player_heal))

            # Not the best solution
            enemy_damage = random.randint(enemy.enemy_attack - 2, enemy.enemy_attack)
            print(enemy.enemy_name + " attacked and dealt ", enemy_damage, " damage.\n")
            player.player_health -= enemy_damage
            return

    enemy_damage = random.randint(enemy.enemy_attack - 2, enemy.enemy_attack)
    print(damage_overview.format(player.player_name, player_damage))
    print(enemy.enemy_name + " attacked and dealt ", enemy_damage, " damage.\n")
    player.player_health -= enemy_damage
    enemy.enemy_health -= player_damage
