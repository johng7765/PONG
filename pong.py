# pong.py                   #
# Created by: John Gawlik   #
# Campus ID: 889752424      #
# Due: September 29th, 2018 #
#############################

import pygame
from settings import Settings
from user_paddle import Paddle_Top
from user_paddle import Paddle_Bottom
from user_paddle import Paddle_Left
from comp_paddle import Comp_Paddle_Top
from comp_paddle import Comp_Paddle_Right
from comp_paddle import Comp_Paddle_Bottom
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

    # Create and instance to store game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Net
    net = Net(screen)

    # Make top paddle:
    paddle_top = Paddle_Top(ai_settings, screen)
    paddle_bottom = Paddle_Bottom(ai_settings, screen)
    paddle_left = Paddle_Left(ai_settings, screen)

    # Make a paddle controlled by the computer.
    comp_paddle_top = Comp_Paddle_Top(ai_settings, screen)
    comp_paddle_right = Comp_Paddle_Right(ai_settings, screen)
    comp_paddle_bottom = Comp_Paddle_Bottom(ai_settings, screen)

    # Create the ball
    ball = Ball(ai_settings, screen)

    # Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, paddle_top, paddle_bottom, paddle_left, comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball)

        if stats.game_active:
            gf.update_comp_paddle_top(comp_paddle_top, ball)
            gf.update_comp_paddle_right(comp_paddle_right, ball)
            gf.update_comp_paddle_bottom(comp_paddle_bottom, ball)
            gf.update_user_paddle_top(paddle_top)
            gf.update_user_paddle_bottom(paddle_bottom)
            gf.update_user_paddle_left(paddle_left)
            gf.update_ball(ai_settings, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball)

        gf.update_screen(ai_settings, screen, stats, sb, paddle_top, paddle_bottom, paddle_left, comp_paddle_top, comp_paddle_right, comp_paddle_bottom, ball, play_button, net)


run_game()
