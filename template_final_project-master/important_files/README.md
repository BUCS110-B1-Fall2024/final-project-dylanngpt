---

Falling Objects Game  
CS110 B1 Final Project - Fall 2024  

Team Members  

Dylan Guthrie  

---

## Project Description  

My project is a **Falling Objects Game**, an interactive and fast-paced game where players control a character using arrow keys to dodge objects falling from the sky. The goal is to avoid collisions while earning points based on survival time. The game includes escalating difficulty as objects fall faster over time, adding to the challenge. Key features include:

- **Dynamic gameplay**: Objects increase speed and variety over time.  
- **Interactive controls**: Smooth movement with arrow keys for precise dodging.  
- **Score tracking**: Points are awarded based on survival duration, with a high-score feature.  
- **Power-ups**: Optional shields or speed boosts for extra excitement.  
- **Unique design**: Vibrant visuals and engaging sound effects enhance the gaming experience.  

This game is designed to provide an engaging and competitive experience for players of all skill levels.  

---

## GUI Design  

### Initial Design  

![initial gui]([https://ibb.co/Smqj6pk](https://ibb.co/bJ1JN2N))  

### Final Design  

![final gui](assets/finalgui.jpg)  

---

## Program Design  

### Features  

1. **Player Movement**: Arrow key controls for smooth navigation.  
2. **Falling Objects**: Randomized objects with varying speeds and sizes.  
3. **Score System**: Tracks survival time and displays high scores.  
4. **Difficulty Progression**: Gradual increase in object speed and frequency.  
5. **Power-Ups**: Optional items for added excitement, such as shields or temporary speed boosts.  
6. **Data Persistence**: Saves high scores to a file for future sessions.  

### Classes  

- **Player**: Manages the character's position, movement, and collision detection.  
- **FallingObject**: Represents objects falling from the sky, with attributes like speed and type.  
- **Game**: Oversees the game logic, including difficulty scaling and score tracking.  
- **GUIManager**: Handles rendering of the game screen and updates based on user interaction.  
- **DataHandler**: Manages saving and loading of high scores from a file.  


Milestone 3:
## **Acceptance Test Plan (ATP)**  

| **Step**                     | **Procedure**                            | **Expected Results**                                 |  
|-------------------------------|------------------------------------------|----------------------------------------------------|  
| **1. Launch the game**        | Run the program.                        | The game window opens, showing the player, falling objects, and initial score of `0`. |  
| **2. Move the player**        | Press the left or right arrow keys.      | The player moves smoothly left or right in response to the inputs. |  
| **3. Objects fall**           | Observe the falling objects.            | Objects fall from the top of the screen at a consistent speed. |  
| **4. Avoid falling objects**  | Move the player to avoid falling objects. | The player avoids collisions, and the game continues running without interruptions. |  
| **5. Collision detection**    | Let a falling object touch the player.   | The game stops, displays "Game Over," and shows the final score on the screen. |  
| **6. Restart the game**       | After a collision, press the **R** key. | The game restarts, resetting the player position, falling objects, and score to `0`. |  
| **7. Score updates**          | Avoid falling objects for an extended time. | The score increases over time as long as the player avoids collisions. |  
| **8. High score saving**      | Close and reopen the game after playing. | The highest score from the previous session is retained and displayed on the main screen. |  



Milestone 2 :

class Player:
    def __init__(self, x, y, img_file):
        """
        Initializes the player object.

        Args:
            x (int): Initial x-coordinate of the player.
            y (int): Initial y-coordinate of the player.
            img_file (str): Path to the player's image file.
        """
        self.x = x
        self.y = y
        self.img_file = img_file

    def move_left(self):
        """
        Moves the player left by a set amount.
        """
        self.x -= 5  # Adjust movement speed as needed

    def move_right(self):
        """
        Moves the player right by a set amount.
        """
        self.x += 5

    def get_position(self):
        """
        Returns the player's current position.

        Returns:
            tuple: (x, y) coordinates of the player.
        """
        return self.x, self.y


class FallingObject:
    def __init__(self, x, y, img_file, speed):
        """
        Initializes a falling object.

        Args:
            x (int): Initial x-coordinate of the object.
            y (int): Initial y-coordinate of the object.
            img_file (str): Path to the object's image file.
            speed (int): Speed at which the object falls.
        """
        self.x = x
        self.y = y
        self.img_file = img_file
        self.speed = speed

    def fall(self):
        """
        Updates the y-coordinate of the object to simulate falling.
        """
        self.y += self.speed

    def reset_position(self, new_x, new_y):
        """
        Resets the object's position to simulate spawning a new object.

        Args:
            new_x (int): New x-coordinate.
            new_y (int): New y-coordinate.
        """
        self.x = new_x
        self.y = new_y

    def get_position(self):
        """
        Returns the object's current position.

        Returns:
            tuple: (x, y) coordinates of the object.
        """
        return self.x, self.y