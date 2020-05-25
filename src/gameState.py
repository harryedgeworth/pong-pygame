from src.state import State
from src.ball import Ball
from src.paddle import Paddle

import pygame
import sys

class GameState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager
        self.AM = self.stateManager.AM

        self.GAME_FONT = pygame.font.Font("assets/fonts/pstart.ttf", 22)

        self.WIDTH = pygame.display.get_surface().get_width()
        self.HEIGHT = pygame.display.get_surface().get_height()

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stateManager.state = 'menu'
                if event.key == pygame.K_DOWN:
                    self.player.speed += 7
                if event.key == pygame.K_UP:
                    self.player.speed -= 7
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.player.speed -= 7
                if event.key == pygame.K_UP:
                    self.player.speed += 7

    def tick(self):
        self.all_sprites.update(self.ball, self.player, self.opponent)

        self.player_text = self.GAME_FONT.render(f"{self.player.score}", True, (100,100,100))
        self.opponent_text = self.GAME_FONT.render(f"{self.opponent.score}", True, (100,100,100))

    def blit(self, surface):
        surface.fill(pygame.Color('grey12'))
        pygame.draw.aaline(surface, (100,100,100), (self.WIDTH/2, 0), (self.WIDTH/2, self.HEIGHT))

        surface.blit(self.player_text, (356,285))
        surface.blit(self.opponent_text, (422,285))

        self.all_sprites.draw(surface)

    def join(self, old_state=None):
        if old_state == 'menu':

            self.ball = Ball((100,100,100))
            self.player = Paddle((100,100,100), 20, self.HEIGHT/2, 1)
            self.opponent = Paddle((100,100,100), self.WIDTH - 20, self.HEIGHT/2, 2)

            self.all_sprites = pygame.sprite.Group()
            self.all_sprites.add(self.ball, self.player, self.opponent)