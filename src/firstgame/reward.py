from game_obj import *
import random


class Reward(GameObj):
    def __init__(self, screen, image_src):
        super().__init__(screen, image_src)
        # 初始化位置
        init_left = random.choice([i for i in range(self.screen_rect.left, self.screen_rect.right - self.rect.width)])
        self.rect.left = init_left
        self.rect.bottom = self.screen_rect.top - self.rect.height

    def take_effect(self, ship):
        pass

    def blit_me(self):
        super().blit_me()
