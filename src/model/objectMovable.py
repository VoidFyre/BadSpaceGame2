from src.function.collide import collide
from src.function.loadImage import loadImage
from src.function.flipImage import flipImageVert
import pygame
import math

class ObjectMovable():
    def __init__(self, pos_x, pos_y, speed:int, img, window_size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.base_img = img
        self.img = img
        self.disabled = False
        self.window_size = window_size
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.mask = pygame.mask.from_surface(self.img)
        self.tracking_obj = None
        self.tracking = False
        self.dx = 0
        self.dy = 0

    def move_left(self):
        self.pos_x -= self.speed

    def move_right(self):
        self.pos_x += self.speed

    def move_up(self):
        self.pos_y -= self.speed

    def move_down(self):
        self.pos_y += self.speed

    def move_toward_object(self, obj):
        # Find direction vector (dx, dy) between self and object
        dx, dy = obj.pos_x - self.pos_x, obj.pos_y - self.pos_y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist #Normalize
        angle = 270 - math.atan2(dy, dx) * 180 / math.pi
        self.img = pygame.transform.rotate(self.base_img, angle)
        

        # Move along normalized vector at speed
        self.pos_x += dx * self.speed
        self.pos_y += dy * self.speed
        

    def update(self):
        if self.pos_y > self.window_height or self.pos_y < 0:
            self.disabled = True

    def render(self, window):
        if not self.disabled:
            window.blit(self.img, (self.pos_x, self.pos_y))

    def collision(self, obj):
        return collide(self, obj)
    
    def load_image(self, path:str, size:tuple):
        return loadImage(path, size)
    
    def flip_image_vert(self, path:str, size:tuple):
        return flipImageVert(self.load_image(path, size))