import pygame

pygame.init()

screen=pygame.display.set_mode((800,600))
running=True

#title
pygame.display.set_caption("Space invaders")

playerimg=pygame.image.load("space-ship.png")
playerx=370
playery=480
playerxchange=0

def player(playerx,playery):
    screen.blit(playerimg,(playerx,playery))

while running:
     #background
    screen.fill((0,255,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerxchange=-0.3
            if event.key==pygame.K_RIGHT:
                playerxchange=0.3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerxchange=0

            

            
   
    
   
    playerx+=playerxchange
    player(playerx,playery)
    pygame.display.update()
