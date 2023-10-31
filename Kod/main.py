import sys
import json
import pygame
from scripts.tilemap import Tilemap

class Game:
    def __init__(self, path):
        pygame.init()

        pygame.display.set_caption('test')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        f = open(path, 'r')
        map_data = json.load(f)
        f.close()
        
        self.tilemap = map_data['tilemap']
        self.tile_size = map_data['tile_size']
        self.offgrid_tiles = map_data['offgrid']
        
        self.tilemap = Tilemap(self, tile_size=16)
        self.tilemap.load('map_editor/map.json')
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()
