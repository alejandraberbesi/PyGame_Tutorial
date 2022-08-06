import pygame
import random

pygame.init()

screen=pygame.display.set_mode((1000,667)) #width (X) ,height (Y) in pixels

#background
background=pygame.image.load('images/galaxy.jpg')

#change title and icon of game window:
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('images/monster.png')   #32 pixels
pygame.display.set_icon(icon)

#player initial config
player_img=pygame.image.load('images/spaceship.png') #128 px
player_x=436 
player_y=520
player_xchange=0

#invader initial config
enemy_img=pygame.image.load('images/alien.png') # 80 pixels
enemy_x=random.randint(0,1000) 
enemy_y=random.randint(50,150) #0 is upper limit
enemy_xchange=0.8
enemy_ychange=40

#shooting initial config
shoot_img=pygame.image.load('images/stars.png') # 32 pixels
shoot_x=0
shoot_y=520
shoot_xchange=0.8
shoot_ychange=40

def player(x,y):
    screen.blit(player_img,(x,y)) 

def enemy(x,y):
    screen.blit(enemy_img,(x,y)) 

#window of game:
running=True
while running:

    screen.fill((25,25,112)) #rgb values

    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT: #to close if close button in window has been pressed
            running=False    

        # keyboard is pressed (right or left):
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow")
                player_xchange=-1.8
            if event.key == pygame.K_RIGHT:
                print("right arrow")
                player_xchange= 1.8

        # keyboard is released
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                print("key released")
                player_xchange= 0

    #BOUNDARIES: 

    player_x+=player_xchange
    if player_x<=0:
        player_x=0
    elif player_x>=872: #spaceship image has 128 px
        player_x=872

    enemy_x+=enemy_xchange
    if enemy_x<=0:
        enemy_xchange=0.8
        enemy_y+=enemy_ychange
    elif enemy_x>=920: #invader image has 80 px
        enemy_xchange=-0.8
        enemy_y+=enemy_ychange

    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    pygame.display.update() #to update the screen (score for example)