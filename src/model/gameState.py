from src.model.player import Player
from src.model.beam import Beam
from src.model.weaponBeam import WeaponBeam
from src.model.projectileExploding import ProjectileExploding
from src.model.enemy import Enemy
from src.model.healthPack import HealthPack
from src.model.ammoPack import AmmoPack
from src.model.upgrade import Upgrade
from src.model.asteroid import Asteroid
import math
import pygame
import random

class GameState():
    def __init__(self, window_size: tuple, scores):
        self.scores = scores
        self.player = Player(465, 800, window_size)
        self.enemies = []
        self.projectiles = []
        self.explosions = []
        self.health_packs = []
        self.ammo_packs = []
        self.upgrades = []
        self.asteroids = []
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
        self.game_lost = False
        self.game_start_timer = 180
        self.asteroid_timer = 1200
        self.death_timer = 300

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
            if isinstance(self.player.primary_weapon, WeaponBeam):
                proj = self.player.shoot_primary()
                self.player.primary_weapon.shooting = True
                if proj is not None:
                    self.projectiles.append(proj)
            else:
                proj = self.player.shoot_primary()
                if proj is not None:
                    self.projectiles.append(proj)

        elif isinstance(self.player.primary_weapon, WeaponBeam):
            self.player.primary_weapon.shooting = False

        if mouse[2]:
            proj = self.player.shoot_secondary()
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

            if not isinstance(proj, Beam):
                proj.update()
                if proj.disabled:
                    if proj in self.projectiles:
                        self.projectiles.remove(proj)

                elif proj.owner == "enemy":
                    if proj.collision(self.player):
                        self.player.hit(proj.damage)
                        proj.hit()
                        
                elif proj.owner == "player":
                    for enemy in self.enemies:
                        if proj.collision(enemy):
                            enemy.hit(proj.damage)
                            proj.hit()
                            if isinstance(proj, ProjectileExploding):
                                proj.exp_sound.play()
                                self.explosions.append(proj.explode())
                            
            else:
                if not proj.disabled:
                    for enemy in self.enemies:
                        if proj.collision(enemy):
                            enemy.hit(proj.damage)
                            proj.hit()

    def explosion_enemy_collision_check(self):
        for explosion in self.explosions:
            explosion.update()
            if explosion.disabled:
                if explosion in self.explosions:
                    self.explosions.remove(explosion)

            if explosion.active:
                for enemy in self.enemies:
                    if explosion.collision(enemy):
                        enemy.hit(explosion.damage)

                explosion.active = False

    def player_enemy_collision_check(self):
        for enemy in self.enemies:
            if enemy.collision(self.player):
                self.player.hit(self.player.health_max / 2 + 10)
                enemy.hit(enemy.health_max)

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

                health_pack.sound.play()
                health_pack.disabled = True

    def update_ammo_packs(self):
        for ammo_pack in self.ammo_packs:
            ammo_pack.update()
            if ammo_pack.disabled:
                if ammo_pack in self.ammo_packs:
                    self.ammo_packs.remove(ammo_pack)
            elif ammo_pack.collision(self.player):
                self.player.refil_ammo()
                ammo_pack.sound.play()
                ammo_pack.disabled = True

    def update_upgrades(self):
        for upgrade in self.upgrades:
            upgrade.update()
            if upgrade.disabled:
                if upgrade in self.upgrades:
                    self.upgrades.remove(upgrade)
            elif upgrade.collision(self.player):
                upgrade.sound.play()
                upgrade.random_upgrade(self.player)
                upgrade.disabled = True

    def update_asteroids(self):
        for ast in self.asteroids:
            ast.update()
            if ast.disabled:
                if ast in self.asteroids:
                    self.asteroids.remove(ast)
            
            if ast.collision(self.player):
                self.player.hit(ast.health)
                ast.hit(self.player.health_cur)

            for proj in self.projectiles:
                if proj.owner == "player":
                    if proj.collision(ast):
                        proj.hit()
                        ast.hit(proj.damage)
                
    def spawn_asteroid(self):
        x = random.randint(0, 900)
        self.asteroids.append(Asteroid(x, -200, self.window_size))

    def update_score(self, rarity):
        if rarity == "common":
            self.player_score += math.ceil(1 * (1 + (0.1 * self.wave_counter)))
        if rarity == "uncommon":
            self.player_score += math.ceil(2 * (1 + (0.1 * self.wave_counter)))
        if rarity == "rare":
            self.player_score += math.ceil(3 * (1 + (0.1 * self.wave_counter)))
        if rarity == "epic":
            self.player_score += math.ceil(4 * (1 + (0.1 * self.wave_counter)))
        if rarity == "legendary":
            self.player_score += math.ceil(5 * (1 + (0.1 * self.wave_counter)))

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()
            if enemy.cooldown <= 0:
                randint = random.randint(0, 100)
                if randint <= 30:
                    self.projectiles.append(enemy.shoot())
                    enemy.cooldown = 60
                else:
                    enemy.cooldown = 30
            else:
                enemy.cooldown -= 1
            if enemy.disabled:
                self.update_score(enemy.rarity)
                self.drop_item(enemy.pos_x, enemy.pos_y, enemy.rarity)
                self.explosions.append(enemy.death())
                if enemy in self.enemies:
                    self.enemies.remove(enemy)

    def update(self):
        if self.game_start_timer >= 1:
            self.game_start_timer -= 1

        else:
            if self.asteroid_timer > 0:
                self.asteroid_timer -= 1
            else:
                self.spawn_asteroid()
                self.asteroid_timer = random.randint(800, 1600)
            self.spawn_enemy()

            self.get_input()
            self.player.update()

            self.projectile_enemy_collision_check()
            self.explosion_enemy_collision_check()
            self.player_enemy_collision_check()
            self.update_enemies()
            self.update_upgrades()
            self.update_health_packs()
            self.update_ammo_packs()
            self.update_asteroids()

            if self.player.dead:
                if self.death_timer > 0:
                    self.death_timer -= 1
                else:
                    self.game_lost = True

                if self.death_timer == 150:
                    self.explosions.append(self.player.kill())
                

                self.scores.write_scores(self.player_score)
        