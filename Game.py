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
        print("DAY ", day_num, "\n")

        if day_num == 1:
            first_enemy = Enemies()
            first_encounter(player, first_enemy)
            moves_num += 1

        while moves_num < 4:
            '''
            Generate a random number between 0,1 
            If it's less than 0,5 spawn a random event
            If it's more or equal than 0,5 spawn a random fight
            '''
            day_event = random.uniform(0, 1)
            print(day_event)
            moves_num += 1

        day_num += 1


elif answer == 2:
    quit()
