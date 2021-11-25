import sys
import pygame

from my_ship import *
from enemy import *
from power_up_reward import *
import obj_utils


class MainEngine:
    def __init__(self, screen):
        self.screen = screen
        self.my_ship = MyShip(screen)
        self.all_enemies = []
        self.all_rewards = []
        self.game_over_font = pygame.font.SysFont(None, 240).render("Game Over", True, (255, 64, 64))
        self.last_enemy_gen_time = time.time()
        self.last_reward_gen_time = time.time()
        self.dead_time = None
        self.bg_image = pygame.image.load(settings.bg_image)

    def handler_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                is_activate = event.type == pygame.KEYDOWN
                if event.key == pygame.K_d:
                    self.my_ship.right(is_activate)
                elif event.key == pygame.K_a:
                    self.my_ship.left(is_activate)
                elif event.key == pygame.K_w:
                    self.my_ship.up(is_activate)
                elif event.key == pygame.K_s:
                    self.my_ship.down(is_activate)
                elif event.key == pygame.K_SPACE:
                    self.my_ship.shoot(is_activate)

    def blit_everything(self):
        self.screen.fill(settings.bg_color)
        self.screen.blit(self.bg_image, self.bg_image.get_rect())
        self.my_ship.blit_me()
        for ship in self.all_enemies:
            ship.blit_me()
        for reward in self.all_rewards:
            reward.blit_me()
        if self.dead_time is not None and time.time() - self.dead_time > settings.game_over_font_delay:
            self.screen.blit(self.game_over_font, [40, 200])

        pygame.display.flip()

    def handler_obj_collide(self):
        # hit enemy
        for my_bullet in reversed(self.my_ship.get_bullets()):
            for enemy in reversed(self.all_enemies):
                if enemy.is_alive and obj_utils.is_collided(my_bullet, enemy):
                    enemy.die()
                    self.my_ship.get_bullets().remove(my_bullet)
                    break
                if enemy.is_alive is False and enemy.is_dead_for_good():
                    self.all_enemies.remove(enemy)

        # I'm hit
        for enemy in self.all_enemies:
            for bullet in reversed(enemy.get_bullets()):
                if self.my_ship.is_alive and obj_utils.is_collided(bullet, self.my_ship):
                    self.my_ship.die()
                    enemy.get_bullets().remove(bullet)
                    self.dead_time = time.time()
                    break

        # get reward
        for reward in reversed(self.all_rewards):
            if self.my_ship.is_alive and obj_utils.is_collided(reward, self.my_ship):
                self.my_ship.power_up()
                self.all_rewards.remove(reward)

    def gen_enemy(self):
        if time.time() - self.last_enemy_gen_time > settings.enemy_gen_interv:
            self.all_enemies.append(Enemy(self.screen, self.my_ship))
            self.last_enemy_gen_time = time.time()
        for i in sorted([i for i in range(len(self.all_enemies))], reverse=True):
            enemy = self.all_enemies[i]
            if enemy.rect.top > self.screen.get_rect().bottom and enemy.is_dead_for_good():
                self.all_enemies.remove(enemy)

    def gen_reward(self):
        if time.time() - self.last_reward_gen_time > settings.reward_gen_interv:
            self.all_rewards.append(PowerUpReward(self.screen, settings.power_up_image_src))
            self.last_reward_gen_time = time.time()
