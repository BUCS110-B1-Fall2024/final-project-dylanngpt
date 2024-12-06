import pygame

class PowerUp:
    def __init__(self, x, y, image_path, effect_type, duration):
        self.x = x
        self.y = y
        self.image_path = image_path
        self.effect_type = effect_type
        self.duration = duration
        self.speed = 3  # Speed of the power-up falling
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def fall(self):
        """Moves the power-up downward."""
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def is_out_of_screen(self, screen_height):
        """Checks if the power-up is out of screen bounds."""
        return self.y > screen_height
