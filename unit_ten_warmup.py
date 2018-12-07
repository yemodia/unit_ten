import pygame
import sys
from pygame.locals import *
import logo

pygame.init()
mainSurface = pygame.display.set_mode((500, 250), 0, 32)

pygame.display.set_caption("Sandy Springs Friends School")

ssfs = logo.Logo(mainSurface)
ssfs.draw_rectangle()
ssfs.draw_trellis()

while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
