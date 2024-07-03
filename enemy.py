import pygame
import time
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.stats = [3,3,3,3,3,3]
        self.image = pygame.Surface((64, 64))
        self.image.fill((random.randint(140,255),random.randint(0,255),random.randint(0,255)))
        self.rect = self.image.get_rect(center=pos)
