import pygame
from pygame.locals import *

class Bullet(pygame.sprite.Sprite):

    def __init__ (self, surf, pos):
        super().__init__()
        self.image = pygame.image.load("images\\Bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
    def update(self):
        if self.rect.top < 0:
            self.kill()
        else:
            self.rect.move_ip(0, -15)

    def draw(self, surf):
        pygame.draw.rect(surf, [000, 255, 000], self.rect, 0)