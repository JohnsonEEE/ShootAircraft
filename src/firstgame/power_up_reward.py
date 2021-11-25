from reward import *
import obj_utils
import settings


class PowerUpReward(Reward):
    def __init__(self, screen, image_src):
        super().__init__(screen, image_src)

    def take_effect(self, ship):
        if obj_utils.is_collided(self, ship):
            pass

    def move(self):
        self.rect.y += settings.reward_speed
