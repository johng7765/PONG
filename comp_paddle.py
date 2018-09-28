# comp_paddle.py                   #
# Created by: John Gawlik          #
# Campus ID: 889752424             #
# Due: September 29th, 2018        #
####################################


import pygame
from pygame.sprite import Sprite


class Comp_Paddle_Top(Sprite):
    """A class to represent a Paddle controlled by the Computer"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Comp_Paddle_Top, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the Comp_Paddle_Top image ands set its rect attribute
        self.image = pygame.image.load('images/comp_paddle_top_bottom.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """Center the paddle on the screen"""
        self.rect.x = self.screen_rect.centerx
        self.rect.y = self.screen_rect.top

        # Store the alien's exact position.
        self.x = float(self.rect.x)

        # Store movement flag
        self.moving_right = False
        self.moving_left = False

    def center_comp_paddle_top(self):
        """Center the paddle on the screen"""
        self.x = self.screen_rect.centerx + (self.screen_rect.centerx / 2)

    def check_right_edge(self):
        """Return true if comp_paddle_top is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right < screen_rect.right:
            return True

    def check_left_edge(self):
        """Return true if comp_paddle_top is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.left > (screen_rect.right / 2):
            return True

    def update_right(self):
        """Move the Paddle right."""
        self.x += self.ai_settings.comp_paddle_speed_factor
        self.rect.x = self.x

    def update_left(self):
        """Move the Paddle right."""
        self.x -= self.ai_settings.comp_paddle_speed_factor
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


class Comp_Paddle_Right(Sprite):
    """A class to represent a Paddle controlled by the Computer"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Comp_Paddle_Right, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the Comp_Paddle_Right image ands set its rect attribute
        self.image = pygame.image.load('images/comp_paddle_right.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """Center the paddle on the screen"""
        self.rect.right = self.screen_rect.right
        self.rect.y = self.screen_rect.centery

        # Store the alien's exact position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def center_comp_paddle_right(self):
        """Center the paddle on the screen"""
        self.y = self.screen_rect.centery

    def check_bottom_edge(self):
        """Return true if comp_paddle_right is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom < screen_rect.bottom:
            return True

    def check_top_edge(self):
        """Return true if comp_paddle_right is at edge of screen."""
        if self.rect.top > 0:
            return True

    def update_up(self):
        """Move the Paddle up."""
        self.y -= (self.ai_settings.comp_paddle_speed_factor * self.ai_settings.comp_paddle_right_direction)
        self.rect.y = self.y

    def update_down(self):
        """Move the Paddle up."""
        self.y += (self.ai_settings.comp_paddle_speed_factor * self.ai_settings.comp_paddle_right_direction)
        self.rect.y = self.y

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


class Comp_Paddle_Bottom(Sprite):
    """A class to represent a Paddle controlled by the Computer"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Comp_Paddle_Bottom, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the Comp_Paddle_Bottom image and set its rect attribute
        self.image = pygame.image.load('images/comp_paddle_top_bottom.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """Center the paddle on the screen"""
        self.rect.x = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def center_comp_paddle_bottom(self):
        """Center the paddle on the screen"""
        self.x = self.screen_rect.centerx + (self.screen_rect.centerx / 2)

    def check_right_edge(self):
        """Return true if comp_paddle_top is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right < screen_rect.right:
            return True

    def check_left_edge(self):
        """Return true if comp_paddle_top is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.left > (screen_rect.right / 2):
            return True

    def update_right(self):
        """Move the Paddle right."""
        self.x += (self.ai_settings.comp_paddle_speed_factor * self.ai_settings.comp_paddle_top_direction)
        self.rect.x = self.x

    def update_left(self):
        """Move the Paddle right."""
        self.x -= (self.ai_settings.comp_paddle_speed_factor * self.ai_settings.comp_paddle_top_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
