#/bin/python3 

import pygame
import random
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
enemySpawnChance = 60
enemySpeedRange = (2, 4)

SPAWN_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY, 3000)

player = Player((SS[0]*0.5, SS[1]*0.5), radius=40, max_speed=5)
entities.append(player)


clock = pygame.time.Clock()


def generateSpawnPos(entity, ss):
    """Selects a random position at the edge of the screen for the enemey to spawn at"""
    horizontal_edge = random.randrange(entity.radius, ss[0] - entity.radius, entity.radius*2)
    vertical_edge = random.randrange(entity.radius, ss[1] - entity.radius, entity.radius*2)
    edge = random.randrange(0, 4)

    valid_pos = {
        0: (horizontal_edge, -entity.radius),
        1: (ss[0] + entity.radius, vertical_edge),
        2: (horizontal_edge, ss[1] + entity.radius),
        3: (-entity.radius, vertical_edge)
    }
    return valid_pos[edge]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_ENEMY:
            #check and see if we will spawn an enemy on this interval
            if random.randrange(0, 100) > (100 - enemySpawnChance):
                max_speed = random.randrange(enemySpeedRange[0],
                                             enemySpeedRange[1])
                enemy = Enemy(radius=30,
                              max_speed=max_speed)
                enemy.pos = generateSpawnPos(enemy, SS)
                entities.append(enemy)
                

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

        if isinstance(entity, Enemy):
            entity.update(dt, player.pos)
        else:
            entity.update(dt)


        #just draw here for now
        if entity.shape is Shape.CIRCLE:
            pygame.draw.circle(GameDisplay,
                               entity.color,
                               (math.floor(entity.x), math.floor(entity.y)),
                               entity.radius,
                               0)
        elif entity.shape is Shape.TRIANGLE:
            pass



    pygame.display.update()

pygame.quit()
