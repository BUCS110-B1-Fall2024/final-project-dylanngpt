import pygame

class FallingObject:
    def __init__(self, x, y, speed, width=30, height=30):
        """Initializes a falling object."""
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height

    def fall(self):
        """Moves the object downward."""
        self.y += self.speed

    def get_rect(self):
        """Returns the object's rectangle for collision detection."""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_out_of_screen(self, screen_height):
        """Checks if the object is out of the screen."""
        return self.y > screen_height
