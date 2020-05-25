from src.state import State
from src.ball import Ball
from src.paddle import Paddle

import pygame
import sys

class GameState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager

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

    def blit(self, surface):
        surface.fill(pygame.Color('grey12'))
        pygame.draw.aaline(surface, (100,100,100), (800/2, 0), (800/2, 600))

        self.all_sprites.draw(surface)

    def join(self, old_state=None):
        if old_state == 'menu':
            self.all_sprites = pygame.sprite.Group()
            self.ball = Ball((100,100,100))
            self.player = Paddle((100,100,100), 20, 600/2, 1)
            self.opponent = Paddle((100,100,100), 800 - 20, 600/2, 2)
            self.all_sprites.add(self.ball, self.player, self.opponent)