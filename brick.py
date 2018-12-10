import pygame

class Brick:
    def __init__(self, width, height, color, main_surface):
        self.main_surface = main_surface
        self.color = color
        self.height = height
        self.width = width

    def create_a_brick(self, x, y):
        pygame.draw.rect(self.main_surface, self.color, (x, y, self.width, self.height), 0)
        pygame.display.update()
    