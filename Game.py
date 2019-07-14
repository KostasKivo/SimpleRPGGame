from Menu import *
from Player import *
from Enemies import *

answer = opening_menu()

if answer == 1:
    print(""
          "\nJørgen, while protecting important cargo for the queen\n"
          "pirates attacked your ship and crew. You wake up\n"
          "with a sword in your hand , not knowing where you\n"
          "are, trying to find your way home ... \n")

    player = Player()

    day_num = 1
    moves_num = 0

    while day_num < 5:

        moves_num = 0
        print("DAY ", day_num)

        print("--------------------------------------------\n")

        if day_num == 1:
            print("\nWhile aimlessly walking in the desert you heard a voice\n"
                  "with all the energy left you go there only to see a filthy pirate\n"
                  "looking viciously at you. You have to fight him!"
                  "\n")
            first_enemy = Enemies()
            enemy_encounter(player, first_enemy)
            moves_num += 1

        while moves_num < 4:
            '''
            Generate a random number between 0,1 
            If it's less than 0,5 spawn a random event
            If it's more or equal than 0,5 spawn a random fight
            '''
            day_event = random.uniform(0, 1)
            random_day_event = random.randint(0, len(random_events) - 1)
            events_chooser(day_event, random_day_event, player)
            moves_num += 1

        day_num += 1

    print("After this big adventure , you finally found your way home.\n"
          "You see the castle in the distance and tears start streaming from your face.\n"
          "Your adventure is finally over..\n")
    end = input()


elif answer == 2:
    quit()
