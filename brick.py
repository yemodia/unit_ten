import pygame


class Brick:
    def __init__(self, width, height, color, main_surface):
        """
        This function describes how a brick is made and what parameters areinvolved to create a brick
        :param width: It knows that it will include a width parameter to draw the bricks
        :param height: It knows that it will include a height parameter to draw the bricks
        :param color: It will require a color to draw a brick
        :param main_surface: The screen or display where pygame runs
        """
        self.main_surface = main_surface
        self.color = color
        self.height = height
        self.width = width

    def create_a_brick(self, x, y):
        """
        This function describes the positional arguments of the bricks
        :param x: The x coordinate of the first brick
        :param y: The y coordinate if the first brick
        :return: none
        """
        pygame.draw.rect(self.main_surface, self.color, (x, y, self.width, self.height), 0)
        pygame.display.update()