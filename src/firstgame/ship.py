import pygame
import time

from gif_image import *
from game_obj import *


class Ship(GameObj):
    def __init__(self, screen, image_src):
        super().__init__(screen, image_src)

        self.bullet_last_gen_time = time.time()
        self.bullets = []
        self.is_alive = True
        self.power_lvl = 1

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
        pass

    def get_bullets(self):
        return self.bullets

    def power_up(self):
        self.power_lvl += 1

    def die(self):
        self.is_alive = False

    def is_dead_for_good(self):
        return len(self.bullets) == 0 and self.explosion.over
