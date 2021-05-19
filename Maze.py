import pygame
import random
SIZE = 40
DX = 800
DY = 800


class Maze:

    def __init__(self, parent_screen):

        self.brick_pic = pygame.image.load("resources/img_3.png")
        self.x = SIZE*4
        self.y = SIZE*4
        self.parent_screen = parent_screen

    def draw_maze(self):
        last_rand_y = 0
        last_rand_x = 0

        for i in range(10):
            self.x = random.randint(0, 8) * 100

            self.y = random.randint(0, 8) * 100
            if self.x == last_rand_x:
                self.x = random.randint(0, 8) * 100
            elif self.y == last_rand_y:
                self.y = random.randint(0, 8) * 100
            else:
                self.parent_screen.blit(self.brick_pic, (self.x, self.y))

            last_rand_x = self.x
            last_rand_y = self.y
            pygame.display.flip()
