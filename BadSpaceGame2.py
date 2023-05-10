from src.controller.gameController import GameController
from src.model.gameState import GameState
from src.view.gameView import GameView
from src.view.mainMenuView import MainMenuView
from src.view.gameOverView import GameOverView
from src.view.pauseMenuView import PauseMenuView
from src.view.optionsView import OptionsView
from src.model.options import Options
import pygame

class BadSpaceGame2():
    def __init__(self):
        self.game_state = None
        self.window_size = (1000, 1000)
        self.window = pygame.display.set_mode(self.window_size)
        pygame.mixer.pre_init(frequency=44100, size = -16, channels = 1, buffer = 512)
        pygame.mixer.init()

    def main(self):
        # Set up game state, options, and sound
        game_state = GameState(self.window_size)
        options = Options()
        channel = pygame.mixer.find_channel(True)
        channel.set_volume(1.0)
        # Set up views
        FPS = 60
        game_view = GameView(self.window, game_state)
        options_view = OptionsView(self.window, options)
        main_menu_view = MainMenuView(self.window)
        game_over_view = GameOverView(self.window, game_state)
        pause_menu_view = PauseMenuView(self.window, game_state)
        views = (game_view, main_menu_view, game_over_view, pause_menu_view, options_view)

        # Set up controller
        game_controller = GameController(game_state, views, FPS, channel, options)

        # Run game
        game_controller.run()
        exit(0)

if __name__ == "__main__":
    BadSpaceGame2().main()