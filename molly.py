import pygame

class Molly:
    """A class to manage Molly."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/Molly.bmp')
        self.rect = self.image.get_rect()

        # start each new ship a the bottom center of the screen
        self.rect.center = self.screen_rect.center


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)