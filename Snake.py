import pygame

SIZE = 40
DX = 800
DY = 800

class Snake:
    def __init__(self, parent_screen , length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = "down"

    def moveUp(self):
        self.direction = "up"

    def moveDown(self):
        self.direction = "down"

    def moveLeft(self):
        self.direction = "left"

    def moveRight(self):
        self.direction = "right"

    def grow(self):
        self.length +=1

    def draw(self):
        # self.parent_screen.fill((255, 255, 255))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def walk(self):
        for i in range((self.length - 1), 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == "up":
            self.y[0] -= SIZE
            self.draw()

        if self.direction == "down":
            self.y[0] += SIZE
            self.draw()

        if self.direction == "left":
            self.x[0] -= SIZE
            self.draw()

        if self.direction == "right":
            self.x[0] += SIZE
            self.draw()

        self.draw()
    def increas_snake(self):
        self.length += 1
        self.x.append(1)
        self.y.append(1)

