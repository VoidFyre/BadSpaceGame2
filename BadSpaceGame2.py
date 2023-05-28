from src.controller.gameController import GameController
from src.model.gameState import GameState
from src.view.gameView import GameView
from src.view.mainMenuView import MainMenuView
from src.view.gameOverView import GameOverView
from src.view.pauseMenuView import PauseMenuView
from src.view.optionsView import OptionsView
from src.view.creditsView import CreditsView
from src.model.options import Options
from src.model.scores import Scores
from src.model.sounds import Sounds
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
        options = Options()
        scores = Scores()
        sounds = Sounds(options.volume)
        game_state = GameState(self.window_size, scores, sounds)
        
        # Set up views
        FPS = 60
        game_view = GameView(self.window, game_state)
        options_view = OptionsView(self.window, options, sounds)
        main_menu_view = MainMenuView(self.window, sounds)
        game_over_view = GameOverView(self.window, game_state, scores, sounds)
        pause_menu_view = PauseMenuView(self.window, game_state, sounds)
        credits_view = CreditsView(self.window, sounds)
        views = (game_view, main_menu_view, game_over_view, pause_menu_view, options_view, credits_view)

        # Set up controller
        game_controller = GameController(game_state, views, FPS, options, sounds)

        # Run game
        game_controller.run()
        exit(0)

if __name__ == "__main__":
    BadSpaceGame2().main()