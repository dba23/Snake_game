import pygame
import time

import random as rd
SIZE = 40
DX = 800
DY = 800



class Apple :
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y =SIZE*3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = rd.randint(0,12)*SIZE
        self.y = rd.randint(0,12)*SIZE
