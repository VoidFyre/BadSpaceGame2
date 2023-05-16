from src.model.weapon import Weapon
from src.model.beam import Beam
import pygame

class WeaponBeam(Weapon):
    def __init__(self, img, proj_img, damage:int, window_size:tuple, sound, hit_sound):
        super().__init__(img, proj_img, None, damage, 0, window_size, sound, hit_sound)
        self.returned = False
        self.beam = Beam(self.proj_img, self.window_size, self.damage, self.hit_sound, (self.pos_x, self.pos_y))
        self.shooting = True
        self.max_damage = damage * 3
        self.heat = 0
        self.max_heat = 300
        self.overheated = False

    def shoot(self):
        if not self.returned:
            self.returned = True
            return self.beam


    def update(self, pos: tuple):
        if self.shooting:
            if not self.overheated:
                self.beam.disabled = False
                if self.heat < self.max_heat:
                    self.heat += 1
                if self.heat == self.max_heat:
                    self.overheated = True
                if self.beam.damage < self.max_damage:
                    self.beam.damage += .1
            else:
                self.beam.damage = self.damage
                self.beam.disabled = True
        else:
            if self.beam.damage > self.damage:
                self.beam.damage -= .1
            self.beam.disabled = True
            if self.heat > 3:
                    self.heat -= 2
            if self.heat > 0:
                self.heat -= 1
            elif self.overheated:
                self.overheated = False
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.beam.update(pos)

    def heat_bar(self, window):
        pygame.draw.rect(window, (255, 70, 0), (10, 790, 10, 200))
        pygame.draw.rect(window, (255, 255, 255), (10, 790, 10, 200 - (200 * (self.heat/self.max_heat))))

    def render(self, window):
        super().render(window)
        self.heat_bar(window)