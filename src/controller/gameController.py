import pygame, sys
from src.model.player import Player

class GameController():
    def __init__(self, game_state, views, fps):
        self.FPS = fps
        self.game_state = game_state
        self.game_view, self.main_menu_view, self.game_over_view, self.pause_menu_view = views
        self.keep_running = True
        self.view_mode = "main"
        self.game_clock = pygame.time.Clock()

    def run(self):
        while self.keep_running:

            self.game_clock.tick(self.FPS)

            while self.view_mode == "main":
                self.run_main_menu()
                if self.main_menu_view.get_button_pressed() == "play":
                    self.view_mode = "play"

            while self.view_mode == "play":
                self.run_game()
                if self.game_state.pause == True:
                    pygame.quit()
                    sys.exit()

            while self.view_mode == "options":
                pass

            while self.view_mode == "pause":
                pass


    def run_game(self):
        self.game_state.update()
        self.game_view.render()

    def run_main_menu(self):
        self.main_menu_view.run()

    def run_pause_menu(self):
        pass

    def run_game_over_menu(self):
        pass