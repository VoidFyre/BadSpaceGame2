from src.model.weapon import Weapon
from src.model.weaponSecondary import WeaponSecondary
from src.model.objectMovable import ObjectMovable
import pygame
import random

class Upgrade(ObjectMovable):
    def __init__(self, pos_x, pos_y, window_size, rarity):
        self.rarity = rarity
        self.sound = pygame.mixer.Sound("assets/sound/upgrade.ogg")
        self.choices = ["ship", "primary", "secondary", "thruster", "shield"]
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

    def get_choice(self):
        if self.choices:
            return random.choice(self.choices)
        else:
            return None

    def random_upgrade(self, player):
        while True:
            choice = self.get_choice()
            if choice == None:
                break
            if choice == "primary":
                if self.rarity == "uncommon":
                    if player.primary_rarity == "common":
                        player.primary_rarity = "uncommon"
                        break
                    else:
                        self.choices.remove("primary")
                        continue
                if self.rarity == "rare":
                    if player.primary_rarity == "common":
                        player.primary_rarity = "uncommon"
                        break

                    elif player.primary_rarity == "uncommon":
                        player.primary_rarity = "rare"
                        break
                    else:
                        self.choices.remove("primary")
                        continue
                if self.rarity == "epic":
                    if player.primary_rarity == "common":
                        player.primary_rarity = "uncommon"
                        break

                    elif player.primary_rarity == "uncommon":
                        player.primary_rarity = "rare"
                        break

                    elif player.primary_rarity == "rare":
                        player.primary_rarity = "epic"
                        break

                    else:
                        self.choices.remove("primary")
                        continue

                if self.rarity == "legendary":
                    if player.primary_rarity == "common":
                        player.primary_rarity = "uncommon"
                        break

                    elif player.primary_rarity == "uncommon":
                        player.primary_rarity = "rare"
                        break

                    elif player.primary_rarity == "rare":
                        player.primary_rarity = "epic"
                        break

                    elif player.primary_rarity == "epic":
                        player.primary_weapon.shooting = False
                        player.primary_weapon.beam.disabled = True
                        player.primary_weapon.stop_shoot_sound()
                        player.primary_rarity = "legendary"
                        break

                    else:
                        self.choices.remove("primary")
                        continue

            if choice == "secondary":
                if self.rarity == "uncommon":
                    if player.secondary_rarity == "common":
                        player.secondary_rarity = "uncommon"
                        break

                    else:
                        self.choices.remove("secondary")
                        continue
                if self.rarity == "rare":
                    if player.secondary_rarity == "common":
                        player.secondary_rarity = "uncommon"
                        break

                    elif player.secondary_rarity == "uncommon":
                        player.secondary_rarity = "rare"
                        break

                    else:
                        self.choices.remove("secondary")
                        continue
                if self.rarity == "epic":
                    if player.secondary_rarity == "common":
                        player.secondary_rarity = "uncommon"
                        break

                    elif player.secondary_rarity == "uncommon":
                        player.secondary_rarity = "rare"
                        break

                    elif player.secondary_rarity == "rare":
                        player.secondary_rarity = "epic"
                        break

                    else:
                        self.choices.remove("secondary")
                        continue

                if self.rarity == "legendary":
                    if player.secondary_rarity == "common":
                        player.secondary_rarity = "uncommon"
                        break

                    elif player.secondary_rarity == "uncommon":
                        player.secondary_rarity = "rare"
                        break

                    elif player.secondary_rarity == "rare":
                        player.secondary_rarity = "epic"
                        break

                    elif player.secondary_rarity == "epic":
                        player.secondary_rarity = "legendary"
                        break

                    else:
                        self.choices.remove("secondary")
                        continue

            if choice == "thruster":
                if self.rarity == "uncommon":
                    if player.thruster_rarity == "common":
                        player.thruster_rarity = "uncommon"
                        break

                    else:
                        self.choices.remove("thruster")
                        continue
                if self.rarity == "rare":
                    if player.thruster_rarity == "common":
                        player.thruster_rarity = "uncommon"
                        break

                    elif player.thruster_rarity == "uncommon":
                        player.thruster_rarity = "rare"
                        break

                    else:
                        self.choices.remove("thruster")
                        continue
                if self.rarity == "epic":
                    if player.thruster_rarity == "common":
                        player.thruster_rarity = "uncommon"
                        break

                    elif player.thruster_rarity == "uncommon":
                        player.thruster_rarity = "rare"
                        break

                    elif player.thruster_rarity == "rare":
                        player.thruster_rarity = "epic"
                        break

                    else:
                        self.choices.remove("thruster")
                        continue

                if self.rarity == "legendary":
                    if player.thruster_rarity == "common":
                        player.thruster_rarity = "uncommon"
                        break

                    elif player.thruster_rarity == "uncommon":
                        player.thruster_rarity = "rare"
                        break

                    elif player.thruster_rarity == "rare":
                        player.thruster_rarity = "epic"
                        break

                    elif player.thruster_rarity == "epic":
                        player.thruster_rarity = "legendary"
                        break

                    else:
                        self.choices.remove("thruster")
                        continue

            if choice == "ship":
                if self.rarity == "uncommon":
                    if player.ship_rarity == "common":
                        player.ship_rarity = "uncommon"
                        break

                    else:
                        self.choices.remove("ship")
                        continue
                if self.rarity == "rare":
                    if player.ship_rarity == "common":
                        player.ship_rarity = "uncommon"
                        break

                    elif player.ship_rarity == "uncommon":
                        player.ship_rarity = "rare"
                        break

                    else:
                        self.choices.remove("ship")
                        continue
                if self.rarity == "epic":
                    if player.ship_rarity == "common":
                        player.ship_rarity = "uncommon"
                        break

                    elif player.ship_rarity == "uncommon":
                        player.ship_rarity = "rare"
                        break

                    elif player.ship_rarity == "rare":
                        player.ship_rarity = "epic"
                        break

                    else:
                        self.choices.remove("ship")
                        continue

                if self.rarity == "legendary":
                    if player.ship_rarity == "common":
                        player.ship_rarity = "uncommon"
                        break

                    elif player.ship_rarity == "uncommon":
                        player.ship_rarity = "rare"
                        break

                    elif player.ship_rarity == "rare":
                        player.ship_rarity = "epic"
                        break

                    elif player.ship_rarity == "epic":
                        player.ship_rarity = "legendary"
                        break

                    else:
                        self.choices.remove("ship")
                        continue

            if choice == "shield":
                if self.rarity == "uncommon":
                    if player.shield_rarity == "common":
                        player.shield_rarity = "uncommon"
                        break

                    else:
                        self.choices.remove("shield")
                        continue
                if self.rarity == "rare":
                    if player.shield_rarity == "common":
                        player.shield_rarity = "uncommon"
                        break

                    elif player.shield_rarity == "uncommon":
                        player.shield_rarity = "rare"
                        break

                    else:
                        self.choices.remove("shield")
                        continue
                if self.rarity == "epic":
                    if player.shield_rarity == "common":
                        player.shield_rarity = "uncommon"
                        break

                    elif player.shield_rarity == "uncommon":
                        player.shield_rarity = "rare"
                        break

                    elif player.shield_rarity == "rare":
                        player.shield_rarity = "epic"
                        break

                    else:
                        self.choices.remove("shield")
                        continue

                if self.rarity == "legendary":
                    if player.shield_rarity == "common":
                        player.shield_rarity = "uncommon"
                        break

                    elif player.shield_rarity == "uncommon":
                        player.shield_rarity = "rare"
                        break

                    elif player.shield_rarity == "rare":
                        player.shield_rarity = "epic"
                        break

                    elif player.shield_rarity == "epic":
                        player.shield_rarity = "legendary"
                        break

                    else:
                        self.choices.remove("shield")
                        continue