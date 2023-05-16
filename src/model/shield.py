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
        self.recharge_sound = pygame.mixer.Sound("assets/sound/shield_recharge.mp3")
        self.hit_sound = pygame.mixer.Sound("assets/sound/shield_hit.wav")
        self.blink_timer = 0

    def update(self, pos: tuple):
        if self.cooldown > 0:
            self.cooldown -= 1

        elif self.health_cur < self.health_max:
            self.health_cur += 1

        if self.broken:
            self.active = False
            self.broken = False
            self.cooldown = 180
            self.recharge_sound.play()

        if self.health_cur >= 0:
            self.active = True

        self.pos_x = pos[0]
        self.pos_y = pos[1]
        
    def hit(self, damage):
        self.cooldown = 60
        self.hit_sound.play()
        self.health_cur -= damage
        if self.health_cur <= 0:
            self.broken = True

    def healthbar(self, window):
        if self.active:
            pygame.draw.rect(window, (0, 0, 255), (300, 960, 400 * (self.health_cur / self.health_max), 10))
        else:
            if self.blink_timer < 10:
                self.blink_timer += 1
            else:
                self.blink_timer = 0

            if self.blink_timer >= 0 and self.blink_timer < 5:
                pygame.draw.rect(window, (255, 0, 0), (300, 960, 400, 10))
            if self.blink_timer >= 5:
                pygame.draw.rect(window, (0, 0, 255), (300, 960, 400, 10))

    def render(self, window):
        if self.active:
            window.blit(self.img, (self.pos_x - 10, self.pos_y - 10))
        else:
            pass
