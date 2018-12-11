# Yerim Dia
# Introduction to Computer Science
# December 11, 2018
# This program is a way of drawing with Pygame
# The purpose of the program was to draw different rows of bricks with each row a different color and the next row has
#  2 less bricks than the previous one.


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
mainSurface.fill((178, 34, 34))
pygame.display.set_caption("Layer Bricks")


WIDTH = (500 - (number_bricks * SPACE)) / number_bricks
# This allows the bricks to evenly fit in the window

x = 0
y = 250 - HEIGHT

for c in range(5):
    color = colors[c]
    x = (WIDTH + SPACE) * c  # Sets the indented x position for new brick after each row
    for b in range(number_bricks):
        bricks = brick.Brick(WIDTH, HEIGHT, color, mainSurface)
        bricks.create_a_brick(x, y)
        x = x + WIDTH + SPACE  # Sets the next brick in a row

        pygame.display.update()
    number_bricks = number_bricks - 2  # each line of brick has 2 less bricks than previous
    y = y - HEIGHT - SPACE  # Sets y coordinate for each brick on next row

while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
