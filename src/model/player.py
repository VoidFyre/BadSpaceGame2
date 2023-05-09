import pygame, os

class Player():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 5
        self.health_cur = 100
        self.health_max = 100
        self.window_height = None
        self.window_width = None
        self.img = pygame.transform.scale(pygame.image.load("assets/component/ship/ship_common.png"), (100, 100))

    def move_left(self):
        if self.pos_x - self.speed > 0:
            self.pos_x -= self.speed

    def move_right(self):
        if self.pos_x + self.speed + self.img.get_height() < self.window_width:
            self.pos_x += self.speed

    def move_up(self):
        if self.pos_y - self.speed > 0:
            self.pos_y -= self.speed

    def move_down(self):
        if self.pos_y + self.speed + self.img.get_width() < self.window_height:
            self.pos_y += self.speed

    def shoot_primary(self):
        pass

    def shoot_secondary(self):
        pass

    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))