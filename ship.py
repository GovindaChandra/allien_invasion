import pygame


class Ship:
    """Class for ship management"""

    def __init__(self, ai_game):
        """Initializes the ship and sets its starting position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loads an image of the ship and gets a rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitime(self):
        """Draws the ship in the current position"""
        self.screen.blit(self.image, self.rect)