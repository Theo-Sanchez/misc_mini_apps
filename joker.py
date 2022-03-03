import sys
import math
from random import randint


# w: width of the building.
# h: height of the building.

w = 1000
h = 1000
w0 = 0
h0 = 0

n = 100

bomb_coordX, bomb_coordY = (randint(0, w), randint(0, h))
print(bomb_coordX, bomb_coordY, 'coordonnée de la bombe')

x0, y0 = ((randint(0, w), randint(0, h)))
print(x0, y0, 'pos de Batman')

# game loop

for i in range(n):

    bomb_dir = ''
    # determin where the bomb is located from Batman
    if bomb_coordX > x0:
        bomb_dir += 'R'
    elif bomb_coordX < x0:
        bomb_dir += 'L'
    if bomb_coordY > y0:
        bomb_dir += 'D'
    elif bomb_coordY < y0:
        bomb_dir += 'U'
    print(f'{i} -> {bomb_dir}\n')
    # possible output (U, UR, R, DR, D, DL, L or UL)

    if 'D' in bomb_dir:
        h0 = y0
        new_y = y0 + (h - h0) / 2
    elif 'U' in bomb_dir:
        h = y0
        new_y = y0 - (h - h0) / 2
    else:
        new_y = y0
    if new_y / int(new_y) != 1:
        new_y += 0.5
    new_y = int(new_y)

    if 'L' in bomb_dir:
        w = x0
        new_x = x0 - (w - w0) / 2
    elif 'R' in bomb_dir:
        w0 = x0
        new_x = x0 + (w - w0) / 2
    else:
        new_x = x0
    if new_x / int(new_x) != 1:
        new_x += 0.5
    new_x = int(new_x)

    x0 = new_x
    y0 = new_y
    
    print(f'x: {new_x}\ny: {new_y}\n')

    if (x0, y0) == (bomb_coordX, bomb_coordY):
        print('bravo')
        break
    