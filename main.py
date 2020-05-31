from src.gameStateManager import GameStateManager
from src.asset_manager import AssetManager 

import pygame


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Pong")

    AM = AssetManager(font_sizes = (16, 22, 45))
    AM.load_assets('assets/')

    gsm = GameStateManager(screen, AM)
    gsm.run()
