import pygame

class Shield():
    def __init__(self, img, health:int):
        self.pos_x = 500
        self.pos_y = 900
        self.img = img
        self.health_max = health
        self.health_cur = health
        self.active = True
        self.cooldown = 0
        self.broken = False
        self.status = "Active"
        self.recharge_sound = pygame.mixer.Sound("assets/sound/shield_recharge.mp3")
        self.hit_sound = pygame.mixer.Sound("assets/sound/shield_hit.wav")

    def update(self, pos: tuple):
        if self.cooldown > 0:
            self.cooldown -= 1

        elif self.health_cur <= self.health_max:
            self.health_cur += 1

        if self.broken:
            self.status = "Recharging"
            self.active = False
            self.broken = False
            self.cooldown = 180
            self.recharge_sound.play()

        if self.health_cur >= 0:
            self.status = "Active"
            self.active = True

        self.pos_x = pos[0]
        self.pos_y = pos[1]
        
    def hit(self, damage):
        self.cooldown = 60
        self.hit_sound.play()
        self.health_cur -= damage
        if self.health_cur <= 0:
            self.broken = True

    def render(self, window):
        if self.active:
            window.blit(self.img, (self.pos_x, self.pos_y))
