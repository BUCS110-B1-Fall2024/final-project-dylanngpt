class Player:
    def __init__(self, x, y, img_file):
        """Initializes the player object
        Args:
            x (int): Starting x-coordinate of the player
            y (int): Starting y-coordinate of the player
            img_file (str): Path to the image file representing the player
        """
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = 5  # Default movement speed

    def move_right(self):
        """Moves the player to the right"""
        self.x += self.speed

    def move_left(self):
        """Moves the player to the left"""
        self.x -= self.speed
