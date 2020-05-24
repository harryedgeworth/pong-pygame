from src.gameStateManager import GameStateManager
from src.asset_manager import AssetManager 

import pygame


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((800,600))

    AM = AssetManager()
    AM.load_assets('assets/')
    AM.add_asset('Open Sans', pygame.font.SysFont('Open Sans', 48))

    gsm = GameStateManager(screen, AM)
    gsm.run()
