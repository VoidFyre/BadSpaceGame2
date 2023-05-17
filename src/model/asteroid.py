from src.model.objectMovable import ObjectMovable
import random
import pygame

class Asteroid(ObjectMovable):
    def __init__(self, pos_x, pos_y, window_size):
        img = self.load_image("assets/item/asderoid_1.png", (150, 150))
        super().__init__(pos_x, pos_y, random.randint(3, 6), img, window_size)
        self.health = 500
        
        self.break_sound = pygame.mixer.Sound("assets/sound/rock_break.wav")

        
        
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0 and not self.disabled:
            self.break_sound.play()
            self.disabled = True

    def update(self):
        self.move_down()