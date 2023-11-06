import sys
import json
import pygame as pg
from pygame.locals import *
from enemies import Enemy
from MapLoader import World, Solids
from player import Player, Bullet
from cloud import Cloud

class Game:
    def __init__(self):
        pg.init()                            # Initialises pg
        pg.display.set_caption("Platformer") # Sets display name 

        SCREEN_WIDTH = 1280 #
        SCREEN_HEIGHT = 720 # Sets constants

        level_1 = True
        level_2 = False

        with open ("tilemaps/testmap.json", "r") as file4: 
            testmap = json.load(file4)
                    
        with open ("tilemaps/level1.json", "r") as file1:  
            level1 = json.load(file1)
                    
        with open ("tilemaps/level2.json", "r") as file2:
            level2 = json.load(file2)

        with open ("tilemaps/level3.json", "r") as file3: # Imports the world maps - consider moving to maploader.py?
            level3 = json.load(file3)
        
        with open ("solids/solidsLevel1.json", "r") as file:
            level1Solids = json.load(file)

        with open ("solids/solidsLevel2.json", "r") as file:
            level2Solids = json.load(file)

        with open ("solids/solidsLevel3.json", "r") as file:
            level3Solids = json.load(file)

        bg = pg.image.load("Data_files/images/himmel.png") # Sets background

        screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        player_starting_position = (20, 490)

        all_sprites = pg.sprite.Group()
        bullets = pg.sprite.Group()
        solids = pg.sprite.Group()
        enemies = pg.sprite.Group()
        player = Player(player_starting_position, solids)
        all_sprites.add(player)


        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets window size

        self.clock = pg.time.Clock() # Sets clock to regulate frames per second
        dt = 0

        level_solids = [level1Solids, level2Solids, level3Solids]

        for level_solid in level_solids:
            for i in level_solid:
                i.append(20)
                i.append(20)

        rects = (tuple(x) for x in level1Solids)
        
        for rect in rects:  # Create the walls/platforms.
            block = Solids(pg.Rect(rect))
            all_sprites.add(block)
            solids.add(block)

        world_level1 = World(level1) #
        world_level2 = World(level2) #
        world_level3 = World(level3) # Sets worlds as variables using World() class 

        selectedWorld = world_level1 # Selects starting world


        n = 0
        k = 0

        self.loc1 = [1050, 540]
        self.dir1 = True

        self.loc2 = [950, 480]
        self.dir2 = True

        self.loc3 = [1050, 440]
        self.dir3 = True

        enemy1_col = Enemy.get_hitbox(Enemy(), 1, self.loc1)
        enemy2_col = Enemy.get_hitbox(Enemy(), 2, self.loc2)
        enemy3_col = Enemy.get_hitbox(Enemy(), 3, self.loc3)


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


            for event in pg.event.get():

                if event.type == pg.QUIT: # Exits the application if the window close button is pressed
                    pg.quit()
                    sys.exit()
                    
                # Changes the map between level 1, 2, 3 and 4  (test map)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        selectedWorld = world_level1

                        level_1 = True
                        player.pos = pg.math.Vector2(player_starting_position)
                        player.rect.topleft = player_starting_position
                        player.vel = pg.math.Vector2(0, 0)
                        player.on_ground = False

                        solids.empty()
                        rects = (tuple(x) for x in level1Solids)
                        
                        for rect in rects:  # Create the walls/platforms.
                            block = Solids(pg.Rect(rect))
                            all_sprites.add(block)
                            solids.add(block)
                    if event.key == pg.K_2:
                        selectedWorld = world_level2                   
                        level_1=False
                        level_2=True
                        player.pos = pg.math.Vector2(player_starting_position)
                        player.rect.topleft = player_starting_position
                        player.vel = pg.math.Vector2(0, 0)
                        player.on_ground = False

                        solids.empty()
                        for rect in rects:  # Create the walls/platforms.
                            rect.fill(255,255,255,0)

                        rects = (tuple(x) for x in level2Solids)
        
                        for rect in rects:  # Create the walls/platforms.
                            block = Solids(pg.Rect(rect))
                            all_sprites.add(block)
                            solids.add(block)
                    if event.key == pg.K_3:
                        selectedWorld = world_level3
                        level_2=False
                        player.pos = pg.math.Vector2(player_starting_position)
                        player.rect.topleft = player_starting_position
                        player.vel = pg.math.Vector2(0, 0)
                        player.on_ground = False

                        solids.empty()

                        rects = (tuple(x) for x in level3Solids)
        
                        for rect in rects:  # Create the walls/platforms.
                            block = Solids(pg.Rect(rect))
                            all_sprites.add(block)
                            solids.add(block)

                    if event.key == pg.K_a:
                        player.vel.x = -220
                    elif event.key == pg.K_d:
                        player.vel.x = 220
                    elif event.key == pg.K_SPACE:  # Jump
                        if player.on_ground:
                            player.vel.y = -470
                            player.pos.y -= 20
                            player.on_ground = False
                    if event.key == pg.K_f:  # Fire a bullet
                        bullet = Bullet(player.rect.midright, 1, damage=10)  # Pass damage value
                        bullets.add(bullet)
                        all_sprites.add(bullet)
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_a and player.vel.x < 0:
                        player.vel.x = 0
                    elif event.key == pg.K_d and  player.vel.x > 0:
                        player.vel.x = 0
                    # Remove bullets that go off-scre
            all_sprites.update(dt)

            for bullet in bullets.copy():
                if bullet.rect.right > SCREEN_WIDTH:
                    bullets.remove(bullet)
                    all_sprites.remove(bullet)
            bullet_solids = pg.sprite.groupcollide(bullets, solids, True, False)
            for bullet in bullet_solids:
                bullet.kill

    
            all_sprites.update(dt)
            all_sprites.draw(screen)            
            pg.display.flip()
            dt = self.clock.tick(60) / 1000

Game()
