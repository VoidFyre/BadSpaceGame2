import pygame
from src.function.loadImage import loadImage
from src.model.weapon import Weapon
from src.model.weaponSecondary import WeaponSecondary
from src.model.thruster import Thruster
from src.model.shield import Shield

class Component():
    def __init__(self, window_size):

        self.window_size = window_size
        
        self.primary_weapons = {
            "common": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_common.png", (75, 75)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_common.png", (30, 30)),
                proj_speed = 10,
                damage = 100,
                cooldown = 15,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg"),
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            ),
            "uncommon": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_uncommon.png", (75, 75)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_uncommon.png", (30, 30)),
                proj_speed = 10,
                damage = 150,
                cooldown = 15,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg"),
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            ),
            "rare": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_rare.png", (75, 75)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_rare.png", (30, 30)),
                proj_speed = 10,
                damage = 150,
                cooldown = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg"),
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            ),
            "epic": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_epic.png", (75, 75)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_epic.png", (30, 30)),
                proj_speed = 10,
                damage = 200,
                cooldown = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg"),
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            ),
            "legendary": Weapon(
                img = self.load_image("assets/component/primary/weapon/primary_legendary.png", (75, 75)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_legendary.png", (30, 30)),
                proj_speed = 10,
                damage = 250,
                cooldown = 5,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg"),
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            )
        }

        self.secondary_weapons = {
            "common": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_common.png", (75, 75)),
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
                exp_dmg = 200,
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            ),
            "uncommon": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_uncommon.png", (75, 75)),
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
                exp_dmg = 220,
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            ),
            "rare": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_rare.png", (75, 75)),
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
                exp_dmg = 250,
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            ),
            "epic": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_epic.png", (75, 75)),
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
                exp_dmg = 300,
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            ),
            "legendary": WeaponSecondary(
                img = self.load_image("assets/component/secondary/weapon/secondary_legendary.png", (75, 75)),
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
                exp_dmg = 400,
                hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
            )
        }

        self.ships = {
            "common": (self.load_image("assets/component/ship/ship_common.png", (75, 75)), 100),
            "uncommon": (self.load_image("assets/component/ship/ship_uncommon.png", (75, 75)), 150),
            "rare": (self.load_image("assets/component/ship/ship_rare.png", (75, 75)), 250),
            "epic": (self.load_image("assets/component/ship/ship_epic.png", (75, 75)), 400),
            "legendary": (self.load_image("assets/component/ship/ship_legendary.png", (75, 75)), 750),
        }

        self.thrusters = {
            "common": Thruster(
                img = self.load_image("assets/component/thruster/thruster_common.png", (75, 75)),
                speed = 5,
                window_size = self.window_size,
                special_sound = None
            ),
            "uncommon": Thruster(
                img = self.load_image("assets/component/thruster/thruster_uncommon.png", (75, 75)),
                speed = 6,
                window_size = self.window_size,
                special_sound = None
            ),
            "rare": Thruster(
                img = self.load_image("assets/component/thruster/thruster_rare.png", (75, 75)),
                speed = 7,
                window_size = self.window_size,
                special_sound = None
            ),
            "epic": Thruster(
                img = self.load_image("assets/component/thruster/thruster_epic.png", (75, 75)),
                speed = 9,
                window_size = self.window_size,
                special_sound = None
            ),
            "legendary": Thruster(
                img = self.load_image("assets/component/thruster/thruster_legendary.png", (75, 75)),
                speed = 12,
                window_size = self.window_size,
                special_sound = None
            )
        }

        self.shields = {
            "common": Shield(
                img = self.load_image("assets/component/shield/shield_common.png", (95, 95)),
                health = 50
            ),
            "uncommon": Shield(
                img = self.load_image("assets/component/shield/shield_uncommon.png", (95, 95)),
                health = 100
            ),
            "rare": Shield(
                img = self.load_image("assets/component/shield/shield_rare.png", (95, 95)),
                health = 150
            ),
            "epic": Shield(
                img = self.load_image("assets/component/shield/shield_epic.png", (95, 95)),
                health = 250
            ),
            "legendary": Shield(
                img = self.load_image("assets/component/shield/shield_legendary.png", (95, 95)),
                health = 400
            ),
        }

    def get_primary(self, rarity):
        return self.primary_weapons[rarity]
    
    def get_secondary(self, rarity):
        return self.secondary_weapons[rarity]
    
    def get_ship(self, rarity):
        return self.ships[rarity]

    def get_thruster(self, rarity):
        return self.thrusters[rarity]

    def get_shield(self, rarity):
        return self.shields[rarity]

    def load_image(self, path:str, size:tuple):
        return loadImage(path, size)