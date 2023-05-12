from src.function.collide import collide
import pygame

class Explosion():
    def __init__(self, pos_x, pos_y, img, damage):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = img
        self.damage = damage
        self.removeTime = False
        self.timer = 20
        self.mask = pygame.mask.from_surface(img)

    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))

    def collision(self, obj):
        return collide(self, obj)