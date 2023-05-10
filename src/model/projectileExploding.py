from src.model.projectile import Projectile

class ProjectileExploding(Projectile):
    def __init__(self, pos_x, pos_y, speed: int, img, exp_img, owner: str, window_size: tuple):
        super().__init__(pos_x, pos_y, speed, img, owner, window_size)
        self.exp_img = exp_img
