import sys
import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf
from pygame.sprite import Group
from scoreboard import Scoreboard

def run_game():
    icon=pygame.image.load('images/ship.bmp')
    pygame.display.set_icon(icon)

    pygame.init()
    pygame.mixer.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Aliens Attack")

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    play_button = Button(ai_settings, screen, "Play")
    sb = Scoreboard(ai_settings, screen, stats)
    bullets = Group()
    aliens =  Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()