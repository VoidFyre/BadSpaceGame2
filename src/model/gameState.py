from src.model.player import Player
import pygame

class GameState():
    def __init__(self, window_size: tuple):
        self.player = Player(500, 900, window_size)
        self.objs = []
        self.player_kills = 0
        self.player_score = 0
        self.wave_counter = 0
        self.window_width = window_size[0]
        self.window_height = window_size[1]
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
            proj = self.player.shoot_primary()
            if proj is not None:
                self.objs.append(proj)

        if mouse[2]:
            proj = self.player.shoot_secondary()
            if proj is not None:
                self.objs.append(proj)

        if keys[pygame.K_ESCAPE]:
            self.pause = True

    def update(self):
        self.get_input()
        self.player.update()
        for obj in self.objs:
            obj.update()
            if obj.disabled:
                if obj in self.objs:
                    self.objs.remove(obj)