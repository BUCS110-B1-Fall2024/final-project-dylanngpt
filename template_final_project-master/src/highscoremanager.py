import os

class HighScoreManager:
    def __init__(self, filename="highscores.txt"):
        """Initializes the high score manager."""
        self.filename = filename
        self.high_score = self.load_high_score()

    def load_high_score(self):
        """Loads the high score from the file."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    return int(file.read().strip())
                except ValueError:
                    return 0
        return 0

    def save_high_score(self, score):
        """Saves the high score to the file."""
        with open(self.filename, "w") as file:
            file.write(str(score))
