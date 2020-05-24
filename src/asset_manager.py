import pygame
import os

class AssetManager():
    def __init__(self, font_sizes):
        self.assets = {}
        self.scoped_assets = {}
        self.convert_images = True
        self.font_sizes = font_sizes

    def load_assets(self, base_path):
        assets = {}
        for path in os.walk(base_path):
            for filename in path[2]:
                full_path = os.path.join(path[0], filename)
                human_path = full_path[len(base_path):]
                if os.path.splitext(full_path)[1] == '.png':
                    self.load_image(full_path, name=human_path)
                if os.path.splitext(full_path)[1] == '.ttf':
                    self.load_font(full_path, name=human_path)

        return assets

    def load_image(self, path, name=None):
        if not name:
            name = path
        image = pygame.image.load(path)
        if self.convert_images:
            image.convert_alpha()
        self.add_asset(name, image)

    def load_font(self, path, name=None, sizes=None):
        if not name:
            name = path
        if not sizes:
            sizes = self.font_sizes
        for size in self.font_sizes:
            font = pygame.font.Font(path, size)
            self.add_asset(f'{name}-{size}', font)

    def add_asset(self, name, asset, scope=None):
        if not scope:
            self.assets[name] = asset
        else:
            if scope not in self.scoped_assets:
                self.scoped_assets[scope] = {}
            self.scoped_assets[scope][name] = asset

    def get_asset(self, name, scope=None):
        '''Return asset with given name.
        If the asset name exists in the given scope, return that asset,
        otherwise return the global asset with that name. If the asset doesn't
        exist in global namespace, returns None.'''

        if scope:
            if name in self.scoped_assets.get(scope, {}):
                return self.scoped_assets[scope][name]
        return self.assets.get(name)