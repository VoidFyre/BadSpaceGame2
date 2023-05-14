from src.model.player import Player
from src.model.projectileExploding import ProjectileExploding
from src.model.enemy import Enemy
from src.model.healthPack import HealthPack
from src.model.ammoPack import AmmoPack
from src.model.upgrade import Upgrade
import math
import pygame
import random

class GameState():
    def __init__(self, window_size: tuple, channel):
        self.player = Player(500, 900, window_size)
        self.enemies = []
        self.projectiles = []
        self.explosions = []
        self.health_packs = []
        self.ammo_packs = []
        self.upgrades = []
        self.player_kills = 0
        self.player_score = 0
        self.wave_counter = 0
        self.wave_length = 0
        self.wave_delay = 0
        self.enemies_spawned = 0
        self.window_size = window_size
        self.window_width = window_size[0]
        self.window_height = window_size[1]
        self.pause = False
        self.wave_spawned = False
        self.channel = channel
        self.hit = pygame.mixer.Sound("assets/sound/hit.wav")

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
            proj = self.player.shoot_primary(self.channel)
            if proj is not None:
                self.projectiles.append(proj)

        if mouse[2]:
            proj = self.player.shoot_secondary(self.channel)
            if proj is not None:
                self.projectiles.append(proj)

        if keys[pygame.K_ESCAPE]:
            self.pause = True

    def get_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def spawn_enemy(self):
        if len(self.enemies) == 0 and self.wave_spawned:
            if self.wave_delay > 0:
                self.wave_delay -= 1

            else:
                self.enemies_spawned = 0
                self.wave_spawned = False
                self.wave_delay = 120
                self.wave_counter += 1
                self.wave_length += 1

        elif not self.wave_spawned:

            if self.enemies_spawned == self.wave_length:
                self.wave_spawned = True

            while self.enemies_spawned < self.wave_length:
                if self.wave_counter < 5:
                    rarity = random.choice(["common", "uncommon"])
                if self.wave_counter >= 5 and self.wave_counter < 10:
                    rarity = random.choice(["common", "uncommon", "rare"])
                if self.wave_counter >= 10 and self.wave_counter < 15:
                    rarity = random.choice(["common", "uncommon", "rare", "epic"])
                if self.wave_counter >= 15:
                    rarity = random.choice(["common", "uncommon", "rare", "epic", "legendary"])

                enemy = Enemy(random.randrange(100, 850), random.randrange(-400, -100), 2, self.window_size, rarity, self.wave_counter)
                is_valid_pos = True
                for existing_enemy in self.enemies:
                    if self.get_distance(existing_enemy.pos_x, existing_enemy.pos_y, enemy.pos_x, enemy.pos_y) < 200:
                        is_valid_pos = False
                        return

                if is_valid_pos:
                    self.enemies_spawned += 1
                    self.enemies.append(enemy)

    def projectile_enemy_collision_check(self):
        for proj in self.projectiles:
            proj.update()
            if proj.disabled:
                if proj in self.projectiles:
                    self.projectiles.remove(proj)

            elif proj.owner == "enemy":
                if proj.collision(self.player):
                    self.channel.play(self.hit)
                    self.player.health_cur -= proj.damage
                    proj.disabled = True
                    
            elif proj.owner == "player":
                for enemy in self.enemies:
                    if proj.collision(enemy):
                        self.channel.play(self.hit)
                        enemy.health_cur -= proj.damage
                        proj.disabled = True
                        if isinstance(proj, ProjectileExploding):
                            self.channel.play(proj.exp_sound)
                            self.explosions.append(proj.explode())

    def explosion_enemy_collision_check(self):
        for explosion in self.explosions:
            if explosion.removeTime:
                if explosion.timer >= 0:
                    explosion.timer -= 1
                elif explosion in self.explosions:
                    self.explosions.remove(explosion)

            else:
                for enemy in self.enemies:
                    if explosion.collision(enemy):
                        enemy.health_cur -= explosion.damage
                
                explosion.removeTime = True

    def drop_item(self, pos_x, pos_y, rarity):
        rand_num = random.randint(0, 100)
        if rand_num >= 40 and rand_num < 60:
            self.health_packs.append(HealthPack(pos_x, pos_y, self.window_size))
        if rand_num >= 60 and rand_num < 80:
            self.ammo_packs.append(AmmoPack(pos_x, pos_y, self.window_size))
        if rand_num >= 80:
            if rarity != "common":
                self.upgrades.append(Upgrade(pos_x, pos_y, self.window_size, rarity))

    def update_health_packs(self):
        for health_pack in self.health_packs:
            health_pack.update()
            if health_pack.disabled:
                if health_pack in self.health_packs:
                    self.health_packs.remove(health_pack)
            elif health_pack.collision(self.player):
                if self.player.health_cur <= self.player.health_max * 4 / 5:
                    self.player.health_cur += self.player.health_max/5
                else:
                    self.player.health_cur = self.player.health_max

                self.channel.play(health_pack.sound)
                health_pack.disabled = True

    def update_ammo_packs(self):
        for ammo_pack in self.ammo_packs:
            ammo_pack.update()
            if ammo_pack.disabled:
                if ammo_pack in self.ammo_packs:
                    self.ammo_packs.remove(ammo_pack)
            elif ammo_pack.collision(self.player):
                self.player.secondary_weapon.ammo = self.player.secondary_weapon.max_ammo
                self.channel.play(ammo_pack.sound)
                ammo_pack.disabled = True

    def update_upgrades(self):
        for upgrade in self.upgrades:
            upgrade.update()
            if upgrade.disabled:
                if upgrade in self.upgrades:
                    self.upgrades.remove(upgrade)
            elif upgrade.collision(self.player):
                self.channel.play(upgrade.sound)
                upgrade.random_upgrade(self.player)
                upgrade.disabled = True

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()
            if enemy.health_cur <= 0:
                self.drop_item(enemy.pos_x, enemy.pos_y, enemy.rarity)
                enemy.disabled = True
            if enemy.cooldown <= 0:
                randint = random.randint(0, 100)
                if randint <= 50:
                    self.projectiles.append(enemy.shoot())
                    enemy.cooldown = 60
                else:
                    enemy.cooldown = 30
            else:
                enemy.cooldown -= 1
            if enemy.disabled:
                if enemy in self.enemies:
                    self.enemies.remove(enemy)

    def update(self):

        self.spawn_enemy()

        self.get_input()
        self.player.update()

        self.projectile_enemy_collision_check()
        self.explosion_enemy_collision_check()
        self.update_enemies()
        
        self.update_upgrades()
        self.update_health_packs()
        self.update_ammo_packs()
        