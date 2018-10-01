# settings.py               #
# Created by: John Gawlik   #
# Campus ID: 889752424      #
# Due: September 29th, 2018 #
#############################


class Settings:
    """A class to store all settings for PONG."""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.lives_limit = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()
        self.user_paddle_speed_factor = None
        self.comp_paddle_speed_factor = None
        self.comp_paddle_top_direction = None
        self.comp_paddle_right_direction = None
        self.comp_paddle_bottom_direction = None
        self.ball_x_speed_factor = None
        self.ball_y_speed_factor = None
        self.ball_x_direction = None
        self.ball_y_direction = None

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        # User Paddles settings
        self.user_paddle_speed_factor = 3.52

        # Computer Paddle settings
        self.comp_paddle_speed_factor = 0.47

        # comp_paddle_direction of 1 represents rights; -1 represents left
        self.comp_paddle_top_direction = 1
        self.comp_paddle_right_direction = 1
        self.comp_paddle_bottom_direction = 1

        # Ball settings
        self.ball_x_speed_factor = 1.5
        self.ball_y_speed_factor = 1.5

        # Ball direction of 1 means right/down; -1 represents left/up
        self.ball_x_direction = -1
        self.ball_y_direction = -1

    def increase_speed(self):
        """Increase speed settings."""
        # self.user_paddle_speed_factor *= self.speedup_scale
        self.comp_paddle_speed_factor *= self.speedup_scale
        self.ball_x_speed_factor *= self.speedup_scale
        self.ball_y_speed_factor = self.speedup_scale
