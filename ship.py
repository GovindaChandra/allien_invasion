import pygame


class Ship:
    """Class for ship management"""

    def __init__(self, ai_game):
        """Initializes the ship and sets its starting position"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads an image of the ship and gets a rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Save x - coordinate of the ship
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update position the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Draws the ship in the current position"""
        self.screen.blit(self.image, self.rect)