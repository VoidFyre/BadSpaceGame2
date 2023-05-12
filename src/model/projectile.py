from src.model.objectMovable import ObjectMovable

class Projectile(ObjectMovable):
    def __init__(self, pos_x, pos_y, speed:int, img, owner:str, window_size:tuple, damage:int):
        self.owner = owner
        self.damage = damage
        super().__init__(pos_x, pos_y, speed, img, window_size)

    def update(self):
        super().update()
        if self.owner == "player":
            self.move_up()

        if self.owner == "enemy":
            self.move_down()