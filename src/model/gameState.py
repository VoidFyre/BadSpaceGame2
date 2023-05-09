from src.model.player import Player
import pygame

class GameState():
    def __init__(self, window_size):
        self.player = Player(500, 900)
        self.objs = []
        self.player_kills = 0
        self.player_score = 0
        self.wave_counter = 0
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.player.window_height = self.window_height
        self.player.window_width = self.window_width
        self.pause = False

    def get_input(self):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        if keys[pygame.K_a]:  # left
            self.player.move_left()

        if keys[pygame.K_d]:  # right
            self.player.move_right()

        if keys[pygame.K_w]:  # up
            self.player.move_up()

        if keys[pygame.K_s]:  # down
            self.player.move_down()

        if mouse[0]:
            self.player.shoot_primary()

        if mouse[2]:
            self.player.shoot_secondary()

        if keys[pygame.K_ESCAPE]:
            self.pause = True

    def update(self):
        self.get_input()