from src.function.collide import collide
import pygame

class Explosion():
    def __init__(self, pos_x, pos_y, img, damage):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = img
        self.damage = damage
        self.timer = 20
        self.mask = pygame.mask.from_surface(img)
        self.disabled = False
        self.active = True

    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.disabled = True

    def collision(self, obj):
        return collide(self, obj)