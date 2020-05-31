import pygame
import sys

from src.state import State

class GameOverState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager
        self.AM = self.stateManager.AM

        self.WIDTH = pygame.display.get_surface().get_width()
        self.HEIGHT = pygame.display.get_surface().get_height()

        # Add images for game over text
        self.AM.add_asset('gameover_text',
            self.AM.get_asset('fonts/pstart.ttf-45', 'gameover').render('GAME OVER!', 1, (100,100,100)),
            'gameover')

        # Add images for return to menu text
        self.AM.add_asset('returntomenu_text',
            self.AM.get_asset('fonts/pstart.ttf-16', 'gameover').render('Press ESC to return to the menu', 1, (100,100,100)),
            'gameover')

        # Add rects
        self.gameOverText =  pygame.Rect(
            (self.WIDTH / 2 - self.AM.get_asset('gameover_text', 'gameover').get_size()[0]/2, 230),
            self.AM.get_asset('gameover_text', 'gameover').get_size())

        self.returnMenuText =  pygame.Rect(
            (self.WIDTH / 2 - self.AM.get_asset('returntomenu_text', 'gameover').get_size()[0]/2, 350),
            self.AM.get_asset('returntomenu_text', 'gameover').get_size())

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.stateManager.state = 'menu'

    def tick(self, clock):
        pass

    def blit(self, surface):
        surface.fill(pygame.Color('grey12'))
        
        surface.blit(self.AM.get_asset('gameover_text', 'gameover'), self.gameOverText)
        surface.blit(self.AM.get_asset('returntomenu_text', 'gameover'), self.returnMenuText)

    def join(self, old_state=None):
        pass
