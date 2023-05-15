from src.function.loadImage import loadImage

class ShipExplosion():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = self.load_image("assets/effect/ship_explosion.png", (150, 150))
        self.timer = 20
        self.disabled = False
        self.active = False

    def load_image(self, path:str, size:tuple):
        return loadImage(path, size)
    
    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.disabled = True

    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))

    def collision(self, obj):
        return False