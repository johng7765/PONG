# game_stats.py             #
# Created by: John Gawlik   #
# Campus ID: 889752424      #
# Due: September 29th, 2018 #
#############################


class GameStats():
    """Track statistics for PONG."""

    def __init__(self, ai_settings):
        """Initialize Statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start PONG in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.player_score = 0
        self.computer_score = 0
