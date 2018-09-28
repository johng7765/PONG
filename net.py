# net.py                    #
# Created by: John Gawlik   #
# Campus ID: 889752424      #
# Due: September 29th, 2018 #
#############################

import pygame


class Net():
    def __init__(self, screen):
        self.screen = screen

        # Load the Net Image
        self.image = pygame.image.load('images/net.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start net at middle of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

        # Store a decimal value for the paddle's center.
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Draw the net."""
        self.screen.blit(self.image, self.rect)