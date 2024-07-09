import pygame
import sys
import config as c
from level import Level
from player import Player



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HIGHT))
        pygame.display.set_caption('Gravedigger-warrior')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.tickrate = c.TICKRATE
        self.cl_dt = 0.0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                # self.player.ruch("d")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                # self.player.ruch("a")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                # self.player.ruch("w")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                # self.player.ruch("s")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # self.player.ruch("space")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                # self.player.ruch("d")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                # self.player.ruch("a")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                # self.player.ruch("s")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                # self.player.ruch("w")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                # self.player.ruch("back")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # self.player.ruch("enter")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:                    
            self.events()
            self.cl_dt += self.clock.tick()/1000
            while self.cl_dt > self.tickrate:
                self.level.run(self.cl_dt)
                self.cl_dt -= self.tickrate
                
           
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
