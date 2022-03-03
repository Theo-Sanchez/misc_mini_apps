import sys
import math
from random import randint
from types import SimpleNamespace

# #slope


# # w: width of the building.
# # h: height of the building.
# w, h = [int(i) for i in input().split()]
w, h = (50, 50)

# # n: maximum number of turns before game over.
# # n = int(input())  
n = 20

# # x0, y0 = [int(i) for i in input().split()]
w0, h0 = 0, 0
# history = []
# dichotomia = 0

bomb_coordX, bomb_coordY = (randint(0, w), randint(0, h))
print(f'({bomb_coordX}, {bomb_coordY}) coordonnée de la bombe')

x0, y0 = ((randint(0, w), randint(0, h)))
print(f'({x0}, {y0}) coordonnée de Batman')

# def get_dist(x, y):
#     return math.sqrt((bomb_coordX - x)**2 + (bomb_coordY - y)**2)

# # To debug: print("Debug messages...", file=sys.stderr, flush=True)

# # game loop
# for i in range(n):
#     # bomb_dir = input()  # Current distance to the bomb compared to previous distance
#     # (COLDER, WARMER, SAME or UNKNOWN)
# AB = math.sqrt((x_batman - x_bomb)**2 + (y_batman - y_bomb)**2)

class Batman:
    def __init__(self, x, y, h, w):
        self.x = x #[x, 0]
        self.y = y # [y, 0]
        self.h = h  # [h, 0]
        self.w = w # [w, 0]

        self.history = []
        self.h0 = 0 # [0, 0]
        self.w0 = 0 # [0, 0]
        self.gap = 0
        self.dist = 0
        # pas oublier de recall dist
        self.dir = ''
        self.temp = ''
        self.slope = False
        self.end = False
        self.wait = False


    def where_to_move(self):

        hist = SimpleNamespace(**self.history[-1])

        if self.temp == 'same':
            if self.dir[1]:
                self.x = self.x + hist.x / 2
                self.y = self.y + hist.y / 2
                self.end = True
                # fin du jeu ?
            else:
                self.x = self.x + hist.x / 2
                # pas besoin d'ajuster la grille
                self.first_move(**{'y': self.y, 'h0': self.h0, 'h': self.h})

        else:
            if self.temp == 'unknown':
                self.dir = tuple([-i for i in hist.dir])
                self.moving(is_double=self.slope)
            # self.slope = self.temp == 'colder'
            if self.temp == 'colder':
                self.adjust_grid()
                self.wait = True # à chier mais temporaire
                self.moving(is_double=self.slope)
            else:
                self.adjust_grid()
                self.dir = tuple([-i for i in hist.dir])
                self.moving(is_double=self.slope)


    def first_move(self, **args):
        # mouvement sur la plus grande distance sur l'axe

        self.calc_dist()
        if args:
            args = SimpleNamespace(**args)
            if args.y - args.h0 > args.h - args.y:
                self.dir = (0, -1)
            else:
                self.dir = (0, 1)
        else:
            if self.x - self.w0 > self.w - self.x:
                self.dir = (-1, 0)
            else:
                self.dir = (1, 0)
        self.moving(is_double=self.slope)

    def calc_dist(self):
        print('calcdist', 'x:', self.x, 'y:', self.y)
        self.dist = math.sqrt((bomb_coordX - self.x)**2 + (bomb_coordY - self.y)**2)
        print(self.dist)


    def adjust_grid(self):

        hist = SimpleNamespace(**self.history[-1])
        gap = hist.gap / 2
        isInt = gap == hist.gap // 2
        gap = int(gap) if isInt else int(gap) + 1

        if not self.slope:
            if self.dir[0] == -1: # on vient de bouger à gauche
                if self.temp == 'warmer':
                    self.w = hist.w - gap
                else:
                    self.w0 = hist.w0 + gap

            elif self.dir[0] == 1: # on vient de bouger à droite
                if self.temp == 'warmer':
                    self.w0 = hist.w0 + gap
                else:
                    self.w = hist.w - gap

            elif self.dir[1] == -1: # on vient de bouger en haut
                if self.temp == 'warmer':
                    self.h = hist.h - gap
                else:
                    self.h0 = hist.w0 + gap

            elif self.dir[1] == 1: # on vient de bouger en bas
                if self.temp == 'warmer':
                    self.h0 = hist.w0 + gap
                else:
                    self.h = hist.h - gap
        else:
            print('problemosssssssssssssss')
            pass


    def moving(self, is_double=False):

        y_adjust = 0, 0


        # vérifier qu'on fait ça avant de changer la grille
        if self.dir[0]:
            if is_double:
                if self.y != h0:
                    y_adjust = -1
                elif self.y != h:
                    y_adjust = 1
                new_y = self.y + y_adjust

            else:
                new_y = self.y
            if self.dir[0] == -1: # left
                x_move = self.x - self.w0
            elif self.dir[0] == 1: # right
                x_move = self.w - self.x
            if self.wait:
                x_move = self.history[-1]['gap']
            new_x = self.x + x_move * self.dir[0]
            self.gap = x_move

        elif self.dir[1]:
            new_x = self.x
            if self.dir[1] == -1: # up
                y_move = self.y - self.h0
            elif self.dir[1] == 1: # down
                y_move = self.h - self.y
            new_y = self.y + y_move * self.dir[1]
            if self.wait:
                y_move = self.history[-1]['gap']
            self.gap = y_move

        self.x = new_x
        self.y = new_y

    def remember(self, i):
        
        self.history += [{
            'x': self.x,
            'y': self.y,
            'dist': self.dist,
            'h0': self.h0,
            'h': self.h,
            'w0': self.w0,
            'w': self.w,
            'dir': self.dir,
            'gap': self.gap,
            'temp': self.temp,
            'slope': self.slope
        }]
        print(self.history[i], i)


    def dist_to_temp(self):

        hist = SimpleNamespace(**self.history[-1])
        if self.wait:
            self.temp = 'unknown'
            self.wait = False
        else:
            if self.dist > hist.dist:
                self.temp = 'colder'
            elif self.dist < hist.dist:
                self.temp = 'warmer'
            else:
                self.temp = 'same'

# batman = Batman(x0, y0, h, w)
# print(vars(batman), 'test') # .__dict__
# batman.first_move()

# batman.moving(False)
# recoucou = 23
# batman.remember()
# batman.calc_dist()
# batman.remember()
# print(batman.history)
n = 3
batman = Batman(x0, y0, h, w)

for i in range(n):
    if batman.end:
        print(batman.x, batman.y, 'test')
    else:
        if i == 0:
            batman.first_move()
        else:
        #     if batman.wait:
        #         pass
        #     else:
            batman.calc_dist()
            batman.dist_to_temp()
            batman.where_to_move()
    batman.remember(i)
