import os
import readchar
import random

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
ERROR_MOVMENT = "You can't go there"
NUM_OF_MAP_OBJECTS = 10
my_position = [0,0]
map_objects = []

#generacion de objetos
while len(map_objects) < NUM_OF_MAP_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
    if new_position not in map_objects and new_position != my_position:
        map_objects.append(new_position)



#main loop
while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for cordinate_x in range(MAP_WIDTH):

            char_to_draw = " "

            for objects in map_objects:
                if objects[POS_X] == cordinate_x and objects[POS_Y] == cordinate_y:
                    if objects[POS_X] == my_position[POS_X] and objects[POS_Y] == my_position[POS_Y]:
                        map_objects.remove(objects)
                    else:
                        char_to_draw = "*"


            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = "@"

            print(" {} ".format(char_to_draw), end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()

    if direction == "w" or direction == "W":
        if my_position[POS_Y] > 0:
            my_position[POS_Y] -= 1
        else:
            my_position[POS_Y] = MAP_HEIGHT - 1
    elif direction == "s" or direction == "S":
        if my_position[POS_Y] < MAP_HEIGHT - 1:
            my_position[POS_Y] += 1
        else:
            my_position[POS_Y] = 0
    elif direction == "a" or direction == "A":
        if my_position[POS_X] > 0:
            my_position[POS_X] -= 1
        else:
            my_position[POS_X] = MAP_WIDTH - 1
    elif direction == "d" or direction == "D":
        if my_position[POS_X] < MAP_WIDTH - 1:
            my_position[POS_X] += 1
        else:
            my_position[POS_X] = 0
    elif direction == "q" or direction == "Q":
        break

    os.system("cls")



