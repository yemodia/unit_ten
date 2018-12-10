import pygame
import sys
from pygame.locals import *
import brick

GOLD = (255, 209, 63)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GREEN = (0, 102, 71)
BLUE = (0, 0, 255)
colors = [GOLD, RED, PURPLE, GREEN, BLUE]

SPACE = 5
HEIGHT = 20
number_bricks = 9


pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)
pygame.display.set_caption("Layer Bricks")


WIDTH = (500 - (number_bricks * SPACE)) / number_bricks

x = 0
y = 250 - HEIGHT

for c in range(5):
    color = colors[c]
    x = (WIDTH + SPACE) * c
    for b in range(number_bricks):
        bricks = brick.Brick(WIDTH, HEIGHT, color, mainSurface)
        bricks.create_a_brick(x, y)
        x = x + WIDTH + SPACE
        pygame.display.update()
    number_bricks = number_bricks - 2
    y = y - HEIGHT - SPACE



while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
