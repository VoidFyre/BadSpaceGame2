from src.model.weapon import Weapon
from src.model.beam import Beam
import pygame

class WeaponBeam(Weapon):
    def __init__(self, img, proj_anim, damage:int, window_size:tuple, sound, hit_sound):
        super().__init__(img, proj_anim, None, damage, 0, window_size, sound, hit_sound)
        self.returned = False
        self.beam = Beam(self.proj_img, self.window_size, self.damage, self.hit_sound, (self.pos_x, self.pos_y))
        self.shooting = True
        self.max_damage = damage * 3
        self.heat = 0
        self.max_heat = 300
        self.overheated = False
        self.hit_sound.set_volume(0.3)
        self.started_shooting = False
        self.deny_sound = pygame.mixer.Sound("assets/sound/denied.wav")
        self.recharge_sound = pygame.mixer.Sound("assets/sound/laser_recharge.wav")
        self.denied = False

    def shoot(self):
        if not self.returned:
            self.returned = True
            return self.beam
        
    def start_shoot_sound(self):
        self.sound.play(loops = -1)

    def stop_shoot_sound(self):
        self.sound.stop()

    def update(self, pos: tuple):
        if self.shooting and not self.overheated:
            if not self.started_shooting:
                self.start_shoot_sound()
                self.started_shooting = True

            self.beam.disabled = False
            if self.heat < self.max_heat:
                self.heat += 1

            if self.heat == self.max_heat:
                self.overheated = True
                self.beam.disabled = True
                self.stop_shoot_sound()

            if self.beam.damage < self.max_damage:
                self.beam.damage += .1

        if self.overheated:
            if self.shooting and not self.denied:
                self.denied = True
                self.deny_sound.play()

            if self.denied and not self.shooting:
                self.denied = False

            if self.heat > 0:
                self.heat -= 1

            else:
                self.recharge_sound.play()
                self.overheated = False

        if not self.shooting and not self.overheated:
            self.denied = False
            self.beam.disabled = True
            if self.started_shooting:
                self.stop_shoot_sound()
                self.started_shooting = False

            if self.beam.damage > self.damage:
                self.beam.damage -= .1

            if self.heat > 3:
                self.heat -= 2

            if self.heat > 0:
                self.heat -= 1

        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.beam.update(pos)

    def heat_bar(self, window):
        pygame.draw.rect(window, (255, 70, 0), (10, 790, 10, 200))
        pygame.draw.rect(window, (255, 255, 255), (10, 790, 10, 200 - (200 * (self.heat/self.max_heat))))

    def render(self, window):
        super().render(window)
        self.heat_bar(window)