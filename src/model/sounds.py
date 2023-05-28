import pygame

class Sounds():
    def __init__(self, volume):

        self.background_music = pygame.mixer.music.load("assets/sound/background_music.ogg")
        self.beam_fire = pygame.mixer.Sound("assets/sound/beam_fire.ogg")
        self.button_press = pygame.mixer.Sound("assets/sound/button_press.ogg")
        self.death = pygame.mixer.Sound("assets/sound/death.ogg")
        self.death_shock = pygame.mixer.Sound("assets/sound/death_shock.wav")
        self.denied = pygame.mixer.Sound("assets/sound/denied.wav")
        self.explosion = pygame.mixer.Sound("assets/sound/explosion.wav")
        self.gunshot = pygame.mixer.Sound("assets/sound/gunshot.wav")
        self.health_pack = pygame.mixer.Sound("assets/sound/health_pack.wav")
        self.hit = pygame.mixer.Sound("assets/sound/hit.wav")
        self.laser_fire = pygame.mixer.Sound("assets/sound/laser_fire.ogg")
        self.laser_recharge = pygame.mixer.Sound("assets/sound/laser_recharge.wav")
        self.plasma_shot = pygame.mixer.Sound("assets/sound/plasma_shot.wav")
        self.reload = pygame.mixer.Sound("assets/sound/reload.wav")
        self.rock_break = pygame.mixer.Sound("assets/sound/rock_break.wav")
        self.secondary_fire = pygame.mixer.Sound("assets/sound/secondary_fire.ogg")
        self.shield_hit = pygame.mixer.Sound("assets/sound/shield_hit.wav")
        self.shield_recharge = pygame.mixer.Sound("assets/sound/shield_recharge.mp3")
        self.upgrade = pygame.mixer.Sound("assets/sound/upgrade.ogg")


        self.sound_list = [self.background_music,
                           self.beam_fire,
                           self.button_press,
                           self.death,
                           self.death_shock,
                           self.denied,
                           self.explosion,
                           self.gunshot,
                           self.health_pack,
                           self.hit,
                           self.laser_fire,
                           self.laser_recharge,
                           self.plasma_shot,
                           self.reload,
                           self.rock_break,
                           self.secondary_fire,
                           self.shield_hit,
                           self.shield_recharge,
                           self.upgrade]
        
        #self.changeVolume(volume)

    def changeVolume(self, volume):
        for sound in self.sound_list:
            pass
            #sound.set_volume(volume)