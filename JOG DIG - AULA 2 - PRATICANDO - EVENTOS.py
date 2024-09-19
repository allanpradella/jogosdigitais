import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

tank = pygame.image.load('tanque.jpg').convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    tank_x = mouse_x - tank.get_width() // 2
    tank_y = mouse_y - tank.get_height() // 2

    screen.fill((255, 255, 255))
    screen.blit(tank, (tank_x, tank_y))

    pygame.display.update()
