from src.model.projectile import Projectile
from src.model.projectileExploding import ProjectileExploding

class Weapon():
    def __init__(self, img, proj_img, proj_speed:int, damage:int, cooldown:int, window_size:tuple, sound):
        self.img = img
        self.proj_img = proj_img
        self.proj_speed = proj_speed
        self.damage = damage
        self.pos_x = 0
        self.pos_y = 0
        self.cooldown = cooldown
        self.window_size = window_size
        self.sound = sound

    def shoot(self):
        return Projectile(self.pos_x + 25, self.pos_y, self.proj_speed, self.proj_img, "player", self.window_size, self.damage)
        
    def update(self, pos: tuple):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        
    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))