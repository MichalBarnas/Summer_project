import  pygame
from player import Player
from enemy import Enemy
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.enemy_sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.setup()
    def setup(self):
        self.player = Player((200,150), self.player_sprite)
        self.enemy = Enemy((300,400), self.enemy_sprites)
    def run(self,dt):
        self.display_surface.fill('black')
        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update()
        self.player_sprite.draw(self.display_surface)
        self.player_sprite.update()
    def collizion(self,dt):
        if pygame.sprite.spritecollide(self.player_sprite.sprite, self.enemy_sprites, True):
            print("kolizja")
    