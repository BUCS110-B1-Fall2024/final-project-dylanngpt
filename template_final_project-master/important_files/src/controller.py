import pygame
from src.model import GameModel
from src.view import GameView

class GameController:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))  # Set window size
        pygame.display.set_caption("Dodging Falling Objects Game")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize model and view
        self.model = GameModel()
        self.view = GameView(self.screen)

    def run(self):
        while self.running:
            self.handle_events()
            self.model.update()  # Update game logic
            self.view.render(self.model)  # Render graphics
            pygame.display.flip()  # Update the screen
            self.clock.tick(60)  # Maintain 60 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.model.player.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.model.player.move_right()
