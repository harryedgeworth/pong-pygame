from src.state import State
import pygame
import sys

class MenuState(State):
    def __init__(self, stateManager):
        self.stateManager = stateManager
        self.AM = self.stateManager.AM

        self.WIDTH = pygame.display.get_surface().get_width()
        self.HEIGHT = pygame.display.get_surface().get_height()

        # Add images for play text and hover text
        self.AM.add_asset('play_image',
            self.AM.get_asset('fonts/pstart.ttf-22').render(' Play Game ', 1, (100,100,100)),
            'menu')
        self.AM.add_asset('play_hover_image',
                self.AM.get_asset('fonts/pstart.ttf-22', 'menu').render('>Play Game<', 1, (255,255,255)),
                'menu')
        # Rectangle represented play text
        self.play_button = pygame.Rect(
            (self.WIDTH / 2 - self.AM.get_asset('play_image', 'menu').get_size()[0]/2, 230),
            self.AM.get_asset('play_image', 'menu').get_size())

        # Add images for quit text and hover text
        self.AM.add_asset('quit_image',
            self.AM.get_asset('fonts/pstart.ttf-22', 'menu').render(' Quit Game ', 1, (100,100,100)),
            'menu')
        self.AM.add_asset('quit_hover_image',
                self.AM.get_asset('fonts/pstart.ttf-22', 'menu').render('>Quit Game<', 1, (255,255,255)),
                'menu')
        # Rectangle represented quit text
        self.quit_button = pygame.Rect(
            (self.WIDTH / 2- self.AM.get_asset('quit_image', 'menu').get_size()[0]/2, 310),
            self.AM.get_asset('quit_image', 'menu').get_size())

    def handleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.collidepoint(event.pos):
                    self.stateManager.state = 'game'
                if self.quit_button.collidepoint(event.pos):
                    sys.exit()

    def tick(self):
        pass

    def blit(self, surface):
        surface.fill(pygame.Color('grey12'))

        if not self.play_button.collidepoint(pygame.mouse.get_pos()):
            surface.blit(self.AM.get_asset('play_image', 'menu'), self.play_button)
        else:
            surface.blit(self.AM.get_asset('play_hover_image', 'menu'), self.play_button)
        if not self.quit_button.collidepoint(pygame.mouse.get_pos()):
            surface.blit(self.AM.get_asset('quit_image', 'menu'), self.quit_button)
        else:
            surface.blit(self.AM.get_asset('quit_hover_image', 'menu'), self.quit_button)