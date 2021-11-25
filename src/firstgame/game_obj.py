import pygame
import time

import settings


class GameObj:
    def __init__(self, screen, image_src):
        self.screen = screen
        self.image = pygame.image.load(image_src)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.last_act_time = time.time()

    def blit_me(self):
        # object refresh once per 'interv' frames, so they won't move too fast
        if time.time() - self.last_act_time >= settings.object_flip_interv:
            self.last_act_time = time.time()
            self.move()
        self.screen.blit(self.image, self.rect)

    def move(self):
        pass
