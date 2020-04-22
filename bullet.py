import pygame


class Bullet(pygame.sprite.Sprite):
    """Class for control bullets"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet  in position (0, 0) and adjust
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet position in float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet"""

        # Update position in float mode
        self.y -= self.settings.bullet_speed

        # Update bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet"""

        pygame.draw.rect(self.screen, self.color, self.rect)
