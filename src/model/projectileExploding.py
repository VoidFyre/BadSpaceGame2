from src.model.projectile import Projectile
from src.model.explosion import Explosion

class ProjectileExploding(Projectile):
    def __init__(self, pos_x, pos_y, speed:int, img, exp_img, owner:str, window_size:tuple, damage:int, exp_dmg:int, exp_sound):
        self.exp_img = exp_img
        self.exp_dmg = exp_dmg
        self.exp_sound = exp_sound
        super().__init__(pos_x, pos_y, speed, img, owner, window_size, damage)

    def explode(self):
        return Explosion(self.pos_x - 250, self.pos_y - 250, self.exp_img, self.exp_dmg)