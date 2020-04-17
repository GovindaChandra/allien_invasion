class Settings:
    """Class for storing all settings of the game Alien Invasion"""

    def __init__(self):
        """Initializes the game settings"""

        # Parameters of the screen
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bullets_allowed = 3

        # Parameters of the ship
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

