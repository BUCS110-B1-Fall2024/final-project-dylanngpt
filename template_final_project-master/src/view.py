import pygame
import os
import sys


class GameView:
    def __init__(self, model):
        self.model = model

        # Set up the display
        self.screen = pygame.display.set_mode((model.width, model.height))
        pygame.display.set_caption("Falling Objects Game")

        # Load assets
        assets_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../assets")
        try:
            self.player_image = pygame.image.load(os.path.join(assets_dir, "player.png"))
            self.object_image = pygame.image.load(os.path.join(assets_dir, "falling_object.png"))
            self.forcefield_image = pygame.image.load(os.path.join(assets_dir, "forcefield.png"))
            self.speed_boost_image = pygame.image.load(os.path.join(assets_dir, "speed_boost.png"))
        except FileNotFoundError:
            print("Assets not found!")
            sys.exit()

        # Resize assets
        self.player_image = pygame.transform.scale(self.player_image, (50, 50))
        self.object_image = pygame.transform.scale(self.object_image, (30, 30))
        self.forcefield_image = pygame.transform.scale(self.forcefield_image, (40, 40))
        self.speed_boost_image = pygame.transform.scale(self.speed_boost_image, (40, 40))

    def render(self):
        self.screen.fill((0, 0, 0))

        # Draw the player
        player_image = self.forcefield_image if self.model.player.invulnerable else self.player_image
        self.screen.blit(player_image, (self.model.player.x, self.model.player.y))

        # Draw falling objects
        for obj in self.model.objects:
            self.screen.blit(self.object_image, (obj.x, obj.y))

        # Draw power-ups
        for power_up in self.model.power_ups:
            power_up_image = self.forcefield_image if power_up.effect_type == "forcefield" else self.speed_boost_image
            self.screen.blit(power_up_image, (power_up.x, power_up.y))

        # Draw HUD
        font = pygame.font.SysFont(None, 36)
        self.screen.blit(font.render(f"Score: {self.model.score}", True, (255, 255, 255)), (10, 10))
        self.screen.blit(font.render(f"High Score: {self.model.high_score}", True, (255, 255, 255)), (10, 50))
        self.screen.blit(font.render(f"Time: {self.model.get_elapsed_time()}s", True, (255, 255, 255)),
                         (self.model.width - 150, 10))
        self.screen.blit(font.render(f"Level: {self.model.level}", True, (255, 255, 255)),
                         (self.model.width // 2 - 50, 10))

        if self.model.game_over:
            game_over_text = font.render("GAME OVER! Press 'R' to Restart", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.model.width // 2, self.model.height // 2))
            self.screen.blit(game_over_text, text_rect)

        pygame.display.flip()
