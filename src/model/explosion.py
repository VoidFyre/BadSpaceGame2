from src.function.collide import collide
import pygame

class Explosion():
    def __init__(self, pos_x, pos_y, anim, damage):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.damage = damage
        self.timer = 32
        self.anim = anim
        self.img = anim[0]
        self.mask = pygame.mask.from_surface(self.img)
        self.disabled = False
        self.active = True

    def animate(self):
        if self.timer >= 28:
            self.img = self.anim[0]
        if self.timer >= 24 and self.timer < 28:
            self.img = self.anim[1]
        if self.timer >= 20 and self.timer < 24:
            self.img = self.anim[2]
        if self.timer >= 16 and self.timer < 20:
            self.img = self.anim[3]
        if self.timer >= 12 and self.timer < 16:
            self.img = self.anim[4]
        if self.timer >= 8 and self.timer < 12:
            self.img = self.anim[5]
        if self.timer >= 4 and self.timer < 8:
            self.img = self.anim[6]
        if self.timer >= 0 and self.timer < 4:
            self.img = self.anim[7]

    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))

    def update(self):
        self.animate()
        self.timer -= 1
        if self.timer == 0:
            self.disabled = True

    def collision(self, obj):
        return collide(self, obj)