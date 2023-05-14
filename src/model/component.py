import pygame
from src.function.loadImage import loadImage
from src.model.weapon import Weapon
from src.model.weaponSecondary import WeaponSecondary

class Component():
    def __init__(self, window_size):

        self.window_size = window_size
        self.primary_weapons = {
            "common": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_common.png", (100, 100)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_common.png", (30, 30)),
                proj_speed = 10,
                damage = 100,
                cooldown = 15,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg")
            ),
            "uncommon": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_uncommon.png", (100, 100)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_uncommon.png", (30, 30)),
                proj_speed = 10,
                damage = 150,
                cooldown = 15,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg")
            ),
            "rare": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_rare.png", (100, 100)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_rare.png", (30, 30)),
                proj_speed = 10,
                damage = 150,
                cooldown = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg")
            ),
            "epic": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_epic.png", (100, 100)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_epic.png", (30, 30)),
                proj_speed = 10,
                damage = 200,
                cooldown = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg")
            ),
            "legendary": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_legendary.png", (100, 100)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_legendary.png", (30, 30)),
                proj_speed = 10,
                damage = 250,
                cooldown = 5,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg")
            )
        }

        self.secondary_weapons = {
            "common": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_common.png", (100, 100)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_common.png", (30, 30)),
                proj_exp_img = self.load_image("assets/component/secondary/explosion/explosion_secondary_common.png", (500, 500)),
                proj_speed = 12,
                damage = 5,
                cooldown = 180,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/secondary_fire.ogg"),
                exp_sound = pygame.mixer.Sound("assets/sound/explosion.wav"),
                exp_dmg = 200
            ),
            "uncommon": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_uncommon.png", (100, 100)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_uncommon.png", (30, 30)),
                proj_exp_img = self.load_image("assets/component/secondary/explosion/explosion_secondary_uncommon.png", (500, 500)),
                proj_speed = 12,
                damage = 10,
                cooldown = 160,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/secondary_fire.ogg"),
                exp_sound = pygame.mixer.Sound("assets/sound/explosion.wav"),
                exp_dmg = 220
            ),
            "rare": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_rare.png", (100, 100)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_rare.png", (30, 30)),
                proj_exp_img = self.load_image("assets/component/secondary/explosion/explosion_secondary_rare.png", (500, 500)),
                proj_speed = 12,
                damage = 15,
                cooldown = 140,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/secondary_fire.ogg"),
                exp_sound = pygame.mixer.Sound("assets/sound/explosion.wav"),
                exp_dmg = 250
            ),
            "epic": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_epic.png", (100, 100)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_epic.png", (30, 30)),
                proj_exp_img = self.load_image("assets/component/secondary/explosion/explosion_secondary_epic.png", (500, 500)),
                proj_speed = 12,
                damage = 25,
                cooldown = 130,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/secondary_fire.ogg"),
                exp_sound = pygame.mixer.Sound("assets/sound/explosion.wav"),
                exp_dmg = 300
            ),
            "legendary": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_legendary.png", (100, 100)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_legendary.png", (30, 30)),
                proj_exp_img = self.load_image("assets/component/secondary/explosion/explosion_secondary_legendary.png", (500, 500)),
                proj_speed = 12,
                damage = 50,
                cooldown = 120,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/secondary_fire.ogg"),
                exp_sound = pygame.mixer.Sound("assets/sound/explosion.wav"),
                exp_dmg = 400
            )
        }

        self.ships = {
            "common": (self.load_image("assets/component/ship/ship_common.png", (100, 100)), 100),
            "uncommon": (self.load_image("assets/component/ship/ship_uncommon.png", (100, 100)), 150),
            "rare": (self.load_image("assets/component/ship/ship_rare.png", (100, 100)), 250),
            "epic": (self.load_image("assets/component/ship/ship_epic.png", (100, 100)), 400),
            "legendary": (self.load_image("assets/component/ship/ship_legendary.png", (100, 100)), 750),
        }

    def get_primary(self, rarity):
        return self.primary_weapons[rarity]
    
    def get_secondary(self, rarity):
        return self.secondary_weapons[rarity]
    
    def get_ship(self, rarity):
        return self.ships[rarity]

    def load_image(self, path:str, size:tuple):
        return loadImage(path, size)