from src.function.loadImage import loadImage

class ShipExplosion():
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.timer = 24
        self.disabled = False
        self.active = False
        anim_1 = self.load_image("assets/effect/ship_explosion/1.png", (100, 100))
        anim_2 = self.load_image("assets/effect/ship_explosion/2.png", (100, 100))
        anim_3 = self.load_image("assets/effect/ship_explosion/3.png", (100, 100))
        anim_4 = self.load_image("assets/effect/ship_explosion/4.png", (100, 100))
        anim_5 = self.load_image("assets/effect/ship_explosion/5.png", (100, 100))
        anim_6 = self.load_image("assets/effect/ship_explosion/6.png", (100, 100))
        self.anim = [anim_1, anim_2, anim_3, anim_4, anim_5, anim_6]
        self.img = anim_1

    def load_image(self, path:str, size:tuple):
        return loadImage(path, size)
    
    def animate(self):
        if self.timer >= 20:
            self.img = self.anim[0]
        if self.timer >= 16 and self.timer < 20:
            self.img = self.anim[1]
        if self.timer >= 12 and self.timer < 16:
            self.img = self.anim[2]
        if self.timer >= 8 and self.timer < 12:
            self.img = self.anim[3]
        if self.timer >= 4 and self.timer < 8:
            self.img = self.anim[4]
        if self.timer >= 0 and self.timer < 4:
            self.img = self.anim[5]
    
    def update(self):
        self.animate()
        self.timer -= 1
        if self.timer == 0:
            self.disabled = True

    def render(self, window):
        window.blit(self.img, (self.pos_x, self.pos_y))

    def collision(self, obj):
        return False