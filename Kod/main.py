import sys
import json
import pygame
from pygame.locals import *
from enemies import Enemy
from MapLoader import World
import time
from cloud import Cloud
# Imports modules and classes from other files

class Game:
    def __init__(self):
        pygame.init()                           # Initialises pygame
        pygame.display.set_caption("Not Mario") # Sets display name 

        SCREEN_WIDTH = 1280 #
        SCREEN_HEIGHT = 720 # Sets constants

        bg = pygame.image.load("Data_files/images/himmel.png") # Sets background

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets window size

        self.clock = pygame.time.Clock() # Sets clock to regulate frames per second
        
        with open ("tilemaps/testmap.json", "r") as file4: 
            testmap = json.load(file4)
                    
        with open ("tilemaps/level1.json", "r") as file1:  
            level1 = json.load(file1)
                    
        with open ("tilemaps/level2.json", "r") as file2:
            level2 = json.load(file2)

        with open ("tilemaps/level3.json", "r") as file3: # Imports the world maps - consider moving to maploader.py?
            level3 = json.load(file3)

        world = World(testmap)       #
        world_level1 = World(level1) #
        world_level2 = World(level2) #
        world_level3 = World(level3) # Sets worlds as variables using World() class s

        selectedWorld = world # Selects starting world
        
        n = 0
        k = 0

        while True:
            self.screen.blit(bg, (0, 0)) # Sets the bakground image
            selectedWorld.draw(self) # Renders the selected world
            Cloud.cloud(Cloud(k),self.screen.blit, n, k)
            if n % 30 == 0:
                k = 1 - k
                n = 0
            n += 1
            #Enemy(1, (50, 50), (8, 15), 5, False, False).render(self.screen) #
            #Enemy(2, (50, 50), (8, 15), 5, False, False).render(self.screen) #  
            #Enemy(3, (50, 50), (8, 15), 5, False, False).render(self.screen) # Test render for enemy.py functionality

            for event in pygame.event.get():

                if event.type == pygame.QUIT: # Exits the application if the window close button is pressed
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
