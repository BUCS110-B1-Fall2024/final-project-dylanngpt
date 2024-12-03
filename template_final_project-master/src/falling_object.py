import random

class FallingObject:
    def __init__(self, x, y, img_file, speed):
        """Initializes a falling object
        Args:
            x (int): Starting x-coordinate of the object
            y (int): Starting y-coordinate of the object
            img_file (str): Path to the image file representing the object
            speed (int): Speed at which the object falls
        """
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed

    def update_position(self):
        """Updates the object's position to fall downward"""
        self.y += self.speed

    @staticmethod
    def generate_random_object(screen_width, img_file, speed):
        """Generates a random falling object at the top of the screen
        Args:
            screen_width (int): Width of the game screen
            img_file (str): Path to the image file representing the object
            speed (int): Speed of the object
        Returns:
            FallingObject: A new falling object instance
        """
        x = random.randint(0, screen_width)
        y = 0  # Start at the top of the screen
        return FallingObject(x, y, img_file, speed)
