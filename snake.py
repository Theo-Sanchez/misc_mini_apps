#             if direction == 'up':
#                 snake_move_y -= 10            MEMOIRE ANCIENNE STRAT A CHIER
#             elif direction == 'down':
#                 snake_move_y += 10
#             elif direction == 'left':
#                 snake_move_x -= 10
#             elif direction == 'right':
#                 snake_move_x += 10

    # randNumLabel = myFont.render("You score is:", 1, white)           AFFICHAGE SCORE CHANTIER
    # diceDisplay = myFont.render(str(stack), 1, white)
    # dis.blit(randNumLabel, (100, 100))
    # dis.blit(diceDisplay, (100, 140))
# score_display = myFont.render(str(stack), 1, (255 ,255 ,0))


#AJOUTER key.event == K_ESC :
    # pause?
#Encore un probleme de baies qui sortent de l'écran ??
# possible de transfo snake_body_pos en ['up':4, 'left':2, 'up':1, 'right':6...]

import pygame
import time
from random import randint

WINDOW_WIDTH = 300
WINDOW_HEIGTH = 400

window_range = (WINDOW_WIDTH , WINDOW_HEIGTH)

close = False
replay = True

green = (0, 255, 0) #mettre dans un dict?
black = (0, 0, 0)
red = (255, 0, 0)
moche = (100, 100, 100)
white = (255, 255, 255)

snake_move_x = 0
snake_move_y = 0
snake_pos_x = 200
snake_pos_y = 150

snake_img_by_position = {
'up': ['lienversimage_head_up', 'lienversimage_body_up'],
'down': ['lienversimage_head_down', 'lienversimage_body_down'],
'left': ['lienversimage_head_left', 'lienversimage_body_left'],
'right': ['lienversimage_head_right', 'lienversimage_body_right']
}
testing = True

stack = 1
snake_body_pos = []
dir_body = ['left',]
snake = (snake_pos_x,snake_pos_y) 
direction = 'left'
dis = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption('Snake game')

pygame.init()
myFont = pygame.font.SysFont("Times New Roman", 18)

clock = pygame.time.Clock()
dot_pos_x = 10* randint(0,int(WINDOW_WIDTH / 10))
dot_pos_y = 10* randint(0,int(WINDOW_HEIGTH / 10))


snake_head_up = pygame.image.load('./img/snake_head_up')
snake_head_down = pygame.image.load('./img/snake_head_minsize') # à changer
snake_head_left = pygame.image.load('./img/snake_head_left')
snake_head_right = pygame.image.load('./img/snake_head_right')

snake_body_straight =pygame.image.load('./img/snake_body_straight') # faudra check les noms des images
snake_body_side = pygame.image.load('./img/snake_body_side')
snake_upleft = pygame.image.load('./img/snake_upleft')
snake_upright = pygame.image.load('./img/snake_upright')
snake_botleft = pygame.image.load('./img/snake_botleft')
snake_botright = pygame.image.load('./img/snake_botright')


snake_heading = {
    'up' : snake_head_up,
    'down' : snake_head_down,
    'left' : snake_head_left,
    'right' : snake_head_right
}

snake_body = {
    'up' : snake_body_straight,
    'down' : snake_body_straight,
    'left' : snake_body_side,
    'right' : snake_body_side,
    'upleft' : snake_upleft,
    'upright' : snake_upright,
    'botleft' : snake_botleft,
    'botright' : snake_botright
}

move_size = 10 # à inplémenter après pour le déplacement varibale.



def sssnake(snake_body_pos, dir_body):

    dis.blit(snake_heading[dir_body[-1]], (snake_body_pos[-1][0], snake_body_pos[-1][1]))

    for i in range(1, len(snake_body_pos)-1):

        if dir_body[i] == dir_body[i-1]:
            dis.blit(snake_body[dir_body[i-1]], (snake_body_pos[i-1][0], snake_body_pos[i-1][1]))

        if (dir_body[i-1],dir_body[i]) == ('right', 'bottom') or ('up', 'left'):
            dis.blit(snake_body['upright'], (snake_body_pos[i-1][0], snake_body_pos[i-1][1]))

        if (dir_body[i-1],dir_body[i]) == ('left', 'bottom') or ('up', 'right'):
            dis.blit(snake_body['upleft'], (snake_body_pos[i-1][0], snake_body_pos[i-1][1]))
            
        if (dir_body[i-1],dir_body[i]) == ('right', 'up') or ('bottom', 'left'):
            dis.blit(snake_body['botright'], (snake_body_pos[i-1][0], snake_body_pos[i-1][1]))

        if (dir_body[i-1],dir_body[i]) == ('left', 'up') or ('bottom', 'right'):
            dis.blit(snake_body['botleft'], (snake_body_pos[i-1][0], snake_body_pos[i-1][1]))

    


