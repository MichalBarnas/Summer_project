import pygame
import sys
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 800))
        pygame.display.set_caption('Gravedigger-warrior')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.tickrate = 1/120.0
        self.cl_dt = 0.0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # dt = self.clock.tick() / 10000
            self.cl_dt += self.clock.tick()/1000
            while self.cl_dt > self.tickrate:
                self.level.run(self.cl_dt)
                self.cl_dt -= self.tickrate
                
           
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
