class Screen:
    def __init__(self):
        """Get the height and width of the screen, set the program to fill it"""
        self.size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
        self.screen = pygame.display.set_mode(size)
        self.x = int((width - 910) / 2)
        self.y = int((height - 675) / 2)
        
    def getScreen(self):
        """Set up x and y coordinates so as to center the game on the screen"""
        
        return self.screen
