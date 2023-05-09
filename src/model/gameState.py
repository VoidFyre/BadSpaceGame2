from src.model import *
from pygame import *

class GameState():
    def __init__(self):
        self.player = None
        self.projectiles = []
        self.enemies = []
        self.upgrades = []
        self.powerups = []
        self.player_kills = 0
        self.player_score = 0
        self.wave_counter = 0

    

    def update(self):
        pass