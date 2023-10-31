import json
import pygame

def load(self, path):
    f = open(path, 'r')
    map_data = json.load(f)
    f.close()
    
    self.tilemap = map_data['tilemap']
    self.tile_size = map_data['tile_size']
    self.offgrid_tiles = map_data['offgrid']
