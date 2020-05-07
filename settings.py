class Settings:
    """Class for storing all settings of the game Alien Invasion"""

    def __init__(self):
        """Initializes the game settings"""

        # Parameters of the screen
        self.screen_width = 1280
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Parameters of the ship
        self.ship_limit = 3
        self.ship_speed = 1.5

        # Bullet settings
        self.bullets_allowed = 3
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Parameters of alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 mean move - rightwards, -1 - leftward
        self.fleet_direction = 1

