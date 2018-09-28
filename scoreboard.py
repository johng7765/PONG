# scoreboard.py             #
# Created by: John Gawlik   #
# Campus ID: 889752424      #
# Due: September 29th, 2018 #
#############################

import pygame.font


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial Level image.
        self.prep_computer_score()
        self.prep_player_score()

    def prep_computer_score(self):
        """Turn the computer score into a rendered image."""
        computer_score_str = "C.Score: " + str(self.stats.computer_score)
        self.computer_score_image = self.font.render(computer_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the level at top right of the screen.
        self.computer_score_rect = self.computer_score_image.get_rect()
        self.computer_score_rect.right = self.screen_rect.right - 20
        self.computer_score_rect.top = 20

    def prep_player_score(self):
        """Turn the computer score into a rendered image."""
        player_score_str = "P.Score: " + str(self.stats.player_score)
        self.player_score_image = self.font.render(player_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the level at top right of the screen.
        self.player_score_rect = self.player_score_image.get_rect()
        self.player_score_rect.left = self.screen_rect.left + 20
        self.player_score_rect.top = 20

    def show_scores(self):
        """Draw Level to the screen."""
        self.screen.blit(self.computer_score_image, self.computer_score_rect)
        self.screen.blit(self.player_score_image, self.player_score_rect)
