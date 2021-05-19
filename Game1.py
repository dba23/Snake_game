import time

import pygame

from pygame.locals import *
from Apple import Apple
from Maze import Maze
from Snake import  Snake

SIZE = 40
DX = 800
DY = 800
global GAME_SPEED
GAME_SPEED = 1

class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("ugly snake ")
        pygame.mixer.init()
        self.play_backround_music()
        self.surface = pygame.display.set_mode((DX, DY))
        self.surface.fill((255, 255, 255))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        # self.maze = Maze(self.surface)
        # self.maze.draw_maze()
        # self.maze_check = True

    def bg_pic(self):
        bg = pygame.image.load("resources/background.jpg")
        self.surface.blit(bg, (0, 0))

    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def play_backround_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()
    def increas_speed(self,current_speed):
       global GAME_SPEED
       GAME_SPEED = current_speed -0.1


    def play(self):
        self.bg_pic()
        self.snake.walk()
        self.apple.draw()

        # self.maze.draw_maze()

        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.apple.move()
            self.snake.increas_snake()
            if self.snake.length % 2 == 0:
                self.increas_speed(GAME_SPEED)
    #
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.game_over()
        for y in range(DY):
            if self.is_collision(self.snake.x[0], self.snake.y[0], 800, y):
                self.game_over()
            if self.is_collision(self.snake.x[0], self.snake.y[0], 0, y):
                self.game_over()

        for x in range(DX):
            if self.is_collision(self.snake.x[0], self.snake.y[0], x, 800):
                self.game_over()
            if self.is_collision(self.snake.x[0], self.snake.y[0], x, 0):
                self.game_over()

    def game_over(self):
        self.play_sound("crash")
        raise Exception("Game Over")


    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2  and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def display_score(self):
        font = pygame.font.SysFont("ariel",20)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (100, 0))

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.moveUp()

                    if event.key == K_DOWN:
                        self.snake.moveDown()
                    if event.key == K_LEFT:
                        self.snake.moveLeft()

                    if event.key == K_RIGHT:
                        self.snake.moveRight()
                    if event.key == K_RETURN:
                        pygame.mixer.music.play()
                        pause = False
                        self.reset_game()
                elif event.type == QUIT:
                    running = False


            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
            time.sleep(GAME_SPEED)

    def show_game_over(self):
        self.bg_pic()
        pygame.mixer.music.pause()
        self.surface.fill((0, 0, 0))
        font = pygame.font.SysFont('ariel', 40)
        line1 = font.render(f"Game Over!! your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render(f"press escape to exit , Enter to play again", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()

        pass

    def reset_game(self):
        self.snake = Snake(self.surface, 1)
        self.apple = Apple(self.surface)
        global  GAME_SPEED
        GAME_SPEED = 1
        pass
