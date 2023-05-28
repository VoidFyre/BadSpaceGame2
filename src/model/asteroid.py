from src.model.objectMovable import ObjectMovable
import random
import pygame

class Asteroid(ObjectMovable):
    def __init__(self, pos_x, pos_y, window_size, sounds):
        img = self.load_image("assets/item/asteroid1.png", (150, 150))
        self.sounds = sounds
        super().__init__(pos_x, pos_y, random.randint(3, 6), img, window_size)
        self.health = 900
        self.anim = [
            self.load_image("assets/item/asteroid1.png", (150, 150)),
            self.load_image("assets/item/asteroid2.png", (150, 150)),
            self.load_image("assets/item/asteroid3.png", (150, 150)),
            self.load_image("assets/item/asteroid4.png", (150, 150)),
            self.load_image("assets/item/asteroid5.png", (150, 150)),
            self.load_image("assets/item/asteroid6.png", (150, 150)),
        ]
        self.destroyed = False
        self.anim_timer = 6
        
        
        
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0 and not self.disabled:
            self.sounds.rock_break.play()
            self.destroyed = True

    def update(self):
        if self.health >= 600:
            self.img = self.anim[0]
        if self.health >= 300 and self.health < 600:
            self.img = self.anim[1]
        if self.health > 0 and self.health < 300:
            self.img = self.anim[2]

        if self.destroyed:
            if self.anim_timer > 0:
                self.anim_timer -= 1
            if self.anim_timer > 4:
                self.img = self.anim[3]
            if self.anim_timer > 2 and self.anim_timer <= 4:
                self.img = self.anim[4]
            if self.anim_timer > 0 and self.anim_timer > 2:
                self.img = self.anim[5]
            if self.anim_timer == 0:
                self.disabled = True

        self.move_down()