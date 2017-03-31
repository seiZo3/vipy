#/bin/python3 

import pygame
from game_objects import *

#initialize pygame
pygame.init()

#set the title of the screen
pygame.display.set_caption('Vipy')

#set size of screen
SS = (800, 600)

GameDisplay = pygame.display.set_mode(SS)
running = True
entities = []

player = Player((SS[0]//2, SS[1]//2), radius=40, max_speed=5)
entities.append(player)

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    #get keys pressed
    keys = pygame.key.get_pressed()

    #get dt
    dt = clock.tick(60)

    if keys[pygame.K_w] and player.y - player.radius > 0:
        player.vely = -player.max_speed
    elif keys[pygame.K_s] and player.y + player.radius < SS[1]:
        player.vely = player.max_speed
    else:
        player.vely = 0
    
    if keys[pygame.K_w] and keys[pygame.K_s]:
        player.vely = 0
    
    if keys[pygame.K_a] and player.x - player.radius > 0:
        player.velx = -player.max_speed
    elif keys[pygame.K_d] and player.x + player.radius < SS[0]:
        player.velx = player.max_speed
    else:
        player.velx = 0
        
    if keys[pygame.K_a] and keys[pygame.K_d]:
        player.velx = 0


    #bullets
    if keys[pygame.K_i]:
        pass


    #blank the screen out
    GameDisplay.fill(BLACK)

    #update entities
    for entity in entities:
        #Update the position of the entities with their respective velocity
        entity.x += entity.velx
        entity.y += entity.vely

        entity.update(dt)

        #just draw here for now
        if entity.shape is Shape.CIRCLE:
            pygame.draw.circle(GameDisplay, entity.color, entity.pos, entity.radius, 0)
        elif entity.shape is Shape.TRIANGLE:
            pass



    pygame.display.update()

pygame.quit()
quit()
        
