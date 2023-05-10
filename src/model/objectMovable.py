class ObjectMovable():
    def __init__(self, pos_x, pos_y, speed: int, img, window_size):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.img = img
        self.disabled = False
        self.window_width = window_size[0]
        self.window_height = window_size[1]

    def move_left(self):
        self.pos_x -= self.speed

    def move_right(self):
        self.pos_x += self.speed

    def move_up(self):
        self.pos_y -= self.speed

    def move_down(self):
        self.pos_y += self.speed

    def update(self):
        if self.pos_y > self.window_height or self.pos_y < 0:
            self.disabled = True

    def render(self, window):
        if not self.disabled:
            window.blit(self.img, (self.pos_x, self.pos_y))