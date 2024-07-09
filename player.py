import pygame
import time
import config as c


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface(c.PLAYER_SIZE)
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)
        #statystyki, jeszcze nie wiem jakie i co która znaczy, wszystko testowo
        self.stats = [10,10,10,10,10,10]
        self.speed = c.SPEED

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect[1] += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect[1] -= self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect[0] -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect[0] += self.speed
            
        #borderlines
        if self.rect[0] < 0:
            self.rect[0] = 0
        if self.rect[0] > (c.SCREEN_WIDTH - c.PLAYER_SIZE[0]):
            self.rect[0] = (c.SCREEN_WIDTH - c.PLAYER_SIZE[0])
            
        if self.rect[1] < 0:
            self.rect[1] = 0
        if self.rect[1] > (c.SCREEN_HIGHT - c.PLAYER_SIZE[1]):
            self.rect[1] = (c.SCREEN_HIGHT - c.PLAYER_SIZE[1])
        # time.sleep(0.005)

    

    def update(self):
        self.movement()
