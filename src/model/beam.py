import pygame
from src.function.collide import collide

class Beam():
    def __init__(self, anim, window_size:tuple, damage:int, hit_sound, pos):
        self.owner = "player"
        self.anim = anim
        self.window_size = window_size
        self.damage = damage
        self.hit_sound = hit_sound
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.disabled = False
        self.img = self.anim[0]
        self.mask = pygame.mask.from_surface(self.img)
        self.animation_timer = 0

    def animate(self):
        if self.animation_timer < 8:
            self.animation_timer += 1
        else:
            self.animation_timer = 0

        if self.animation_timer >= 0 and self.animation_timer < 2:
            self.img = self.anim[0]
        if self.animation_timer >= 2 and self.animation_timer < 4:
            self.img = self.anim[1]
        if self.animation_timer >= 4 and self.animation_timer < 6:
            self.img = self.anim[2]
        if self.animation_timer >= 6:
            self.img = self.anim[3]

    def update(self, pos):
        self.animate()
        self.pos_x = pos[0] + 16
        self.pos_y = pos[1] - 1028

    def hit(self):
        self.hit_sound.play()

    def render(self, window):
        if not self.disabled:
            window.blit(self.img, (self.pos_x, self.pos_y))

    def collision(self, obj):
        return collide(self, obj) and not self.disabled