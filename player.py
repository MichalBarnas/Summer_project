import pygame
import time


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((64, 64))
        self.image.fill('blue')
        self.rect = self.image.get_rect(center=pos)
        #statystyki, jeszcze nie wiem jakie i co która znaczy, wszystko testowo
        self.stats = [10,10,10,10,10,10]
    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect[1] += 2
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect[1] -= 2
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect[0] -= 2
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect[0] += 2
            
        #borderlines
        if self.rect[0] <0:
            self.rect[0]=0
        if self.rect[0] >1216:
            self.rect[0]=1216
            
        if self.rect[1] <0:
            self.rect[1]=0
        if self.rect[1] >736:
            self.rect[1]=736
        time.sleep(0.005)

    def update(self):
        self.movement()
