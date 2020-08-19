import pygame
from constants import WHITE

class Paddle(pygame.sprite.Sprite):
    # this class represents a paddle deriving from Sprite class in pygame

    def __init__(self, color, width, height):
        # call the parent class (Sprite) constructor
        super().__init__()

        # pass in the color of paddle, its position, width and height
        # set the background color transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # draw the paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # get the rectangle object with image dimensions
        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y -= pixels
        # check if out of bounds
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        # check if out of bounds
        if self.rect.y > 400:
            self.rect.y = 400




