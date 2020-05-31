from src.menuState import MenuState
from src.gameState import GameState
from src.gameOverState import GameOverState

import pygame

class GameStateManager:
    def __init__(self, surface, AM=None):
        self.AM = AM

        self.current_state = 'menu'
        self.states = {
            'menu': MenuState(self),
            'game': GameState(self),
            'gameover': GameOverState(self)
        }

        self.surface = surface
        self.running = True

    @property
    def state(self):
        return self.states[self.current_state]

    @state.setter
    def state(self, state):
        old_state = self.current_state
        self.state.leave(state)
        self.current_state = state
        self.state.join(old_state)

    def handleEvents(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
        self.state.handleEvents(events)

    def blit(self, flip_display=True):
        self.state.blit(self.surface)
        if flip_display:
            pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            clock.tick(60)
            self.handleEvents()
            self.state.tick(clock)
            self.blit()
