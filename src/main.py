#/bin/python3 

import pygame

#initialize pygame
pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

#set size of screen
SS = (800, 600)


class Entity(object):
    def __init__(self, x, y, radius=10, color=RED):
        self.x = x
        self.y = y
        self.color = color
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val

    @property
    def speed(self):
        return 5

    @property
    def pos(self):
        return (self.x, self.y)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, val):
        self.__color = val

    @property
    def radius(self):
        return self.__radius


GameDisplay = pygame.display.set_mode(SS)
running = True


player = Entity(SS[0]//2, SS[1]//2, radius=40, color=RED)

#set the title of the screen
pygame.display.set_caption('Vipy')

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    #get keys pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player.y - player.radius > 0:
        player.y -= player.speed
    if keys[pygame.K_s] and player.y + player.radius < SS[1]:
        player.y += player.speed
    if keys[pygame.K_a] and player.x - player.radius > 0:
        player.x -= player.speed
    if keys[pygame.K_d] and player.x + player.radius < SS[0]:
        player.x += player.speed

    #bullets
    if keys[pygame.K_i]:
        pass

    GameDisplay.fill(BLACK)
    pygame.draw.circle(GameDisplay, player.color, player.pos, player.radius, 0)
        

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
        
