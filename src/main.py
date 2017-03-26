#/bin/python3 

import pygame

#initialize pygame
pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#set size of screen
SS = (800, 600)


class Player():
    def __init__(self, x, y, color = RED):
        self.x = x
        self.y = y
        self.color = color

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if val < 0:
            self.__x = 0
        else:
            self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if val < 0:
            self.__y = 0
        else:
            self.__y = val

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, val):
        self.__color = val

    @property
    def radius(self):
        return 40

    @property
    def velocity(self):
        return 5

    @property
    def pos(self):
        return (self.x, self.y)


GameDisplay = pygame.display.set_mode(SS)
running = True


player = Player(SS[0]//2, SS[1]//2)

#set the title of the screen
pygame.display.set_caption('Vipy')

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print(event)
            print("Exiting...")
    

    #get keys pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player.y - player.radius > 0:
        player.y -= player.velocity
    if keys[pygame.K_s] and player.y + player.radius < SS[1]:
        player.y += player.velocity
    if keys[pygame.K_a] and player.x - player.radius > 0:
        player.x -= player.velocity
    if keys[pygame.K_d] and player.x + player.radius < SS[0]:
        player.x += player.velocity

    GameDisplay.fill(BLACK)
    pygame.draw.circle(GameDisplay, player.color, player.pos, player.radius, 0)
        

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
        
