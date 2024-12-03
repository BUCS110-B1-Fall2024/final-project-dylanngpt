class GameController:
    def __init__(self, player, screen_width, screen_height):
        """Initializes the game controller
        Args:
            player (Player): The player object
            screen_width (int): Width of the game screen
            screen_height (int): Height of the game screen
        """
        self.player = player
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.falling_objects = []  # List to store active falling objects
        self.score = 0
        self.game_over = False

    def move_player(self, direction):
        """Moves the player based on input
        Args:
            direction (str): 'left' or 'right' direction
        """
        if direction == "left" and self.player.x > 0:
            self.player.move_left()
        elif direction == "right" and self.player.x < self.screen_width:
            self.player.move_right()

    def spawn_falling_object(self, img_file, speed):
        """Creates a new falling object and adds it to the game
        Args:
            img_file (str): Path to the object's image file
            speed (int): Speed of the falling object
        """
        new_object = FallingObject.generate_random_object(self.screen_width, img_file, speed)
        self.falling_objects.append(new_object)

    def update_game_state(self):
        """Updates positions of all objects and checks for collisions"""
        for obj in self.falling_objects:
            obj.update_position()
            # Remove objects that move off-screen
            if obj.y > self.screen_height:
                self.falling_objects.remove(obj)
                self.score += 1  # Increase score for successfully dodging an object
            # Check for collision
            if self.check_collision(obj):
                self.game_over = True
                break

    def check_collision(self, obj):
        """Checks for collision between the player and an object
        Args:
            obj (FallingObject): The falling object to check collision with
        Returns:
            bool: True if a collision occurs, False otherwise
        """
        player_rect = (self.player.x, self.player.y, 50, 50)  # Example dimensions
        obj_rect = (obj.x, obj.y, 30, 30)  # Example dimensions
        return (
            player_rect[0] < obj_rect[0] + obj_rect[2]
            and player_rect[0] + player_rect[2] > obj_rect[0]
            and player_rect[1] < obj_rect[1] + obj_rect[3]
            and player_rect[1] + player_rect[3] > obj_rect[1]
        )
