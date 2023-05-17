from src.model.objectMovable import ObjectMovable
import pygame

class Projectile(ObjectMovable):
    def __init__(self, pos_x, pos_y, speed:int, img, owner:str, window_size:tuple, damage:int, hit_sound):
        self.owner = owner
        self.damage = damage
        super().__init__(pos_x, pos_y, speed, img, window_size)
        self.hit_sound = hit_sound

    def update(self):
        super().update()

        if self.owner == "player":
            self.move_up()

        if self.owner == "enemy":
            self.move_down()

    def hit(self):
        self.disabled = True
        self.hit_sound.play()