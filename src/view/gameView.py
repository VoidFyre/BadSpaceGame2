import pygame

class GameView():
    def __init__(self, window, game_state):
        self.window = window
        self.game_state = game_state
        self.bg_1 = pygame.transform.scale(pygame.image.load("assets/interface/background/small_stars.png"), (1000, 1000)).convert_alpha()
        self.bg_2 = pygame.transform.scale(pygame.image.load("assets/interface/background/large_stars.png"), (1000, 1000)).convert_alpha()
        self.bg_3 = pygame.transform.scale(pygame.image.load("assets/interface/background/space_clouds_1.png"), (1000, 1000)).convert_alpha()
        self.bg_4 = pygame.transform.scale(pygame.image.load("assets/interface/background/space_clouds_2.png"), (1000, 1000)).convert_alpha()
        self.bg_5 = pygame.transform.scale(pygame.image.load("assets/interface/background/space_clouds_3.png"), (1000, 1000)).convert_alpha()
        self.scroll_1 = 0
        self.scroll_2 = 0
        self.scroll_3 = 0
        self.scroll_4 = 0
        self.scroll_5 = 0

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
        pygame.display.set_caption("Bad Things From Outer Space: The Game 2")
        self.draw_background()
        self.game_state.player.render(self.window)

        pygame.event.set_grab(True)
        pygame.mouse.set_pos(500, 500)

        big_font = self.get_font(100)

        if self.game_state.game_start_timer >= 120:
            start_timer = big_font.render("3", True, "White")
            start_timer_rect = start_timer.get_rect(center = (500, 500))
            self.window.blit(start_timer, start_timer_rect)
        elif self.game_state.game_start_timer >= 60:
            start_timer = big_font.render("2", True, "White")
            start_timer_rect = start_timer.get_rect(center = (500, 500))
            self.window.blit(start_timer, start_timer_rect)
        elif self.game_state.game_start_timer > 0:
            start_timer = big_font.render("1", True, "White")
            start_timer_rect = start_timer.get_rect(center = (500, 500))
            self.window.blit(start_timer, start_timer_rect)

        for proj in self.game_state.projectiles:
            proj.render(self.window)

        for enemy in self.game_state.enemies:
            enemy.render(self.window)

        for explosion in self.game_state.explosions:
            explosion.render(self.window)

        for health_pack in self.game_state.health_packs:
            health_pack.render(self.window)

        for ammo_pack in self.game_state.ammo_packs:
            ammo_pack.render(self.window)

        for upgrade in self.game_state.upgrades:
            upgrade.render(self.window)

        for ast in self.game_state.asteroids:
            ast.render(self.window)

        font = self.get_font(20)

        ammo_counter = font.render("Ammo: " + str(self.game_state.player.secondary_weapon.ammo) + "/" + str(self.game_state.player.secondary_weapon.max_ammo), True, "White")
        ammo_counter_rect = ammo_counter.get_rect(topleft = (750, 920))

        wave_display = font.render("Wave: " + str(self.game_state.wave_counter), True, "White")
        wave_display_rect = wave_display.get_rect(topleft = (750, 50))

        remaining_enemies = font.render("Enemies: " + str(len(self.game_state.enemies)), True, "White")
        remaining_enemies_rect = remaining_enemies.get_rect(topleft = (750, 80))

        score = font.render("Score: " + str(self.game_state.player_score), True, "White")
        score_rect = score.get_rect(topleft = (50, 50))

        self.window.blit(ammo_counter, ammo_counter_rect)
        self.window.blit(wave_display, wave_display_rect)
        self.window.blit(remaining_enemies, remaining_enemies_rect)
        self.window.blit(score, score_rect)
        
        pygame.display.update()