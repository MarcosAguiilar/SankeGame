import os
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15
ERROR_MOVMENT = "You can't go there"
my_position = [3,1]


while True:
    print("+" + "-" * MAP_WIDTH * 3 + "+")
    for cordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for cordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    direction = readchar.readchar()

    if direction == "w":
        if my_position[POS_Y] > 0:
            my_position[POS_Y] -= 1
        else:
            my_position[POS_Y] = MAP_HEIGHT - 1
    elif direction == "s":
        if my_position[POS_Y] < MAP_HEIGHT - 1:
            my_position[POS_Y] += 1
        else:
            my_position[POS_Y] = 0
    elif direction == "a":
        if my_position[POS_X] > 0:
            my_position[POS_X] -= 1
        else:
            my_position[POS_X] = MAP_WIDTH - 1
    elif direction == "d":
        if my_position[POS_X] < MAP_WIDTH - 1:
            my_position[POS_X] += 1
        else:
            my_position[POS_X] = 0
    elif direction == "q":
        break

    os.system("cls")



