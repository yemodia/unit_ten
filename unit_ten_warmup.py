import pygame, sys
from pygame.locals import *

pygame.init()
mainSurface = pygame.display.set_mode((500,500), 0, 32)
pygame.display.set_caption("Sandy Springs Friends School")

while True:
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
