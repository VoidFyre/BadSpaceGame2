import pygame
from src.function.loadImage import loadImage
from src.model.weapon import Weapon
from src.model.weaponSecondary import WeaponSecondary
from src.model.thruster import Thruster
from src.model.shield import Shield
from src.model.weaponBeam import WeaponBeam

class Component():
    def __init__(self, window_size, sounds):

        self.window_size = window_size
        self.sounds = sounds
        
        self.primary_weapons = {
            "common": Weapon(
                name = "Ballistic Repeater",
                name_color = "White",
                img = self.load_image("assets/component/primary/weapon/primary_common.png", (75, 75)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_common.png", (30, 30)),
                proj_speed = 10,
                damage = 100,
                cooldown = 15,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/gunshot.wav"),
                hit_sound = self.sounds.hit
            ),
            "uncommon": Weapon(
                name = "Laser Rifle",
                name_color = "Green",
                img = self.load_image("assets/component/primary/weapon/primary_uncommon.png", (75, 75)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_uncommon.png", (30, 30)),
                proj_speed = 12,
                damage = 150,
                cooldown = 15,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/laser_fire.ogg"),
                hit_sound = self.sounds.hit
            ),
            "rare": Weapon(
                name = "Plasma Thrower",
                name_color = "Blue",
                img = self.load_image("assets/component/primary/weapon/primary_rare.png", (75, 75)),
                proj_img = self.load_image("assets/component/primary/projectile/projectile_primary_rare.png", (30, 30)),
                proj_speed = 15,
                damage = 150,
                cooldown = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/plasma_shot.wav"),
                hit_sound = self.sounds.hit
            ),
            "epic": WeaponBeam(
                name = "Graviton Accelerator",
                name_color = "Purple",
                img = self.load_image("assets/component/primary/weapon/primary_epic.png", (75, 75)),
                proj_anim = [
                    self.load_image("assets/component/primary/projectile/laser_epic1.png", (32, 1028)),
                    self.load_image("assets/component/primary/projectile/laser_epic2.png", (32, 1028)),
                    self.load_image("assets/component/primary/projectile/laser_epic3.png", (32, 1028)),
                    self.load_image("assets/component/primary/projectile/laser_epic4.png", (32, 1028))
                ],
                damage = 10,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/beam_fire.ogg"),
                hit_sound = self.sounds.hit
            ),
            "legendary": WeaponBeam(
                name = "Solar Radiation Ray",
                name_color = "Orange",
                img = self.load_image("assets/component/primary/weapon/primary_legendary.png", (75, 75)),
                proj_anim = [
                    self.load_image("assets/component/primary/projectile/laser_legendary1.png", (32, 1028)),
                    self.load_image("assets/component/primary/projectile/laser_legendary2.png", (32, 1028)),
                    self.load_image("assets/component/primary/projectile/laser_legendary3.png", (32, 1028)),
                    self.load_image("assets/component/primary/projectile/laser_legendary4.png", (32, 1028))
                ],
                damage = 15,
                window_size = self.window_size,
                sound = pygame.mixer.Sound("assets/sound/beam_fire.ogg"),
                hit_sound = self.sounds.hit
            )
        }

        self.secondary_weapons = {
            "common": WeaponSecondary(
                name = "Rocket Launcher Mk1",
                name_color = "White",
                img = self.load_image("assets/component/secondary/weapon/secondary_common.png", (75, 75)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_common.png", (30, 30)),
                proj_exp_anim = [
                    self.load_image("assets/effect/explosion_common/1.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/2.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/3.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/4.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/5.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/6.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/7.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/8.png", (500, 500))
                ],
                proj_speed = 12,
                damage = 5,
                cooldown = 180,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = self.sounds.secondary_fire,
                exp_sound = self.sounds.explosion,
                exp_dmg = 200,
                hit_sound = self.sounds.hit,
                tracking = False,
                proj_count = 1
            ),
            "uncommon": WeaponSecondary(
                "Vector Rocket Launcher",
                name_color = "Green",
                img = self.load_image("assets/component/secondary/weapon/secondary_uncommon.png", (75, 75)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_uncommon.png", (30, 30)),
                proj_exp_anim = [
                    self.load_image("assets/effect/explosion_common/1.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/2.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/3.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/4.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/5.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/6.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/7.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/8.png", (500, 500))
                ],
                proj_speed = 12,
                damage = 10,
                cooldown = 160,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = self.sounds.secondary_fire,
                exp_sound = self.sounds.explosion,
                exp_dmg = 220,
                hit_sound = self.sounds.hit,
                tracking = False,
                proj_count = 1
            ),
            "rare": WeaponSecondary(
                name = "Seismic Grenade Launcher",
                name_color = "Blue",
                img = self.load_image("assets/component/secondary/weapon/secondary_rare.png", (75, 75)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_rare.png", (30, 30)),
                proj_exp_anim = [
                    self.load_image("assets/effect/explosion_common/1.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/2.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/3.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/4.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/5.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/6.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/7.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/8.png", (500, 500))
                ],
                proj_speed = 12,
                damage = 15,
                cooldown = 140,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = self.sounds.secondary_fire,
                exp_sound = self.sounds.explosion,
                exp_dmg = 250,
                hit_sound = self.sounds.hit,
                tracking = True,
                proj_count = 1
            ),
            "epic": WeaponSecondary(
                name = "Singularity Cannon",
                name_color = "Purple",
                img = self.load_image("assets/component/secondary/weapon/secondary_epic.png", (75, 75)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_epic.png", (30, 30)),
                proj_exp_anim = [
                    self.load_image("assets/effect/explosion_common/1.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/2.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/3.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/4.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/5.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/6.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/7.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/8.png", (500, 500))
                ],
                proj_speed = 12,
                damage = 25,
                cooldown = 130,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = self.sounds.secondary_fire,
                exp_sound = self.sounds.explosion,
                exp_dmg = 300,
                hit_sound = self.sounds.hit,
                tracking = True,
                proj_count = 1
            ),
            "legendary": WeaponSecondary(
                name = "Solar Storm Cluster Launcher",
                name_color = "Orange",
                img = self.load_image("assets/component/secondary/weapon/secondary_legendary.png", (75, 75)),
                proj_img = self.load_image("assets/component/secondary/projectile/projectile_secondary_legendary.png", (30, 30)),
                proj_exp_anim = [
                    self.load_image("assets/effect/explosion_common/1.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/2.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/3.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/4.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/5.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/6.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/7.png", (500, 500)),
                    self.load_image("assets/effect/explosion_common/8.png", (500, 500))
                ],
                proj_speed = 12,
                damage = 50,
                cooldown = 120,
                ammo = 10,
                max_ammo = 10,
                window_size = self.window_size,
                sound = self.sounds.secondary_fire,
                exp_sound = self.sounds.explosion,
                exp_dmg = 400,
                hit_sound = self.sounds.hit,
                tracking = True,
                proj_count = 6
            )
        }

        COMMON_SHIP_HP = 100
        UNCOMMON_SHIP_HP = 150
        RARE_SHIP_HP = 250
        EPIC_SHIP_HP = 400
        LEGENDARY_SHIP_HP = 750

        self.ships = {
            "common": (self.load_image("assets/component/ship/ship_common.png", (75, 75)), COMMON_SHIP_HP, "Squadron Fighter Mk1", "White"),
            "uncommon": (self.load_image("assets/component/ship/ship_uncommon.png", (75, 75)), UNCOMMON_SHIP_HP, "Squadron Interceptor", "Green"),
            "rare": (self.load_image("assets/component/ship/ship_rare.png", (75, 75)), RARE_SHIP_HP, "Crescent Wing Bomber", "Blue"),
            "epic": (self.load_image("assets/component/ship/ship_epic.png", (75, 75)), EPIC_SHIP_HP, "Axe Wing Executioner", "Purple"),
            "legendary": (self.load_image("assets/component/ship/ship_legendary.png", (75, 75)), LEGENDARY_SHIP_HP, "Sun Wing Destroyer \"Gungnir\"", "Orange"),
        }

        self.thrusters = {
            "common": Thruster(
                name = "Ion Thruster Mk1",
                name_color = "White",
                img = self.load_image("assets/component/thruster/thruster_common.png", (75, 75)),
                speed = 5,
                window_size = self.window_size,
                special_sound = None
            ),
            "uncommon": Thruster(
                name = "Ion Thruster Mk2 Boost",
                name_color = "Green",
                img = self.load_image("assets/component/thruster/thruster_uncommon.png", (75, 75)),
                speed = 6,
                window_size = self.window_size,
                special_sound = None
            ),
            "rare": Thruster(
                name = "Plasmatic Afterburner",
                name_color = "Blue",
                img = self.load_image("assets/component/thruster/thruster_rare.png", (75, 75)),
                speed = 7,
                window_size = self.window_size,
                special_sound = None
            ),
            "epic": Thruster(
                name = "Wormhole Blink Drive",
                name_color = "Purple",
                img = self.load_image("assets/component/thruster/thruster_epic.png", (75, 75)),
                speed = 9,
                window_size = self.window_size,
                special_sound = None
            ),
            "legendary": Thruster(
                "Hyperion Lightspeed Drive",
                name_color = "Orange",
                img = self.load_image("assets/component/thruster/thruster_legendary.png", (75, 75)),
                speed = 12,
                window_size = self.window_size,
                special_sound = None
            )
        }

        COMMON_SHIELD_HP = 50
        UNCOMMON_SHIELD_HP = 100
        RARE_SHIELD_HP = 150
        EPIC_SHIELD_HP = 250
        LEGENDARY_SHIELD_HP = 400

        self.shields = {
            "common": Shield(
                name = "Deflector Mk1",
                name_color = "White",
                img = self.load_image("assets/component/shield/shield_common.png", (95, 95)),
                health = COMMON_SHIELD_HP
            ),
            "uncommon": Shield(
                name = "Laser Deflector",
                name_color = "Green",
                img = self.load_image("assets/component/shield/shield_uncommon.png", (95, 95)),
                health = UNCOMMON_SHIELD_HP
            ),
            "rare": Shield(
                name = "Plasma Projector Shield",
                name_color = "Blue",
                img = self.load_image("assets/component/shield/shield_rare.png", (95, 95)),
                health = RARE_SHIELD_HP
            ),
            "epic": Shield(
                name = "Graviton Well Absorption Shield",
                name_color = "Purple",
                img = self.load_image("assets/component/shield/shield_epic.png", (95, 95)),
                health = EPIC_SHIELD_HP
            ),
            "legendary": Shield(
                name = "Sunbeam Projector Shield",
                name_color = "Orange",
                img = self.load_image("assets/component/shield/shield_legendary.png", (95, 95)),
                health = LEGENDARY_SHIELD_HP
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