

class Thruster():
    def __init__(self, name:str, name_color:str, img, speed:int, window_size:tuple, special_sound):
        self.name = name
        self.name_color = name_color
        self.img = img
        self.pos_x = 465
        self.pos_y = 800
        self.speed = speed
        self.window_size = window_size
        self.special_sound = special_sound
        
    def update(self, pos: tuple):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        
    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))