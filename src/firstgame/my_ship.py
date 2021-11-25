import time

import settings
from bullet import *
from ship import *


class MyShip(Ship):
    def __init__(self, screen):
        super().__init__(screen, 'images/myplanelittle.png')

        # 初始化位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.speed_x = 0
        self.speed_y = 0
        self.is_shooting = False
        self.explosion = GIFImage("images/explode.gif", 5)

    def up(self, is_activate):
        if is_activate:
            self.speed_y -= settings.my_ship_speed
        else:
            self.speed_y += settings.my_ship_speed

    def down(self, is_activate):
        if is_activate:
            self.speed_y += settings.my_ship_speed
        else:
            self.speed_y -= settings.my_ship_speed

    def left(self, is_activate):
        if is_activate:
            self.speed_x -= settings.my_ship_speed
        else:
            self.speed_x += settings.my_ship_speed

    def right(self, is_activate):
        if is_activate:
            self.speed_x += settings.my_ship_speed
        else:
            self.speed_x -= settings.my_ship_speed

    def shoot(self, is_activate):
        self.is_shooting = is_activate

    def gen_bullets(self):
        if self.is_shooting and time.time() - self.bullet_last_gen_time > settings.my_bullet_gen_interv:
            if self.power_lvl == 1:
                self.gen_bullet(0)
            elif self.power_lvl == 2:
                self.gen_bullet(-1)
                self.gen_bullet(1)
            elif self.power_lvl == 3:
                self.gen_bullet(-1)
                self.gen_bullet(0)
                self.gen_bullet(1)
            elif self.power_lvl == 4:
                self.gen_bullet(-2)
                self.gen_bullet(-1)
                self.gen_bullet(1)
                self.gen_bullet(2)
            else:
                self.gen_bullet(-2)
                self.gen_bullet(-1)
                self.gen_bullet(0)
                self.gen_bullet(1)
                self.gen_bullet(2)

            self.bullet_last_gen_time = time.time()

    def gen_bullet(self, x_speed):
        bullet = Bullet(self.screen, x_speed, -settings.my_bullet_speed, bullet_src_1)
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.bottom = self.rect.top
        self.bullets.append(bullet)

    def blit_me(self):
        if self.is_alive:
            super().blit_me()
            self.gen_bullets()
        elif self.explosion.over is False:
            self.explosion.render(self.screen, (self.rect.left, self.rect.top))

        for bullet in reversed(self.bullets):
            bullet.blit_me()
            if bullet.rect.bottom < self.screen_rect.top:
                self.bullets.remove(bullet)

    def move(self):
        if (self.speed_x < 0 and self.rect.left >= self.screen_rect.left) \
                or (self.speed_x > 0 and self.rect.right <= self.screen_rect.right):
            self.rect.x += self.speed_x
        if (self.speed_y > 0 and self.rect.bottom <= self.screen_rect.bottom) \
                or (self.speed_y < 0 and self.rect.top >= self.screen_rect.top):
            self.rect.y += self.speed_y
