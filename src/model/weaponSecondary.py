from src.model.weapon import Weapon
from src.model.projectileExploding import ProjectileExploding

class WeaponSecondary(Weapon):
    def __init__(self, name:str, name_color:str, img, proj_img, proj_exp_anim, proj_speed:int, damage:int, cooldown:int, ammo:int, max_ammo:int, window_size:tuple, sound, exp_sound, exp_dmg, hit_sound, tracking:bool, proj_count:int):
        super().__init__(name, name_color, img, proj_img, proj_speed, damage, cooldown, window_size, sound, None)
        self.proj_exp_anim = proj_exp_anim
        self.proj_count = proj_count
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.exp_sound = exp_sound
        self.exp_dmg = exp_dmg
        self.hit_sound = hit_sound
        self.tracking = tracking

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            self.sound.play()
            projs = []
            count = self.proj_count
            while count > 0:
                proj = ProjectileExploding(self.pos_x + 30, self.pos_y, self.proj_speed, self.proj_img, self.proj_exp_anim, "player", self.window_size, self.damage, self.exp_dmg, self.exp_sound, self.hit_sound, self.tracking)
                projs.append(proj)
                count -= 1
            return projs
        
    def refil_ammo(self):
        if self.ammo < self.max_ammo:
            self.ammo += 1