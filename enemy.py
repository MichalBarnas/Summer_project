import pygame
import time


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((64, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=pos)
