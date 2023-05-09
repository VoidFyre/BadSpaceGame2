from src.controller.gameController import GameController
from src.model.gameState import GameState
from src.view.gameView import GameView
from src.view.mainMenuView import MainMenuView
from src.view.gameOverView import GameOverView
from src.view.pauseMenuView import PauseMenuView
import pygame

class Main():
    def __init__(self):
        self.game_state = None
        self.window_size = (1000, 1000)
        self.window = pygame.display.set_mode(self.window_size)

    def main(self):
        # Set up game state
        game_state = GameState(self.window_size)

        # Set up views
        FPS = 60
        game_view = GameView(self.window, game_state)
        main_menu_view = MainMenuView(self.window)
        game_over_view = GameOverView(self.window, game_state)
        pause_menu_view = PauseMenuView(self.window, game_state)
        views = (game_view, main_menu_view, game_over_view, pause_menu_view)

        # Set up controller
        game_controller = GameController(game_state, views, FPS)

        # Run game
        game_controller.run()
        exit(0)

if __name__ == "__main__":
    Main().main()