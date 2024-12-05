import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3,1]


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

direccion = input("Donde te quieres mover? [WASD]:")
direction = readchar.readchar()

