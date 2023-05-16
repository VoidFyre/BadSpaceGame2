import pygame
from src.function.collide import collide

class Beam():
    def __init__(self, img, window_size:tuple, damage:int, hit_sound, pos):
        self.img = img
        self.window_size = window_size
        self.damage = damage
        self.hit_sound = hit_sound
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.disabled = False
        self.mask = pygame.mask.from_surface(self.img)

    def update(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1] - 1000

    def hit(self):
        self.hit_sound.play()

    def render(self, window):
        if not self.disabled:
            window.blit(self.img, (self.pos_x, self.pos_y))

    def collision(self, obj):
        return collide(self, obj)