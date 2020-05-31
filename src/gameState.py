from src.state import State
from src.ball import Ball
from src.paddle import Paddle

import pygame
import sys

class GameState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager
        self.AM = self.stateManager.AM

        self.WIDTH = pygame.display.get_surface().get_width()
        self.HEIGHT = pygame.display.get_surface().get_height()

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stateManager.change_state('menu')
                if event.key == pygame.K_DOWN:
                    self.player.speed += 7
                if event.key == pygame.K_UP:
                    self.player.speed -= 7
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.player.speed -= 7
                if event.key == pygame.K_UP:
                    self.player.speed += 7

    def tick(self, clock):
        self.all_sprites.update(self.ball, self.player, self.opponent)

        self.AM.add_asset('player_score',
            self.AM.get_asset('fonts/pstart.ttf-22').render(f"{self.player.score}", 1, (100,100,100)),
            'game')
        self.AM.add_asset('opponent_score',
            self.AM.get_asset('fonts/pstart.ttf-22').render(f"{self.opponent.score}", 1, (100,100,100)),
            'game')

        self.AM.add_asset('fps_counter',
            self.AM.get_asset('fonts/pstart.ttf-16').render(f"{int(clock.get_fps())} FPS", 1, (100,100,100)),
            'game')

        if self.player.score == 1:
            self.stateManager.change_state('gameover', winner='player')
        elif self.opponent.score == 1:
            self.stateManager.change_state('gameover', winner='opponent')

    def blit(self, surface):
        surface.fill(pygame.Color('grey12'))
        pygame.draw.aaline(surface, (100,100,100), (self.WIDTH/2, 0), (self.WIDTH/2, self.HEIGHT))

        surface.blit(self.AM.get_asset('player_score', 'game'), (356,285))
        surface.blit(self.AM.get_asset('opponent_score', 'game'), (422,285))
        surface.blit(self.AM.get_asset('fps_counter', 'game'), (10,10))

        self.all_sprites.draw(surface)

    def join(self, old_state=None):
        if old_state == 'menu':

            self.ball = Ball((100,100,100))
            self.player = Paddle((100,100,100), 20, self.HEIGHT/2, 1)
            self.opponent = Paddle((100,100,100), self.WIDTH - 20, self.HEIGHT/2, 2)

            self.all_sprites = pygame.sprite.Group()
            self.all_sprites.add(self.ball, self.player, self.opponent)
