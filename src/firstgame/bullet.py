import pygame

from game_obj import *

bullet_src_1 = 'images/bullet1.png'
bullet_src_2 = 'images/bullet2.png'


class Bullet(GameObj):
    def __init__(self, screen, x_speed, y_speed, bullet_img_src):
        super().__init__(screen, bullet_img_src)
        self.image = pygame.image.load(bullet_img_src)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.x_speed = x_speed
        self.y_speed = y_speed

    def blit_me(self):
        super().blit_me()

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
