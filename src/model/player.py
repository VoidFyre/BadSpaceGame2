import pygame
from src.model.objectMovable import ObjectMovable
from src.model.component import Component

class Player(ObjectMovable):
    def __init__(self, pos_x, pos_y, window_size: tuple):
        self.component = Component(window_size)
        
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.primary_cd = 100
        self.secondary_cd = 100
        self.window_size = window_size
        self.primary_rarity = "legendary"
        self.secondary_rarity = "common"
        self.ship_rarity = "common"
        self.thruster_rarity = "common"
        self.shield_rarity = "common"
        self.img, self.health_max = self.component.get_ship(self.ship_rarity)
        self.primary_weapon = self.component.get_primary(self.primary_rarity)
        self.secondary_weapon = self.component.get_secondary(self.secondary_rarity)
        self.thruster = self.component.get_thruster(self.thruster_rarity)
        self.shield = self.component.get_shield(self.shield_rarity)
        self.refil_health = False
        

        
        self.health_cur = self.health_max
        super().__init__(pos_x, pos_y, 5, self.img, window_size)

    def move_left(self):
        if self.pos_x - self.thruster.speed > 0:
            self.pos_x -= self.thruster.speed

    def move_right(self):
        if self.pos_x + self.thruster.speed + self.img.get_height() < self.window_width:
            self.pos_x += self.thruster.speed

    def move_up(self):
        if self.pos_y - self.thruster.speed > 0:
            self.pos_y -= self.thruster.speed

    def move_down(self):
        if self.pos_y + self.thruster.speed + self.img.get_width() < self.window_height:
            self.pos_y += self.thruster.speed

    def shoot_primary(self):
        if self.primary_cd == 0:
            self.primary_cd = self.primary_weapon.cooldown
            return self.primary_weapon.shoot()

    def shoot_secondary(self):
        if self.secondary_cd == 0:
            self.secondary_cd = self.secondary_weapon.cooldown
            return self.secondary_weapon.shoot()
    
    def update(self):
        if self.primary_cd > 0:
            self.primary_cd -= 1

        if self.secondary_cd > 0:
            self.secondary_cd -= 1

        self.img, self.health_max = self.component.get_ship(self.ship_rarity)
        self.primary_weapon = self.component.get_primary(self.primary_rarity)
        self.secondary_weapon = self.component.get_secondary(self.secondary_rarity)
        self.thruster = self.component.get_thruster(self.thruster_rarity)
        self.shield = self.component.get_shield(self.shield_rarity)

        self.primary_weapon.update((self.pos_x, self.pos_y))
        self.secondary_weapon.update((self.pos_x, self.pos_y))
        self.thruster.update((self.pos_x, self.pos_y))
        self.shield.update((self.pos_x, self.pos_y))

        if self.refil_health:
            self.refil_health = False
            self.health_cur = self.health_max

        if self.disabled:
            return True
        else:
            return False

    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))
        self.primary_weapon.render(window)
        self.secondary_weapon.render(window)
        self.thruster.render(window)
        self.shield.render(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.pos_x, self.pos_y + self.img.get_height() + 10, self.img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.pos_x, self.pos_y + self.img.get_height() + 10, self.img.get_width() * (self.health_cur/self.health_max), 10))
        pygame.draw.rect(window, (0, 0, 255), (self.pos_x, self.pos_y + self.img.get_height() + 15, self.img.get_width() * (self.shield.health_cur/self.shield.health_max), 5))

    def hit(self, damage):
        if self.shield.health_cur > 0:
            self.shield.hit(damage)
        else: 
            self.health_cur -= damage
        if self.health_cur <= 0:
            self.disabled = True

    def refil_ammo(self):
        self.secondary_weapon.refil_ammo()