import sys
import pygame


class AlienInvasion:
    """Class to manage the resources and behavior of the game."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Starting the main game cycle."""
        while True:
            # Tracking keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # The screen is redrawn every time the loop passes
            self.screen.fill(self.bg_color)
            # Display the last drawn screen.
            pygame.display.flip()


if __name__ == '__main__':
    # Create an instance and launch the game.
    ai = AlienInvasion()
    ai.run_game()

