import sys
import json
import pygame
from pygame.locals import *
from enemies import Enemy
from MapLoader import World

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Not Mario")

        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720

        bg = pygame.image.load("Data_files/images/himmel.png")

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        
        with open ("tilemaps/testmap.json", "r") as file4:
            testmap = json.load(file4)
                    
        with open ("tilemaps/level1.json", "r") as file1:
            level1 = json.load(file1)
                    
        with open ("tilemaps/level2.json", "r") as file2:
            level2 = json.load(file2)

        with open ("tilemaps/level3.json", "r") as file3:
            level3 = json.load(file3)

        world = World(testmap)
        world_level1 = World(level1)
        world_level2 = World(level2)
        world_level3 = World(level3)

        selectedWorld = world

        while True:
            # Sets the bakground image
            self.screen.blit(bg, (0, 0))
            
            # Renders the selected world
            selectedWorld.draw(self)

            Enemy(1, (50, 50), (8, 15), 5, False, False).render(self.screen)
            Enemy(2, (50, 50), (8, 15), 5, False, False).render(self.screen)
            Enemy(3, (50, 50), (8, 15), 5, False, False).render(self.screen)

            for event in pygame.event.get():

                # Exits the application if the window close button is pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                # Changes the map between level 1, 2, 3 and 4  (test map)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selectedWorld = world_level1
                    if event.key == pygame.K_2:
                        selectedWorld = world_level2
                    if event.key == pygame.K_3:
                        selectedWorld = world_level3
                    if event.key == pygame.K_4:
                        selectedWorld = world
            pygame.display.update()
            self.clock.tick(60)

Game()
