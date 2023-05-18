import pygame, sys
from src.model.player import Player

class GameController():
    def __init__(self, game_state, views: list, fps: int, options):
        self.FPS = fps
        self.game_state = game_state
        self.game_view, self.main_menu_view, self.game_over_view, self.pause_menu_view, self.options_view, self.credits_view = views
        self.keep_running = True
        self.view_mode = "main"
        self.game_clock = pygame.time.Clock()
        self.music = "assets/sound/background_music.ogg"
        self.options = options

    def reset(self):
        self.game_state.__init__((self.game_state.window_width, self.game_state.window_height), self.game_state.scores)

    def run(self):
        pygame.mixer.music.set_volume(self.options.volume)
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(-1)

        while self.keep_running:

            

            self.game_clock.tick(self.FPS)

            if self.view_mode == "main":
                self.run_main_menu()

            if self.view_mode == "play":
                self.run_game()

            if self.view_mode == "options":
                self.run_options_menu()
                

            if self.view_mode == "pause":
                self.run_pause_menu()

            if self.view_mode == "gameover":
                self.run_game_over_menu()

            if self.view_mode == "credits":
                self.run_credits()


    def run_game(self):
        self.game_state.update()
        self.game_view.run()
        if self.game_state.pause == True:
            self.view_mode = "pause"
            pygame.mixer.stop()
            self.game_state.pause = False

        if self.game_state.game_lost:
            self.view_mode = "gameover"


    def run_main_menu(self):
        self.main_menu_view.run()
        if self.main_menu_view.button_pressed == "play":
            self.main_menu_view.button_pressed = None
            self.view_mode = "play"
            
        if self.main_menu_view.button_pressed == "options":
            self.main_menu_view.button_pressed = None
            self.view_mode = "options"

        if self.main_menu_view.button_pressed == "credits":
            self.main_menu_view.button_pressed = None
            self.view_mode = "credits"

    def run_pause_menu(self):
        self.pause_menu_view.run()
        if self.pause_menu_view.button_pressed == "resume":
            self.pause_menu_view.button_pressed = None
            self.view_mode = "play"

        if self.pause_menu_view.button_pressed == "restart":
            self.pause_menu_view.button_pressed = None
            self.reset()
            self.view_mode = "play"

        if self.pause_menu_view.button_pressed == "main":
            self.pause_menu_view.button_pressed = None
            self.reset()
            self.view_mode = "main"

    def run_game_over_menu(self):
        self.game_over_view.run()
        if self.game_over_view.button_pressed == "main":
            self.game_over_view.button_pressed = None
            self.reset()
            self.view_mode = "main"

        if self.game_over_view.button_pressed == "restart":
            self.game_over_view.button_pressed = None
            self.reset()
            self.view_mode = "play"

    def run_options_menu(self):
        self.options_view.run()
        if self.options_view.button_pressed == "back":
            self.options_view.button_pressed = None
            self.view_mode = "main"

    def run_credits(self):
        self.credits_view.run()
        if self.credits_view.button_pressed == "back":
            self.credits_view.button_pressed = None
            self.view_mode = "main"