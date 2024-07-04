import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group,image,stats):
        super().__init__(group)
        self.stats = stats
        self.image = image
        self.image = pygame.Surface((64, 64))
        self.image.fill((150,100,50))
        self.rect = self.image.get_rect(center=pos)

class Skeleton(Enemy):
    def __init__(self, pos, group,name,image,stats,size):
        super().__init__(group)
        self.stats = stats
        self.image = image
        self.name = name
        self.image = pygame.Surface(size)
        self.image.fill((150,100,50))
        self.rect = self.image.get_rect(center=pos)