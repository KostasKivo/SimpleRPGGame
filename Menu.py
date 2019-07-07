import random

# 4 random events
random_events = ["Lucky in your misfortune, you found an oasis while wandering. You rested there and restored\n "
                 "your health and mana.",
                 "While trying to find your way home a snake bit you. You camped for some hours to rest. You lost\n"
                 "3 health and 2 mana",
                 "Hearing some voices in the distance you start to run, you arrive at the place but you see only some\n"
                 "skeletons.Your sanity is vanishing slowly ... You have to find your way back!",
                 "Hearing some voices in the distance you start to run, you arrive at the place and you find a better\n"
                 "sword...Someone is helping you..."]

#
random_fights = [""]


def opening_menu():
    answer = input(
        "Greetings traveller,\n"   
        "Press 1 to start game,\n"     
        "press 2 to exit\n")

    if answer == "1":
        # print("Nice one")
        return 1
    elif answer == "2":
        # print("Nice two")
        return 2


def first_encounter(player, enemy):
    print("\nWhile aimlessly walking in the desert you heard a voice\n"
          "with all the energy left you go there only to see a filthy pirate\n"
          "looking viciously at you. You have to fight him!"
          "\n")

    while enemy.enemy_health > 0 and player.player_health > 0:

        answer = fight_menu()

        if answer == "1":
            player_damage = random.randint(player.player_attack-2, player.player_attack)
            enemy_damage = random.randint(enemy.enemy_attack-2, enemy.enemy_attack)
            print(player.player_name + " attacked and dealt ", player_damage,
                  "damage.")
            print(enemy.enemy_name + " attacked and dealt ", enemy_damage, " damage.")
            player.player_health -= enemy_damage
            enemy.enemy_health -= player_damage

        elif answer == "2":
            return
        elif answer == "3":
            return

    if enemy.enemy_health <= 0:
        print(enemy.enemy_name + " fainted.\n"
                                 "You have ", player.player_health, " health.")
        return
    elif player.player_health <= 0:
        print(player.player_name + " fainted.\n "
                                   "Game over!\n\n\n\n\n\n\n")
        opening_menu()


def fight_menu():
    answer = input(
        "\nPress 1 to attack"
        "\n press 2 to use magic"
        "\n press 3 to use inventory\n")
    return answer
