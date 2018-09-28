# ball.py                   #
# Created by: John Gawlik   #
# Campus ID: 889752424      #
# Due: September 21st, 2018 #
#############################


import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    """A class to represent a Pong Ball"""

    def __init__(self, ai_settings, screen):
        """Initialize the ball and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the Comp_Paddle image and set its rect attribute
        self.image = pygame.image.load('images/ball.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the Paddle at the middle of the top of the screen.
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.centery

        # Store the balls's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def center_ball(self):
        """Center the ball on the screen"""
        self.x = self.screen_rect.centerx
        self.y = self.screen_rect.centery

    def check_user_horizontal_edge(self):
        """Return True if the ball is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.x <= screen_rect.left - 60:
            return True

    def check_comp_horizontal_edge(self):
        """Return True if the ball is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.x >= screen_rect.right + 60:
            return True

    def check_user_vertical_top_edge(self):
        """Return True if the ball is at a edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.y <= (screen_rect.top - 60) and self.x <= (screen_rect.right / 2):
            return True

    def check_comp_vertical_top_edge(self):
        """Return True if the ball is at a edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.y <= (screen_rect.top - 60) and self.x >= (screen_rect.right / 2):
            return True

    def check_user_vertical_bottom_edge(self):
        """Return True if the ball is at a edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.y >= (screen_rect.bottom + 60) and self.x <= (screen_rect.right / 2):
            return True

    def check_comp_vertical_bottom_edge(self):
        """Return True if the ball is at a edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.y >= (screen_rect.bottom + 60) and self.x >= (screen_rect.right / 2):
            return True

    def update(self):
        """Move the ball with x and y components."""
        # Move the ball to the right or left
        self.x += (self.ai_settings.ball_x_speed_factor * self.ai_settings.ball_x_direction)
        self.rect.x = self.x

        # Move the ball the ball up or down
        self.y += (self.ai_settings.ball_y_speed_factor * self.ai_settings.ball_y_direction)
        self.rect.y = self.y

    def blitme(self):
        """Draw the ball at its current location."""
        self.screen.blit(self.image, self.rect)
