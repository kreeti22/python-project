class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """initialize the game's settings"""
        # screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (90, 55, 180)

        # ship settings
        self.ship_speed = 2.0
        self.ship_limit = 4
        
        # bullet settings
        self.bullet_speed = 4 
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (230, 230, 240)
        self.bullets_allowed = 5
        
        # alien settings 
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50