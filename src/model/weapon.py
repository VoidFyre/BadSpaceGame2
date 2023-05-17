from src.model.projectile import Projectile

class Weapon():
    def __init__(self, name:str, name_color:str, img, proj_img, proj_speed:int, damage:int, cooldown:int, window_size:tuple, sound, hit_sound):
        self.name = name
        self.name_color = name_color
        self.img = img
        self.proj_img = proj_img
        self.proj_speed = proj_speed
        self.damage = damage
        self.pos_x = 465
        self.pos_y = 800
        self.cooldown = cooldown
        self.window_size = window_size
        self.sound = sound
        self.hit_sound = hit_sound

    def shoot(self):
        self.sound.play()
        return Projectile(self.pos_x + 15, self.pos_y, self.proj_speed, self.proj_img, "player", self.window_size, self.damage, self.hit_sound)
        
    def update(self, pos: tuple):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        
    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))