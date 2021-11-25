from main_engine import *


def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    engine = MainEngine(screen)

    while True:
        engine.handler_events()
        engine.gen_enemy()
        engine.gen_reward()
        engine.handler_obj_collide()
        engine.blit_everything()


run_game()
