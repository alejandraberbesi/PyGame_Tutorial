import pygame
from pygame import mixer
import random
import math

pygame.init()

screen=pygame.display.set_mode((1000,667)) #width (X) ,height (Y) in pixels

#background
background=pygame.image.load('images/galaxy.jpg')

#background sound
mixer.music.load('sounds/background.wav')
mixer.music.play(-1)
mixer.music.set_volume(0.15)

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
enemy_img=[]
enemy_x=[]
enemy_y=[]
enemy_xchange=[]
enemy_ychange=[]
num_enemies=6

for i in range(num_enemies):
    enemy_img.append(pygame.image.load('images/alien.png')) # 80 pixels
    enemy_x.append(random.randint(0,920)) 
    enemy_y.append(random.randint(50,150)) #0 is upper limit
    enemy_xchange.append(0.5)
    enemy_ychange.append(40)

#shooting initial config
shoot_img=pygame.image.load('images/stars.png') # 32 pixels
shoot_x=0
shoot_y=520
shoot_ychange=3
shoot_state="ready"  #ready: you cant see the stars in screen -- fire: stars are currently moving

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
text_x=10#where we want score to appear on screen
text_y=10

over_font=pygame.font.Font('freesansbold.ttf',100)

def show_score(x,y):
    score=font.render("Score: "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y)) 

def game_over_text():
    over_text=over_font.render("GAME OVER :(",True,(0,255,0))
    screen.blit(over_text,(160,265)) 

def player(x,y):
    screen.blit(player_img,(x,y)) 

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y)) 

def fire_stars(x,y):
    global shoot_state
    shoot_state="fire"
    screen.blit(shoot_img,(x+45,y)) #stars appears at center of spaceship

def is_collision(enemy_x,enemy_y,shoot_x,shoot_y):
    distance=math.sqrt(math.pow(enemy_x-shoot_x,2) +math.pow(enemy_y-shoot_y,2))
    if distance<27:
        return True
    else:
        return False
 
#window of game:
running=True
while running:

    screen.fill((25,25,112)) #rgb values

    screen.blit(background, (0,0)) #adding background

    for event in pygame.event.get():
        if event.type==pygame.QUIT: #to close if close button in window has been pressed
            running=False    

        # keyboard is pressed:
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow")
                player_xchange=-1.8
            if event.key == pygame.K_RIGHT:
                print("right arrow")
                player_xchange= 1.8
            if event.key == pygame.K_SPACE:
                if shoot_state=="ready":    
                    sh_sound=mixer.Sound('sounds/laser.wav')
                    sh_sound.play()
                    sh_sound.set_volume(0.2)
                    shoot_x=player_x
                    fire_stars(shoot_x,shoot_y)


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

    for i in range(num_enemies):

        if enemy_y[i]>450:
            for j in range(num_enemies):
                enemy_y[j]=2000
            game_over_text()
            break

        enemy_x[i]+=enemy_xchange[i]
        if enemy_x[i]<=0:
            enemy_xchange[i]=0.5
            enemy_y[i]+=enemy_ychange[i]
        elif enemy_x[i]>=920: #invader image has 80 px
            enemy_xchange[i]=-0.5
            enemy_y[i]+=enemy_ychange[i]
        
        collision=is_collision(enemy_x[i],enemy_y[i],shoot_x,shoot_y)
        if collision:
            explosion_sound=mixer.Sound('sounds/explosion.wav')
            explosion_sound.play()
            explosion_sound.set_volume(0.1)
            shoot_y=520
            shoot_state="ready"  
            score_value+=1
            enemy_x[i]=random.randint(0,920) 
            enemy_y[i]=random.randint(50,150) 

        enemy(enemy_x[i],enemy_y[i],i)

    #stars shooting
    if shoot_y<=0:
        shoot_y=520
        shoot_state="ready"
    if shoot_state=="fire":
        fire_stars(shoot_x,shoot_y) 
        shoot_y-=shoot_ychange

    player(player_x,player_y) 
    show_score(text_x,text_y)
    pygame.display.update() #to update the screen (score for example)