import pygame

class Player:
    def __init__(self, x, y, speed, width=50, height=50):
        """Initializes the player."""
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.invulnerable = False

    def move_left(self):
        """Moves the player to the left."""
        self.x -= self.speed

    def move_right(self):
        """Moves the player to the right."""
        self.x += self.speed

    def get_rect(self):
        """Returns the player's rectangle for collision detection."""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def boundary_check(self, screen_width):
        """Ensures the player stays within the screen boundaries."""
        self.x = max(0, min(screen_width - self.width, self.x))
