#/bin/python3 

import pygame

#initialize pygame
pygame.init()

#set size of screen
SS = (800, 600)
GameDisplay = pygame.display.set_mode(SS)
running = True

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


#set the title of the screen
pygame.display.set_caption('Vipy')

clock = pygame.time.Clock()

#the player, represented by a position for now
player = [SS[0]//2, SS[1]//2]

# radius of the player's circle
player_size = 40

#the speed the player can move
player_velocity = 40

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Exiting...")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player[1] -= player_velocity
        if keys[pygame.K_s]:
            player[1] += player_velocity
        if keys[pygame.K_a]:
            player[0] -= player_velocity
        if keys[pygame.K_d]:
            player[0] += player_velocity

        GameDisplay.fill(BLACK)
        pygame.draw.circle(GameDisplay, RED, player, player_size, 0)

        
        print(event)

        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()
        
