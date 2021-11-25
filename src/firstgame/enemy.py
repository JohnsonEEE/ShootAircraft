import pygame
import random
import time

from ship import *
from bullet import *
import settings


class Enemy(Ship):
    def __init__(self, screen, my_ship):
        super().__init__(screen, 'images/enemy.png')

        # 初始化位置
        init_left = random.choice([i for i in range(self.screen_rect.left, self.screen_rect.right - self.rect.width)])
        self.rect.left = init_left
        self.rect.bottom = self.screen_rect.top - self.rect.height
        self.my_ship = my_ship

        self.explosion = GIFImage("images/explode.gif", 1)
        self.stay_start_time = None

    def up(self, is_activate):
        pass

    def down(self, is_activate):
        pass

    def left(self, is_activate):
        pass

    def right(self, is_activate):
        pass

    def shoot(self, is_activate):
        pass

    def gen_bullets(self):
        if time.time() - self.bullet_last_gen_time > settings.enemy_bullet_gen_interv:
            # arithmetic of bullet's direction
            tria_x = self.my_ship.rect.x - self.rect.x
            tria_y = self.my_ship.rect.y - self.rect.y if self.my_ship.rect.y > self.rect.y else 0
            x_speed = (tria_x / (abs(tria_x) + tria_y)) * settings.enemy_bullet_speed if abs(tria_x) + tria_y != 0 else 0
            y_speed = settings.enemy_bullet_speed - abs(x_speed)
            if y_speed < 1:
                x_speed -= 1
                y_speed = 1

            bullet = Bullet(self.screen, x_speed, y_speed, bullet_src_2)
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.bottom
            self.bullets.append(bullet)
            self.bullet_last_gen_time = time.time()

    def blit_me(self):
        if self.is_alive:
            super().blit_me()
            self.gen_bullets()
        elif self.explosion.over is False:
            self.explosion.render(self.screen, (self.rect.left, self.rect.top))

        for bullet in reversed(self.bullets):
            bullet.blit_me()
            if bullet.rect.top > self.screen_rect.bottom:
                self.bullets.remove(bullet)

    def move(self):
        if self.is_alive:
            if self.stay_start_time is None and self.rect.top >= settings.enemy_stay_top_position:
                self.stay_start_time = time.time()
            if self.stay_start_time is None or time.time() - self.stay_start_time > settings.enemy_stay_time:
                self.rect.y += settings.enemy_ship_speed
