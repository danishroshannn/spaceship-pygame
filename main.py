import pygame
import random

pygame.init()

screen=pygame.display.set_mode((800,600))
running=True

#title
pygame.display.set_caption("Space invaders")

playerimg=pygame.image.load("space-ship.png")
playerx=370
playery=480
playerxchange=0

#enemy
enemyimg=pygame.image.load("enemy.png")
enemyx=random.randint(0,800)
enemyy=random.randint(50,150)
enemyxchange=0

def player(playerx,playery):
    screen.blit(playerimg,(playerx,playery))

def enemy(enemyx,enemyy):
    screen.blit(enemyimg,(enemyx,enemyy))

while running:
     #background
    screen.fill((0,255,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
 #playermovement
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerxchange=-0.3
            if event.key==pygame.K_RIGHT:
                playerxchange=0.3
       # if event.type==pygame.KEYUP:
        #    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
         #       playerxchange=0


    #boundary
    playerx+=playerxchange
    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736


    player(playerx,playery)
    enemy(enemyx,enemyy)
    pygame.display.update()
