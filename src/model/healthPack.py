from src.model.objectMovable import ObjectMovable
import pygame

class HealthPack(ObjectMovable):
    def __init__(self, pos_x, pos_y, window_size):

        self.img = self.load_image("assets/item/first_aid.png", (40, 40))
        self.sound = pygame.mixer.Sound("assets/sound/health_pack.wav")
        super().__init__(pos_x, pos_y, 2, self.img, window_size)

    def update(self):
        super().update()
        self.move_down()