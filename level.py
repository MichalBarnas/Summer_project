import pygame
from player import Player
from enemy import Enemy
import random

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.enemy_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.npc_sprites = pygame.sprite.Group()
        self.setup()
        self.game_state = 0
    def setup(self):
        self.player = Player((100, 400), self.player_sprite)
        self.enemy1 = Enemy((random.randint(200,500),random.randint(50,750)), self.enemy_sprites, (230,100,30),[3,3,3,3,3,3])
        self.npc1 = Enemy((random.randint(850,1230),random.randint(50,750)), self.npc_sprites,(100,200,200),[1,1,1,1,1,1])

    def run(self, dt):
        if self.game_state == 0:
            self.display_surface.fill((90,150,10))
            self.player_sprite.draw(self.display_surface)
            self.player_sprite.update()
            self.enemy_sprites.draw(self.display_surface)
            self.npc_sprites.draw(self.display_surface)
            self.action(dt)
        elif self.game_state == 1:
            self.display_surface.fill((190,150,10))
            self.player_sprite.draw(self.display_surface)
            self.player_sprite.update()
            self.enemy_sprites.draw(self.display_surface)     
            self.action(dt)
    def action(self, dt):
        if pygame.sprite.spritecollide(self.player_sprite.sprite, self.enemy_sprites, True,):
            self.game_state = 1
            self.player.rect[1] = 400
            self.player.rect[0] = 200
            self.enemy1 = Enemy((800,400), self.enemy_sprites,(230,100,30),[3,3,3,3,3,3])