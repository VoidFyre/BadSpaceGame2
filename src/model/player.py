import pygame
from src.model.objectMovable import ObjectMovable
from src.model.component import Component
from src.model.shipExplosion import ShipExplosion

class Player(ObjectMovable):
    def __init__(self, pos_x, pos_y, window_size: tuple):
        self.component = Component(window_size)
        
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.primary_cd = 0
        self.secondary_cd = 0
        self.window_size = window_size
        self.primary_rarity = "common"
        self.secondary_rarity = "common"
        self.ship_rarity = "common"
        self.thruster_rarity = "common"
        self.shield_rarity = "common"

        self.new_primary = False
        self.new_secondary = False
        self.new_thruster = False
        self.new_ship = False
        self.new_shield = False
        self.new_display_timer = 120

        self.img, self.health_max, self.ship_name, self.ship_name_color = self.component.get_ship(self.ship_rarity)
        self.primary_weapon = self.component.get_primary(self.primary_rarity)
        self.secondary_weapon = self.component.get_secondary(self.secondary_rarity)
        self.thruster = self.component.get_thruster(self.thruster_rarity)
        self.shield = self.component.get_shield(self.shield_rarity)
        self.refil_health = False
        self.dead = False
        self.death_sound = pygame.mixer.Sound("assets/sound/death.ogg")
        self.death_shock = pygame.mixer.Sound("assets/sound/death_shock.wav")
        

        
        self.health_cur = self.health_max
        super().__init__(pos_x, pos_y, 5, self.img, window_size)

    def move_left(self):
        if not self.dead:
            if self.pos_x - self.thruster.speed > 0:
                self.pos_x -= self.thruster.speed

    def move_right(self):
        if not self.dead:
            if self.pos_x + self.thruster.speed + self.img.get_height() < self.window_width:
                self.pos_x += self.thruster.speed

    def move_up(self):
        if not self.dead:
            if self.pos_y - self.thruster.speed > 0:
                self.pos_y -= self.thruster.speed

    def move_down(self):
        if not self.dead:
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

        self.img, self.health_max, self.ship_name, self.ship_name_color = self.component.get_ship(self.ship_rarity)
        self.primary_weapon = self.component.get_primary(self.primary_rarity)
        self.secondary_weapon = self.component.get_secondary(self.secondary_rarity)
        self.thruster = self.component.get_thruster(self.thruster_rarity)
        self.shield = self.component.get_shield(self.shield_rarity)

        if not self.dead:
            self.primary_weapon.update((self.pos_x, self.pos_y))
            self.secondary_weapon.update((self.pos_x, self.pos_y))
            self.thruster.update((self.pos_x, self.pos_y))
            self.shield.update((self.pos_x, self.pos_y))

        if self.refil_health:
            self.refil_health = False
            self.health_cur = self.health_max


    def get_font(self, size):
        return pygame.font.Font("assets/interface/font/joystix.otf", size)

    def display_upgrades(self, window):

        font = self.get_font(12)

        if self.new_ship:
            if self.new_display_timer > 0:
                self.new_display_timer -= 1
                new_upgrade = font.render(self.ship_rarity + " ship upgrade: " + self.ship_name, True, self.ship_name_color)
                new_upgrade_rect = new_upgrade.get_rect(topleft = (300, 900))
                window.blit(new_upgrade, new_upgrade_rect)
        elif self.new_primary:
            if self.new_display_timer > 0:
                self.new_display_timer -= 1
                new_upgrade = font.render(self.primary_rarity + " primary upgrade: " + self.primary_weapon.name, True, self.primary_weapon.name_color)
                new_upgrade_rect = new_upgrade.get_rect(topleft = (300, 900))
                window.blit(new_upgrade, new_upgrade_rect)
        elif self.new_secondary:
            if self.new_display_timer > 0:
                self.new_display_timer -= 1
                new_upgrade = font.render(self.secondary_rarity + " secondary upgrade: " + self.secondary_weapon.name, True, self.secondary_weapon.name_color)
                new_upgrade_rect = new_upgrade.get_rect(topleft = (300, 900))
                window.blit(new_upgrade, new_upgrade_rect)
        elif self.new_shield:
            if self.new_display_timer > 0:
                self.new_display_timer -= 1
                new_upgrade = font.render(self.shield_rarity + " shield upgrade: " + self.shield.name, True, self.shield.name_color)
                new_upgrade_rect = new_upgrade.get_rect(topleft = (300, 900))
                window.blit(new_upgrade, new_upgrade_rect)
        elif self.new_thruster:
            if self.new_display_timer > 0:
                self.new_display_timer -= 1
                new_upgrade = font.render(self.thruster_rarity + " thruster upgrade: " + self.thruster.name, True, self.thruster.name_color)
                new_upgrade_rect = new_upgrade.get_rect(topleft = (300, 900))
                window.blit(new_upgrade, new_upgrade_rect)

        if self.new_display_timer == 0:
            self.new_display_timer = 120
            self.new_ship = False
            self.new_primary = False
            self.new_secondary = False
            self.new_shield = False
            self.new_thruster = False

    def render(self, window):
        if not self.disabled:
            window.blit(self.img, (self.pos_x, self.pos_y))
            self.primary_weapon.render(window)
            self.secondary_weapon.render(window)
            self.thruster.render(window)
            self.shield.render(window)
            self.healthbar(window)
            self.shield.healthbar(window)
            self.display_upgrades(window)
        
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (300, 950, 400, 20))
        pygame.draw.rect(window, (0, 255, 0), (300, 950, 400 * (self.health_cur / self.health_max), 20))

    def hit(self, damage):
        if self.shield.health_cur > 0:
            self.shield.hit(damage)
        else: 
            self.health_cur -= damage
        if self.health_cur <= 0 and not self.dead:
            self.death_shock.play()
            self.dead = True

    def kill(self):
        self.disabled = True
        self.death_shock.stop()
        self.death_sound.play()
        return ShipExplosion(self.pos_x - 25, self.pos_y - 20)

    def refil_ammo(self):
        self.secondary_weapon.refil_ammo()