#/bin/python3 

import pygame

#initialize pygame
pygame.init()

#set size of screen
GameDisplay = pygame.display.set_mode((800,600))
running = True


#set the title of the screen
pygame.display.set_caption('Vipy')

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Exiting...")

        print(event)

        pygame.display.update()
        clock.tick(60)

pygame.quit()
quit()
        
