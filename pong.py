# pong.py                   #
# Created by: John Gawlik   #
# Campus ID: 889752424      #
# Due: September 29th, 2018 #
#############################

import pygame
from settings import Settings
from user_paddle import PaddleTop
from user_paddle import PaddleBottom
from user_paddle import PaddleLeft
from comp_paddle import CompPaddleTop
from comp_paddle import CompPaddleRight
from comp_paddle import CompPaddleBottom
from game_stats import GameStats
from ball import Ball
from net import Net
import game_functions as gf
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("PONG")

    # Create sounds for when the paddle is hit.
    user_paddle_hit_sound = pygame.mixer.Sound('sounds/user_paddle_hit.wav')
    comp_paddle_hit_sound = pygame.mixer.Sound('sounds/comp_paddle_hit.wav')

    # Create and instance to store game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Net
    net = Net(screen)

    # Make top paddle:
    paddle_top = PaddleTop(ai_settings, screen)
    paddle_bottom = PaddleBottom(ai_settings, screen)
    paddle_left = PaddleLeft(ai_settings, screen)

    # Make a paddle controlled by the computer.
    comp_paddle_top = CompPaddleTop(ai_settings, screen)
    comp_paddle_right = CompPaddleRight(ai_settings, screen)
    comp_paddle_bottom = CompPaddleBottom(ai_settings, screen)

    # Create the ball
    ball = Ball(ai_settings, screen)

    # Make the play button.
    play_button = Button(screen, "Play")

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, stats, sb, play_button, paddle_top, paddle_bottom, paddle_left,
                        comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball)

        if stats.game_active:
            gf.update_comp_paddle_top(comp_paddle_top, ball)
            gf.update_comp_paddle_right(comp_paddle_right, ball)
            gf.update_comp_paddle_bottom(comp_paddle_bottom, ball)
            gf.update_user_paddle_top(paddle_top)
            gf.update_user_paddle_bottom(paddle_bottom)
            gf.update_user_paddle_left(paddle_left)
            gf.update_ball(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                           comp_paddle_right, comp_paddle_bottom, ball, user_paddle_hit_sound, comp_paddle_hit_sound)

        gf.update_screen(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top,
                         comp_paddle_right, comp_paddle_bottom, ball, play_button, net)


run_game()
