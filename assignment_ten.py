import pygame, sys
from pygame.locals import *
import brick

pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)

pygame.display.set_caption("Layer Bricks")

brick = brick.Bricks(mainSurface)
brick.create_a_brick()


while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
