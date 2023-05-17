from src.model.projectile import Projectile
from src.model.explosion import Explosion

class ProjectileExploding(Projectile):
    def __init__(self, pos_x, pos_y, speed:int, img, exp_img, owner:str, window_size:tuple, damage:int, exp_dmg:int, exp_sound, hit_sound, tracking:bool):
        self.exp_img = exp_img
        self.exp_dmg = exp_dmg
        self.exp_sound = exp_sound
        super().__init__(pos_x, pos_y, speed, img, owner, window_size, damage, hit_sound)
        self.tracking = tracking

    def update(self):
        

        if self.tracking and self.tracking_obj is not None:
            if self.tracking_obj.disabled:
                self.tracking = False
            self.move_toward_object(self.tracking_obj)

        elif self.owner == "player":
            self.move_up()

        elif self.owner == "enemy":
            self.move_down()

        if self.pos_y > self.window_height or self.pos_y < 0:
            self.disabled = True

    def explode(self):
        return Explosion(self.pos_x - 250, self.pos_y - 250, self.exp_img, self.exp_dmg)
    