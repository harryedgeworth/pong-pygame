from src.state import State
import pygame

class GameState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stateManager.state = 'menu'

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.speed[0] -= 2
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.speed[0] += 2
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.speed[1] -= 2
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.speed[1] += 2

    def tick(self):
        self.speed[0] *= 0.8
        self.speed[1] *= 0.8

        if abs(self.speed[0]) < 1: self.speed[0] = 0
        if abs(self.speed[1]) < 1: self.speed[1] = 0

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def blit(self, surface):
        surface.fill((56, 136, 21))
        pygame.draw.rect(surface, (211, 187, 43), self.rect)

    def join(self, old_state=None):
        if old_state == 'menu':
            self.rect = pygame.Rect((280, 200), (80,80))
            self.speed = [0,0]