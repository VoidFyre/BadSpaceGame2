import pygame, sys
from src.model.button import Button

class GameOverView():
    def __init__(self, window, game_state, scores):
        self.game_state = game_state
        self.window = window
        self.scores = scores
        pygame.init()

        # Setting up background images
        self.bg_1 = pygame.transform.scale(pygame.image.load("assets/interface/background/small_stars.png"), (1000, 1000)).convert_alpha()
        self.bg_2 = pygame.transform.scale(pygame.image.load("assets/interface/background/large_stars.png"), (1000, 1000)).convert_alpha()
        self.bg_3 = pygame.transform.scale(pygame.image.load("assets/interface/background/space_clouds_1.png"), (1000, 1000)).convert_alpha()
        self.bg_4 = pygame.transform.scale(pygame.image.load("assets/interface/background/space_clouds_2.png"), (1000, 1000)).convert_alpha()
        self.bg_5 = pygame.transform.scale(pygame.image.load("assets/interface/background/space_clouds_3.png"), (1000, 1000)).convert_alpha()
        self.cursor_image = pygame.transform.scale(pygame.image.load("assets/interface/cursor/cursor.png"), (60, 60))
        self.cursor = self.cursor_image.get_rect()
        self.button_pressed = None
        self.scroll_1 = 0
        self.scroll_2 = 0
        self.scroll_3 = 0
        self.scroll_4 = 0
        self.scroll_5 = 0
        self.button_sound = pygame.mixer.Sound("assets/sound/button_press.ogg")

    def get_button_pressed(self):
        pressed = self.button_pressed
        self.button_pressed = None
        return pressed

    def get_font(self, size):
        return pygame.font.Font("assets/interface/font/joystix.otf", size)
    
    def draw_background(self):

        i = 0
        while i < 2:
            self.window.blit(self.bg_1, (0, ((self.bg_1.get_height() * -i)  + self.scroll_1)))
            i += 1

        i = 0
        while i < 2:
            self.window.blit(self.bg_2, (0, ((self.bg_2.get_height() * -i)  + self.scroll_2)))
            i += 1

        i = 0
        while i < 2:
            self.window.blit(self.bg_3, (0, ((self.bg_3.get_height() * -i)  + self.scroll_3)))
            i += 1

        i = 0
        while i < 2:
            self.window.blit(self.bg_4, (0, ((self.bg_4.get_height() * -i)  + self.scroll_4)))
            i += 1

        i = 0
        while i < 2:
            self.window.blit(self.bg_5, (0, ((self.bg_5.get_height() * -i)  + self.scroll_5)))
            i += 1

        self.scroll_1 += 1
        self.scroll_2 += 1.5
        self.scroll_3 += 2
        self.scroll_4 += 2.5
        self.scroll_5 += 3

        if abs(self.scroll_1) > self.bg_1.get_height():
            self.scroll_1 = 0

        if abs(self.scroll_2) > self.bg_2.get_height():
            self.scroll_2 = 0

        if abs(self.scroll_3) > self.bg_3.get_height():
            self.scroll_3 = 0

        if abs(self.scroll_4) > self.bg_4.get_height():
            self.scroll_4 = 0

        if abs(self.scroll_5) > self.bg_5.get_height():
            self.scroll_5 = 0



    def run(self):
        pygame.display.set_caption("Bad Things From Outer Space: The Game 2 GAME OVER")

        pygame.mouse.set_visible(False)
        
        self.draw_background()

        menu_mouse_pos = pygame.mouse.get_pos()

        base_button_image = pygame.transform.scale(pygame.image.load("assets/interface/button/button_long.png"), (300, 100))
        hovering_button_image = pygame.transform.scale(pygame.image.load("assets/interface/button/button_long_hovering.png"), (300, 100))

        main_menu_button = Button(base_image = base_button_image,
                                hovering_image = hovering_button_image,
                                pos = (200, 350),
                                text_input = "MAIN MENU",
                                font = self.get_font(30),
                                base_color = "Black",
                                hovering_color = "White")
        
        restart_button = Button(base_image = base_button_image,
                                hovering_image = hovering_button_image,
                                pos = (200, 500),
                                text_input = "RESTART",
                                font = self.get_font(30),
                                base_color = "Black",
                                hovering_color = "White")
        
        quit_button = Button(base_image = base_button_image,
                                hovering_image = hovering_button_image,
                                pos = (200, 650),
                                text_input = "QUIT",
                                font = self.get_font(30),
                                base_color = "Black",
                                hovering_color = "White")

        for button in [main_menu_button, restart_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(self.window)

        self.cursor.center = menu_mouse_pos

        if pygame.mouse.get_focused():
            self.window.blit(self.cursor_image, self.cursor)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.checkForInput(menu_mouse_pos):
                    self.button_sound.play()
                    self.button_pressed = "main"

                if restart_button.checkForInput(menu_mouse_pos):
                    self.button_sound.play()
                    self.button_pressed = "restart"

                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        font = self.get_font(30)

        score = font.render("Score: " + str(self.game_state.player_score), True, "White")
        score_rect = score.get_rect(center = (650, 400))

        high_score = font.render("High Score: " + str(self.scores.high_score), True, "White")
        high_score_rect = score.get_rect(center = (650, 500))

        self.window.blit(score, score_rect)
        self.window.blit(high_score, high_score_rect)

        pygame.display.update()