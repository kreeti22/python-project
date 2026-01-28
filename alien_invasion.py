import sys

import pygame 

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("alien invasion")

        # set the background colour 
        self.bg_color = (30,30,230)
    
    def run_game(self):
        """start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT : 
                    sys.exit()

            # redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            # MAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__' :
    # make a game instance and run the game 
    ai = AlienInvasion()
    ai.run_game()
