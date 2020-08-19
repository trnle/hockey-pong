import pygame
from constants import BLACK
from random import randint

class Ball(pygame.sprite.Sprite):
    # this class represents the ball

    def __init__(self, color, width, height):
        # call the parent class Sprite
        super().__init__()

        # pass in the color of the ball, its position, width and height
        # set the background color to transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the ball
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 10), randint(-10, 10)]

        # get rectangle object that has image dimensions
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-10, 10)