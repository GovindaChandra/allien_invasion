import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Class to manage the resources and behavior of the game."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Starting the main game cycle."""
        while True:
            # Tracking keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # The screen is redrawn every time the loop passes
            self.screen.fill(self.settings.bg_color)
            self.ship.blitime()
            # Display the last drawn screen.
            pygame.display.flip()


if __name__ == '__main__':
    # Create an instance and launch the game.
    ai = AlienInvasion()
    ai.run_game()

