import pygame
from player import Player
from enemy import Enemy
import random

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.enemy_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.setup()

    def setup(self):
        self.player = Player((100, 400), self.player_sprite)
        self.enemy1 = Enemy((random.randint(200,500),random.randint(50,750)), self.enemy_sprites)
        self.enemy2 = Enemy((random.randint(550,800),random.randint(50,750)), self.enemy_sprites)
        self.enemy3 = Enemy((random.randint(850,1230),random.randint(50,750)), self.enemy_sprites)

    def run(self, dt):
        self.display_surface.fill('black')
        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update()
        self.player_sprite.draw(self.display_surface)
        self.player_sprite.update()
        self.action(dt)
    def action(self, dt):
        if pygame.sprite.spritecollide(self.player_sprite.sprite, self.enemy_sprites, False,):
            print("kolizja")
        print( pygame.sprite.spritecollide(self.player_sprite.sprite, self.enemy_sprites, False,))