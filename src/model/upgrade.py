from src.model.weapon import Weapon
from src.model.weaponSecondary import WeaponSecondary
from src.model.objectMovable import ObjectMovable
import pygame
import random

class Upgrade(ObjectMovable):
    def __init__(self, pos_x, pos_y, window_size, rarity):
        self.rarity = rarity
        self.sound = pygame.mixer.Sound("assets/sound/upgrade.ogg")
        images = {
            "uncommon": self.load_image("assets/item/upgradeorb/orb_uncommon.png", (30, 30)),
            "rare": self.load_image("assets/item/upgradeorb/orb_rare.png", (30, 30)),
            "epic": self.load_image("assets/item/upgradeorb/orb_epic.png", (30, 30)),
            "legendary": self.load_image("assets/item/upgradeorb/orb_legendary.png", (30, 30))
        }

        super().__init__(pos_x, pos_y, 2, images[rarity], window_size)

    def update(self):
        super().update()
        self.move_down()

    def random_upgrade(self, player):
        rand_num = random.randint(0, 100)
        if rand_num >= 0 and rand_num < 25:
            if player.ship_rarity == "common" or player.ship_rarity == "uncommon":
                player.ship_rarity = self.rarity
                player.health_cur = player.health_max
            
            if player.ship_rarity == "rare" and self.rarity != "uncommon":
                player.ship_rarity = self.rarity
                player.health_cur = player.health_max

            if player.ship_rarity == "epic" and self.rarity == "legendary":
                player.ship_rarity = self.rarity
                player.health_cur = player.health_max
                
        if rand_num >= 30 and rand_num < 50:
            if player.primary_rarity == "common" or player.primary_rarity == "uncommon":
                player.primary_rarity = self.rarity
            
            if player.primary_rarity == "rare" and self.rarity != "uncommon":
                player.primary_rarity = self.rarity

            if player.primary_rarity == "epic" and self.rarity == "legendary":
                player.primary_rarity = self.rarity
        
        if rand_num >= 60 and rand_num < 75:
            if player.secondary_rarity == "common" or player.secondary_rarity == "uncommon":
                player.secondary_rarity = self.rarity
            
            if player.secondary_rarity == "rare" and self.rarity != "uncommon":
                player.secondary_rarity = self.rarity

            if player.secondary_rarity == "epic" and self.rarity == "legendary":
                player.secondary_rarity = self.rarity

        if rand_num >= 75:
            if player.thruster_rarity == "common" or player.thruster_rarity == "uncommon":
                player.thruster_rarity = self.rarity
            
            if player.thruster_rarity == "rare" and self.rarity != "uncommon":
                player.thruster_rarity = self.rarity

            if player.thruster_rarity == "epic" and self.rarity == "legendary":
                player.thruster_rarity = self.rarity