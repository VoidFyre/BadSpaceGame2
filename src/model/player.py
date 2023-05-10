import pygame
from src.model.objectMovable import ObjectMovable
from src.model.weapon import Weapon
from src.model.weaponSecondary import WeaponSecondary

class Player(ObjectMovable):
    def __init__(self, pos_x, pos_y, window_size: tuple):
        super().__init__(pos_x, pos_y, 5, None, window_size)
        self.health_cur = 100
        self.health_max = 100
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.primary_cd = 100
        self.secondary_cd = 100
        self.window_size = window_size
        self.primary_weapon = Weapon(
            img = pygame.transform.scale(pygame.image.load("assets/component/primary/weapon/primary_common.png"), (100, 100)),
            proj_img = pygame.transform.scale(pygame.image.load("assets/component/primary/projectile/projectile_primary_common.png"), (30, 30)),
            proj_speed = 10,
            damage = 10,
            cooldown = 40,
            window_size = self.window_size,
            sound = None
        )
        self.secondary_weapon = WeaponSecondary(
            img = pygame.transform.scale(pygame.image.load("assets/component/secondary/weapon/secondary_common.png"), (100, 100)),
            proj_img = pygame.transform.scale(pygame.image.load("assets/component/secondary/projectile/projectile_secondary_common.png"), (30, 30)),
            proj_exp_img = pygame.transform.scale(pygame.image.load("assets/component/secondary/explosion/explosion_secondary_common.png"), (20, 20)),
            proj_speed = 10,
            damage = 5,
            cooldown = 180,
            ammo = 10,
            max_ammo = 10,
            window_size = self.window_size,
            sound = None,
            expl_sound = None
        )
        self.thruster = None
        self.img = pygame.transform.scale(pygame.image.load("assets/component/ship/ship_common.png"), (100, 100))

    def move_left(self):
        if self.pos_x - self.speed > 0:
            self.pos_x -= self.speed

    def move_right(self):
        if self.pos_x + self.speed + self.img.get_height() < self.window_width:
            self.pos_x += self.speed

    def move_up(self):
        if self.pos_y - self.speed > 0:
            self.pos_y -= self.speed

    def move_down(self):
        if self.pos_y + self.speed + self.img.get_width() < self.window_height:
            self.pos_y += self.speed

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

        self.primary_weapon.update((self.pos_x, self.pos_y))
        self.secondary_weapon.update((self.pos_x, self.pos_y))

    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))
        self.primary_weapon.render(window)
        self.secondary_weapon.render(window)
        # self.thruster.render()