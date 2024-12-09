import os
import readchar
import random

from prompt_toolkit.key_binding.bindings.named_commands import clear_screen

POS_X = 0
POS_Y = 1

ERROR_MOVMENT = "You can't go there"
NUM_OF_MAP_OBJECTS = 10

obstacle_definition= """\
  ######################################
   ################    #################
#   ###########         ################
          ###             ##############
                               ######   
                                        
####                ##       ###########
##           #                     #####
#                         ##            
##                       ####          #
######                    ##            
###                            #####    
#            ###           #            
              #           ##        ####
#####       #####                 ######
######     #######            ##########
#######  ###########        ############
#####################      #############
########################################\
"""
end_game = False
died = False
my_position = [0,0]
tail_length = 0
tail = []
map_objects = []

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

#main loop
while not end_game:
    # generacion de objetos
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
        if new_position not in map_objects and new_position != my_position:
            map_objects.append(new_position)

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):

            char_to_draw = " "

            tail_in_position = None

            for objects in map_objects:
                if objects[POS_X] == cordinate_x and objects[POS_Y] == cordinate_y:
                    if objects[POS_X] == my_position[POS_X] and objects[POS_Y] == my_position[POS_Y]:
                        map_objects.remove(objects)
                        tail_length += 1
                        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
                        if new_position not in map_objects and new_position != my_position:
                            map_objects.append(new_position)
                    else:
                        char_to_draw = "*"

            for tails in tail:
                if tails[POS_X] == cordinate_x and tails[POS_Y] == cordinate_y:
                    char_to_draw = "@"
                    tail_in_position = tails


            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"

                if tail_in_position:
                    died = True
                    end_game = True

            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                char_to_draw = "#"

            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()

    if direction == "w" or direction == "W":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        if my_position[POS_Y] > 0:
            my_position[POS_Y] -= 1
        else:
            my_position[POS_Y] = MAP_HEIGHT - 1
    elif direction == "s" or direction == "S":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        if my_position[POS_Y] < MAP_HEIGHT - 1:
            my_position[POS_Y] += 1
        else:
            my_position[POS_Y] = 0
    elif direction == "a" or direction == "A":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        if my_position[POS_X] > 0:
            my_position[POS_X] -= 1
        else:
            my_position[POS_X] = MAP_WIDTH - 1
    elif direction == "d" or direction == "D":
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        if my_position[POS_X] < MAP_WIDTH - 1:
            my_position[POS_X] += 1
        else:
            my_position[POS_X] = 0
    elif direction == "q" or direction == "Q":
        end_game = True

    os.system("cls")

    if died:
        print("\n" * 100)  # Desplaza el texto hacia abajo
        print(" " * 20 + "¡¡¡Estas muerto!!!")
        print("\n" * 5)  # Espacio al final


