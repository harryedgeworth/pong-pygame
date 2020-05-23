import pygame
import os

pygame.init()

def load_assets(base_path, convert_images=False, font_sizes = (16,)):
    assets = {}
    for path in os.walk(base_path):
        for filename in path[2]:
            asset = None
            full_path = os.path.join(path[0], filename)
            human_path = full_path[len(base_path):]
            if os.path.splitext(full_path)[1] == '.png':
                asset = pygame.image.load(full_path)
                if convert_images:
                    asset.convert_alpha()
                assets[human_path] = asset
            if os.path.splitext(full_path)[1] == '.ttf':
                for size in font_sizes:
                    asset = pygame.font.Font(full_path, size)
                    assets[f'{human_path}-{size}'] = asset
    return assets