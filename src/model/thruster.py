

class Thruster():
    def __init__(self, img, speed:int, window_size:tuple, special_sound):
        self.img = img
        self.pos_x = 500
        self.pos_y = 900
        self.speed = speed
        self.window_size = window_size
        self.special_sound = special_sound
        
    def update(self, pos: tuple):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        
    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))