import pygame


class Alien(pygame.sprite.Sprite):
    """Class, present alien"""

    def __init__(self, ai_game):
        """Init alien and base position"""

        super().__init__()
        self.screen = ai_game.screen

        # Load alien image
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Setup base position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save horizontal position
        self.x = float(self.rect.x)
