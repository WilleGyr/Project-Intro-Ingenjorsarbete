import pygame

class Enemy:
    def __init__(self, game, e_type, pos, size, speed, shoots, spawns):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.speed = speed
        self.shoots = shoots
        self.spawns = spawns

    def render(self, surf):
        if self.type == 1:
            pygame.draw.circle(surf, (0, 0, 255), (250, 250), 75)
        elif self.type == 2:
            pass
        else:
            pass
        surf.blit(self.game.assets["player"], self.pos)