x = (WINDOW_WIDTH * 0.45)
y = (WINDOW_HEIGTH * 0.8)


while not close:
# while replay:
    clock.tick(30)
    dot_pos = (dot_pos_x, dot_pos_y)
    snake_pos_x += snake_move_x
    snake_pos_y += snake_move_y
    print(dir_body)
    snake_body_pos.append([snake_pos_x, snake_pos_y])
    dir_body.append(direction)

    while len(snake_body_pos) > stack:
        snake_body_pos.pop(0)
    while len(dir_body) > stack:
        dir_body.pop(0)
    snake = (snake_pos_x, snake_pos_y)
    
    if snake[0] > WINDOW_WIDTH:      # pas fou try >=? mais tjr pas fou. Pourquoi ? 
        snake_pos_x -= WINDOW_WIDTH
    if snake[0] < 0:
        snake_pos_x += WINDOW_WIDTH
    if snake[1] > WINDOW_HEIGTH:
        snake_pos_y -= WINDOW_HEIGTH
    if snake[1] < 0:
        snake_pos_y += WINDOW_HEIGTH

    if [snake[0], snake[1]] in snake_body_pos[:-1]: 
        print((snake[0], snake[1]), snake_body_pos, "PROBLEMOS ?" )
        # ajoùter plein de trucs
        close = True

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            close=True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != 'down':
                snake_move_x = 0
                snake_move_y = -5
                direction = 'up'

            elif event.key == pygame.K_DOWN and direction != 'up':
                snake_move_x = 0
                snake_move_y = 5
                direction = 'down'

            elif event.key == pygame.K_LEFT and direction != 'right':
                snake_move_x = -5 
                snake_move_y = 0
                direction = 'left'

            elif event.key == pygame.K_RIGHT and direction != 'left':
                snake_move_x = 5
                snake_move_y = 0    
                direction = 'right'

            if testing and event.key == pygame.K_z: # testing_part
                snake_move_x = 0
                snake_move_y = 0
    
    if dot_pos_x > WINDOW_WIDTH or dot_pos_x < 0:
        dot_pos_x = 10*randint(0, int((WINDOW_WIDTH-1)/10)) - 10
    if dot_pos_y > WINDOW_HEIGTH or dot_pos_y < 0:
        dot_pos_y = 10*randint(0, int((WINDOW_HEIGTH-1)/10)) - 10

    if (snake[0],snake[1]) == dot_pos:
        if testing:
            if direction == 'up':
                dot_pos_x -= 15
            elif direction == 'down':
                dot_pos_x += 15
            elif direction == 'right':
                dot_pos_x += 15
            elif direction == 'left':
                dot_pos_x -= 15
        else:
            dot_pos_x = 10*randint(0, int((WINDOW_WIDTH-1)/10)) - 10
            dot_pos_y = 10*randint(0, int((WINDOW_HEIGTH-1)/10)) - 10
        stack +=1
    



    # print((snake[0], snake[1]), snake_body_pos) # test
    
    
    dis.fill(black)
    # sssnake(snake_body_pos, dir_body)
    offset = len(str(stack))
    score_display = myFont.render(str(stack-1), 1, white)
    dis.blit(score_display, (WINDOW_WIDTH-(10*offset), 10))
    # dir_body.append(direction)
    
    for i in range (stack):
        pygame.draw.rect(surface=dis, color=green, rect=[snake_body_pos[i-1][0], snake_body_pos[i-1][1], 5, 5], border_radius=10) # à changer avec snake_body_pos.img
    pygame.draw.rect(surface=dis, color=red, rect=[snake_body_pos[-1][0], snake_body_pos[-1][1], 5, 5], border_radius=10) # à changer avec snake_head.img


    # pygame.draw.rect(surface=dis, moche, rect=[dot_pos_x,dot_pos_y,5,5])
    pygame.draw.rect(surface=dis, color=moche, rect=[dot_pos_x,dot_pos_y,5,5])
    
    # pygame.display.flip()         # CHECK LA NUANCE ? 
    pygame.display.update() 
        
quit()




# gameDisplay.fill(white)
