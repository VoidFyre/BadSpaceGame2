from src.model.objectMovable import ObjectMovable
from src.model.projectile import Projectile
from src.model.shipExplosion import ShipExplosion
import pygame
import random

class Enemy(ObjectMovable):
    def __init__(self, pos_x, pos_y, speed:int, window_size, rarity, wave):
        self.rarity = rarity
        self.wave = wave
        self.window_size = window_size
        self.cooldown = 0
        self.pos_y_stop = random.randint(300, 550)
        self.pos_x_left = pos_x - random.randint(30, 70)
        self.pos_x_right = pos_x + random.randint(30, 70)
        self.direction = random.choice(["left", "right"])
        self.death_sound = pygame.mixer.Sound("assets/sound/death.ogg")
        self.hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")

        # Image Rarity Map
        image = {
            "common": self.load_image("assets/component/enemy/enemy_common.png", (75, 75)),
            "uncommon": self.load_image("assets/component/enemy/enemy_uncommon.png", (75, 75)),
            "rare": self.load_image("assets/component/enemy/enemy_rare.png", (75, 75)),
            "epic": self.load_image("assets/component/enemy/enemy_epic.png", (100, 100)),
            "legendary": self.load_image("assets/component/enemy/enemy_legendary.png", (130, 130))
        }

        projImage = {
            "common": self.load_image("assets/component/primary/projectile/projectile_primary_common.png", (30, 30)),
            "uncommon": self.load_image("assets/component/primary/projectile/projectile_primary_uncommon.png", (30, 30)),
            "rare": self.load_image("assets/component/primary/projectile/projectile_primary_rare.png", (30, 30)),
            "epic": self.load_image("assets/component/primary/projectile/projectile_primary_epic.png", (30, 30)),
            "legendary": self.load_image("assets/component/primary/projectile/projectile_primary_legendary.png", (30, 30)),
        }

        projDamage = {
            "common": 10 * (1 + (0.1 * wave)),
            "uncommon": 15 * (1 + (0.1 * wave)),
            "rare": 20 * (1 + (0.1 * wave)),
            "epic": 25 * (1 + (0.1 * wave)),
            "legendary": 40 * (1 + (0.1 * wave)),
        }

        health = {
            "common": 100 * (1 + (0.1 * wave)),
            "uncommon": 150 * (1 + (0.1 * wave)),
            "rare": 200 * (1 + (0.1 * wave)),
            "epic": 250 * (1 + (0.1 * wave)),
            "legendary": 500 * (1 + (0.1 * wave)),
        }

        self.img = image[rarity]
        self.projImg = projImage[rarity]
        self.projDmg = projDamage[rarity]
        self.health_cur = health[rarity]
        self.health_max = health[rarity]
        super().__init__(pos_x, pos_y, speed, self.img, window_size)

    def shoot(self):
        return Projectile(self.pos_x + self.img.get_width() / 2 - 15, self.pos_y + 50, 10, self.projImg, "enemy", self.window_size, self.projDmg, self.hit_sound)
    
    def update(self):
        if self.pos_y < self.pos_y_stop:
            self.move_down()
        elif self.direction == "left":
            self.move_left()
            if self.pos_x <= self.pos_x_left:
                self.direction = "right"

        elif self.direction == "right":
            self.move_right()
            if self.pos_x >= self.pos_x_right:
                self.direction = "left"


    def render(self, window):
        super().render(window)
        if self.health_cur != self.health_max:
            self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.pos_x, self.pos_y - self.img.get_height() + 80, self.img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.pos_x, self.pos_y - self.img.get_height() + 80, self.img.get_width() * (self.health_cur/self.health_max), 10))

    def hit(self, damage):
        self.health_cur -= damage
        if self.health_cur <= 0:
            self.disabled = True

    def death(self):
        self.death_sound.play()
        return ShipExplosion(self.pos_x - 50, self.pos_y - 20)