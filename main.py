import pygame

pygame.init()

screen=pygame.display.set_mode((800,600)) #height, width in pixels

#to open window of game:
running=True
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT: #if close button in window has been pressed
            running=False







