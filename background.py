import pygame
from typing import Tuple
from pycollision import Collision


class Background:

    def __init__(self, img: str, screen, pos=(0, 0), speed: float = 0.5):

        self.bg_image = pygame.image.load(img).convert_alpha()
        self.speed = speed
        self.bg_x, self.bg_y = pos
        self.screen = screen
        self.previous_x, self.previous_y = pos
        self.pre_x, self.pre_y = pos

    def update(self):
        self.screen.blit(self.bg_image, (self.bg_x, self.bg_y))

    def resetprevPos(self):
        self.pre_x, self.pre_y = self.bg_x, self.bg_y

    def getPos(self):
        return self.bg_x, self.bg_y

    def getRect(self):
        return self.bg_image.get_rect()

    def previousPos(self):
        return self.pre_x, self.pre_y

    def resetPreviousPos(self):
        self.bg_x, self.bg_y = self.previous_x, self.previous_y

    def setPos(self, pos):
        self.bg_x, self.bg_y = pos
