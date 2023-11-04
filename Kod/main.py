import sys
import json
import pygame
from pygame.locals import *
from enemies import Enemy
from MapLoader import World
from cloud import Cloud
# Imports modules and classes from other files

class Game:
    def __init__(self):
        pygame.init()                           # Initialises pygame
        pygame.display.set_caption("Not Mario") # Sets display name 

        SCREEN_WIDTH = 1280 #
        SCREEN_HEIGHT = 720 # Sets constants

        level_1 = True
        level_2 = False
        level_3 = False

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
        world_level3 = World(level3) # Sets worlds as variables using World() class 

        selectedWorld = world # Selects starting world

        n = 0
        k = 0

        self.loc1 = [1050, 540]
        self.dir1 = True

        self.loc2 = [950, 480]
        self.dir2 = True

        self.loc3 = [1050, 440]
        self.dir3 = True

        while True:
            self.screen.blit(bg, (0, 0)) # Sets the bakground image 
            selectedWorld.draw(self) # Renders the selected world

            #Cloud.cloud(Cloud(k),self.screen.blit, n, k)
            #if n % 30 == 0:
            #    k = 1 - k
            #    n = 0
            #n += 1

            if level_1:
                if self.loc1[0] < 1135 and self.dir1:
                    self.loc1[0] = self.loc1[0] + 1
                    Enemy.render_enemy(Enemy(), self.screen, 1, self.loc1, self.dir1)
                elif self.loc1[0] == 1135 and self.dir1:
                    self.dir1 = False
                
                if self.loc1[0] > 830 and not self.dir1:
                    self.loc1[0] = self.loc1[0] - 1
                    Enemy.render_enemy(Enemy(), self.screen, 1, self.loc1, self.dir1)
                elif self.loc1[0] == 830 and not self.dir1:
                    self.dir1 = True

                enemy1_col = Enemy.get_hitbox(Enemy(), 1, self.loc1)

            elif level_2:
                if self.loc2[0] < 1045 and self.dir2:
                    self.loc2[0] = self.loc2[0] + 1
                    Enemy.render_enemy(Enemy(), self.screen, 2, self.loc2, self.dir2)
                elif self.loc2[0] == 1045 and self.dir2:
                    self.dir2 = False
                
                if self.loc2[0] > 865 and not self.dir2:
                    self.loc2[0] = self.loc2[0] - 1
                    Enemy.render_enemy(Enemy(), self.screen, 2, self.loc2, self.dir2)
                elif self.loc2[0] == 865 and not self.dir2:
                    self.dir2 = True

                enemy2_col = Enemy.get_hitbox(Enemy(), 2, self.loc2)

            else:
                if self.loc3[0] < 1100 and self.dir3:
                    self.loc3[0] = self.loc3[0] + 1
                    Enemy.render_enemy(Enemy(), self.screen, 3, self.loc3, self.dir3)
                elif self.loc3[0] == 1100 and self.dir3:
                    self.dir3 = False
                
                if self.loc3[0] > 955 and not self.dir3:
                    self.loc3[0] = self.loc3[0] - 1
                    Enemy.render_enemy(Enemy(), self.screen, 3, self.loc3, self.dir3)
                elif self.loc3[0] == 955 and not self.dir3:
                    self.dir3 = True

                enemy3_col = Enemy.get_hitbox(Enemy(), 3, self.loc3)

            for event in pygame.event.get():

                if event.type == pygame.QUIT: # Exits the application if the window close button is pressed
                    pygame.quit()
                    sys.exit()
                    
                # Changes the map between level 1, 2, 3 and 4  (test map)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selectedWorld = world_level1
                        level_1 = True

                    if event.key == pygame.K_2:
                        selectedWorld = world_level2
                        level_1 = False
                        level_2 = True

                    if event.key == pygame.K_3:
                        selectedWorld = world_level3
                        level_2 = False

                    if event.key == pygame.K_4:
                        selectedWorld = world

            pygame.display.update()
            self.clock.tick(60)

Game()
