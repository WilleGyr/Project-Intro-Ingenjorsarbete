import pygame

class Enemy:
    def __init__(self, e_type, pos, size, speed, shoots, spawns):
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
            pygame.draw.circle(surf, (0, 255, 0), (500, 250), 75)
        else:
            pygame.draw.circle(surf, (255, 0, 0), (750, 250), 75)
