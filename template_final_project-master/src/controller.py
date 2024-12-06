import pygame
from model import GameModel
from view import GameView

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.view = GameView(self.model)

        self.running = True
        self.clock = pygame.time.Clock()

    def mainloop(self):
        """Main game loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Pass events to the model
                self.model.handle_event(event)

            self.model.update()
            self.view.render()
            self.clock.tick(60)

        pygame.quit()
