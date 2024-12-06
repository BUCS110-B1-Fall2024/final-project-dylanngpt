import random
import pygame
import os
from playerr import Player
from fallingobject import FallingObject
from highscoremanager import HighScoreManager
from powerup import PowerUp


class GameModel:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.player = Player(self.width // 2, self.height - 50, speed=7)
        self.objects = []
        self.power_ups = []
        self.active_power_up = None
        self.power_up_timer = 0
        self.power_up_spawn_time = pygame.time.get_ticks()
        self.spawn_timer = 0
        self.score = 0
        self.game_over = False
        self.level = 1
        self.start_time = pygame.time.get_ticks()

        # High score management
        self.high_score_manager = HighScoreManager()
        self.high_score = self.high_score_manager.high_score

        # Asset directory
        self.assets_dir = os.path.join(os.path.dirname(__file__), "../assets")

    def reset_game(self):
        """Resets the game state."""
        self.__init__()

    def handle_event(self, event):
        """Handles game restart on key press."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and self.game_over:
                self.reset_game()
    
    
    def spawn_power_up(self):
        """Spawns a new power-up periodically."""
        current_time = pygame.time.get_ticks()
        if current_time - self.power_up_spawn_time >= 15000:  # Every 15 seconds
            self.power_up_spawn_time = current_time
            power_up_type = random.choice(["forcefield", "speed_boost"])
            x = random.randint(50, self.width - 50)
            image_path = os.path.join(self.assets_dir, f"{power_up_type}.png")
            power_up = PowerUp(x=x, y=0, image_path=image_path, effect_type=power_up_type, duration=5000)
            self.power_ups.append(power_up)

    def handle_power_up_collision(self):
        """Handles collisions with power-ups."""
        player_rect = self.player.get_rect()
        for power_up in self.power_ups:
            if player_rect.colliderect(power_up.rect):
                self.active_power_up = power_up
                self.power_up_timer = pygame.time.get_ticks()
                self.power_ups.remove(power_up)

                # Apply power-up effect
                if power_up.effect_type == "forcefield":
                    self.player.invulnerable = True
                elif power_up.effect_type == "speed_boost":
                    self.player.speed += 3

    def deactivate_power_up(self):
        """Deactivates power-up after its duration."""
        if self.active_power_up:
            elapsed_time = pygame.time.get_ticks() - self.power_up_timer
            if elapsed_time > self.active_power_up.duration:
                if self.active_power_up.effect_type == "forcefield":
                    self.player.invulnerable = False
                elif self.active_power_up.effect_type == "speed_boost":
                    self.player.speed -= 3
                self.active_power_up = None

    def update_difficulty(self):
        """Adjusts difficulty over time."""
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        new_level = elapsed_time // 30 + 1
        if new_level > self.level:
            self.level = new_level

    def update(self):
        """Updates the game state."""
        if self.game_over:
            if self.score > self.high_score:
                self.high_score = self.score
                self.high_score_manager.save_high_score(self.high_score)
            return

        self.update_difficulty()
        self.spawn_power_up()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        self.player.boundary_check(self.width)

        # Spawn falling objects
        self.spawn_timer += 1
        spawn_rate = max(20 - self.level, 5)
        if self.spawn_timer >= spawn_rate:
            self.spawn_timer = 0
            self.objects.append(
                FallingObject(
                    x=random.randint(0, self.width - 30),
                    y=0,
                    speed=random.randint(3, 8 + self.level)
                )
            )

        # Update falling objects and power-ups
        for obj in self.objects:
            obj.fall()
        for power_up in self.power_ups:
            power_up.fall()

        # Remove off-screen entities
        self.objects = [obj for obj in self.objects if not obj.is_out_of_screen(self.height)]
        self.power_ups = [power_up for power_up in self.power_ups if not power_up.is_out_of_screen(self.height)]

        # Handle collisions
        self.handle_power_up_collision()
        self.deactivate_power_up()

        player_rect = self.player.get_rect()
        for obj in self.objects:
            if player_rect.colliderect(obj.get_rect()):
                if not self.player.invulnerable:
                    self.game_over = True
                    return

        # Update score
        self.score += 1

    def get_elapsed_time(self):
        """Calculates elapsed time."""
        return (pygame.time.get_ticks() - self.start_time) // 1000
