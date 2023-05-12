from src.model.weapon import Weapon
from src.model.projectileExploding import ProjectileExploding

class WeaponSecondary(Weapon):
    def __init__(self, img, proj_img, proj_exp_img, proj_speed:int, damage:int, cooldown:int, ammo:int, max_ammo:int, window_size:tuple, sound, exp_sound, exp_dmg):
        super().__init__(img, proj_img, proj_speed, damage, cooldown, window_size, sound)
        self.proj_exp_img = proj_exp_img
        self.pos_x = 0
        self.pos_y = 0
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.exp_sound = exp_sound
        self.exp_dmg = exp_dmg

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            return ProjectileExploding(self.pos_x + 50, self.pos_y, self.proj_speed, self.proj_img, self.proj_exp_img, "player", self.window_size, self.damage, self.exp_dmg, self.exp_sound)