# user_paddle.py             #
# Created by: John Gawlik    #
# Campus ID: 889752424       #
# Due: September 29th, 2018  #
##############################

import pygame
from pygame.sprite import Sprite


class Paddle_Top(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the paddle and set its starting position"""
        super(Paddle_Top, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the paddle image and get its rect.
        self.image = pygame.image.load('images/user_paddle_top_bottom.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start paddle at the middle of the Bottom of the player's side.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

        # Store a decimal value for the paddle's center.
        self.center = float(self.rect.centerx)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def center_paddle_top(self):
        # Start paddle at the middle of the Bottom of the screen.
        self.center = (self.screen_rect.centerx / 2)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < (self.screen_rect.right / 2):
            self.center += self.ai_settings.user_paddle_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.user_paddle_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


class Paddle_Left(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the paddle and set its starting position"""
        super(Paddle_Left, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the paddle image and get its rect.
        self.image = pygame.image.load('images/user_paddle_left.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start paddle at the middle of the Left of the screen.
        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the paddle's center.
        self.center = float(self.rect.centery)

        # Movement Flag
        self.moving_up = False
        self.moving_down = False

    def center_paddle_left(self):
        # Start paddle at the middle of the Left of the screen.
        self.center = self.screen_rect.centery

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_up and self.rect.top > 0:
            self.center -= self.ai_settings.user_paddle_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.user_paddle_speed_factor

        # Update rect object from self.center
        self.rect.centery = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


class Paddle_Bottom(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the paddle and set its starting position"""
        super(Paddle_Bottom, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the paddle image and get its rect.
        self.image = pygame.image.load('images/user_paddle_top_bottom.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start paddle at the middle of the Bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the paddle's center.
        self.center = float(self.rect.centerx)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def center_paddle_bottom(self):
        # Start paddle at the middle of the Bottom of the screen.
        self.center = (self.screen_rect.centerx / 2)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < (self.screen_rect.right / 2):
            self.center += self.ai_settings.user_paddle_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.user_paddle_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)