import sys
import json
import pygame as pg
from pygame.locals import *
from enemies import Enemy
from MapLoader import World, Solids
from player import Player, Bullet

class Game:
    def __init__(self):
        pg.init()                          
        pg.display.set_caption("Platformer") 

        SCREEN_WIDTH = 1280 
        SCREEN_HEIGHT = 720 

        # Första banan startas
        level_1 = True
        level_2 = False
        level_3 = False


        score = 0

        # Öppnar filerna som kommer användas för att få grafik i spelet
        with open ("tilemaps/testmap.json", "r") as file4: 
            testmap = json.load(file4)
                    
        with open ("tilemaps/level1.json", "r") as file1:  
            level1 = json.load(file1)
                    
        with open ("tilemaps/level2.json", "r") as file2:
            level2 = json.load(file2)

        with open ("tilemaps/level3.json", "r") as file3: # Imports the world maps - consider moving to maploader.py?
            level3 = json.load(file3)
        
        # Innehåller filerna med blocken man kan stå på, används till att kolla kollision mellan andra sprites
        with open ("solids/solidsLevel1.json", "r") as file:
            level1Solids = json.load(file)

        with open ("solids/solidsLevel2.json", "r") as file:
            level2Solids = json.load(file)

        with open ("solids/solidsLevel3.json", "r") as file:
            level3Solids = json.load(file)


        bg = pg.image.load("Data_files/images/himmel.png") # Bakgrundsbilden

        screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Startar alltid på samma ställe i alla banor, därför behövs bara ett startställe
        player_starting_position = (20, 490) 

        # Alla sprites som kommer behövas när kollision sker
        all_sprites = pg.sprite.Group()
        bullets = pg.sprite.Group()
        solids = pg.sprite.Group()
        enemies = pg.sprite.Group()
        player = Player(player_starting_position,solids) # Kollisionen mellan spelare och solida blocks sker i player.py
        all_sprites.add(player)

        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets window size

        self.clock = pg.time.Clock() # Sets clock to regulate frames per second
        dt = 0

        level_solids = [level1Solids, level2Solids, level3Solids]

        # Gör om informationen från deras json filer till att ha fyra värden samt gör dem till en tuple så att de ska funka som rects
        for level_solid in level_solids:
            for i in level_solid:
                i.append(20)
                i.append(20)


        # Skapas för första banan, kan göras till en funktion då den används flera gånger
        rects = (tuple(x) for x in level1Solids)
        
        for rect in rects: 
            block = Solids(pg.Rect(rect))
            all_sprites.add(block)
            solids.add(block)

        # Berättar vilken fil som ska laddas in vid varje värld
        world_level1 = World(level1) 
        world_level2 = World(level2) 
        world_level3 = World(level3) 

        selectedWorld = world_level1 #Startvärld

        # Berättar vart varje fiende befinner sig vid start
        self.loc1 = [1050, 540]
        self.dir1 = True

        self.loc2 = [950, 480]
        self.dir2 = True

        self.loc3 = [1050, 440]
        self.dir3 = True

        enemy1_alive = True
        enemy2_alive = True
        enemy3_alive = True

        while True:
            self.screen.blit(bg, (0, 0)) # Sets the bakground image 
            selectedWorld.draw(self) # Renders the selected world

            if level_1 and enemy1_alive:
                # Sköter platsen där fienden befinner sig och att den vänder sig om vid en viss kordinat
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

                # enemies spriten uppdateras varje frame för att kollisionen ska kunna kollas i varje frame
                enemies.empty()
                enemy = Solids(pg.Rect(self.loc1[0], self.loc1[1] - 4*15,6*6,4*15))
                all_sprites.add(enemy)
                enemies.add(enemy)

                # Se om man tagit sig till slutet och ladda in nästa karta
            if level_1:

                if not enemy1_alive:
                    enemies.empty()

                if player.rect.x > 1210:
                    
                    selectedWorld = world_level2                   
                    level_1=False
                    level_2=True
                    level_3=False
                    player.pos = pg.math.Vector2(player_starting_position)
                    player.rect.topleft = player_starting_position
                    player.vel = pg.math.Vector2(0, 0)
                    player.on_ground = False

                    solids.empty()

                    rects = (tuple(x) for x in level2Solids)
    
                    for rect in rects: 
                        block = Solids(pg.Rect(rect))
                        all_sprites.add(block)
                        solids.add(block)


            elif level_2 and enemy2_alive:
                # Sköter platsen där fienden befinner sig och att den vänder sig om vid en viss kordinat
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

                enemies.empty()
                enemy = Solids(pg.Rect(self.loc2[0], self.loc2[1] - 5*15, 8*6 ,5*15))
                all_sprites.add(enemy)
                enemies.add(enemy)
                # Se om man tagit sig till slutet och ladda in nästa karta
            if level_2:
                if not enemy2_alive:
                    enemies.empty()

                if player.rect.x > 1210:
                    selectedWorld = world_level3
                    level_1=False
                    level_2=False
                    level_3=True
                    player.pos = pg.math.Vector2(player_starting_position)
                    player.rect.topleft = player_starting_position
                    player.vel = pg.math.Vector2(0, 0)
                    player.on_ground = False

                    solids.empty()

                    rects = (tuple(x) for x in level3Solids)
    
                    for rect in rects:
                        block = Solids(pg.Rect(rect))
                        all_sprites.add(block)
                        solids.add(block)           


            elif level_3 and enemy3_alive:
                # Sköter platsen där fienden befinner sig och att den vänder sig om vid en viss kordinat
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

                enemies.empty()
                enemy = Solids(pg.Rect(self.loc3[0], self.loc3[1] - 8*15, 14*6, 8*15))
                all_sprites.add(enemy)
                enemies.add(enemy)

            if level_3:
                if not enemy3_alive:
                    enemies.empty()

                if player.rect.x > 1210:
                    pg.quit()
                    sys.exit()                

            # Du har ramlat ner
            if player.rect.y > 650:
                pg.quit()
                Game()
            
            for event in pg.event.get():
                
                # Gör så att koden avslutas när spelet stängs ner
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                elif event.type == pg.KEYDOWN:
                    # Gör så att man kan byta bana när man trycker på 1, 2, 3. Skulle kunna tas bort om man vill ge spelet till någon annan
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

                        rects = (tuple(x) for x in level2Solids)
        
                        for rect in rects: 
                            block = Solids(pg.Rect(rect))
                            all_sprites.add(block)
                            solids.add(block)
                    if event.key == pg.K_3:
                        selectedWorld = world_level3
                        level_1 = False
                        level_2 = False
                        level_3 = True
                        player.pos = pg.math.Vector2(player_starting_position)
                        player.rect.topleft = player_starting_position
                        player.vel = pg.math.Vector2(0, 0)
                        player.on_ground = False

                        solids.empty()

                        rects = (tuple(x) for x in level3Solids)
        
                        for rect in rects: 
                            block = Solids(pg.Rect(rect))
                            all_sprites.add(block)
                            solids.add(block)

                    # uppdaterar värden i player så att den ska kunna röra på sig
                    if event.key == pg.K_a:
                        player.vel.x = -220
                    elif event.key == pg.K_d:
                        player.vel.x = 220
                    elif event.key == pg.K_SPACE: 
                        if player.on_ground:
                            player.vel.y = -470
                            player.pos.y -= 20
                            player.on_ground = False
                    # När bulletklassen körs läggs alla bullets in i bullet spriten        
                    elif event.key == pg.K_f:  
                        bullet = Bullet(player.rect.midright, 1)
                        bullets.add(bullet)
                        all_sprites.add(bullet)
                    
                    # Omstart
                    elif event.key == pg.K_r: 
                        pg.quit()
                        Game()
                # Återställer värden på spelaren så att den blir statisk när man släpper knapparna        
                elif event.type == pg.KEYUP:
                    if event.key == pg.K_a and player.vel.x < 0:
                        player.vel.x = 0
                    elif event.key == pg.K_d and  player.vel.x > 0:
                        player.vel.x = 0
            # Uppdaterar alla sprites varje frame
            all_sprites.update(dt)

            # Ta bort bullet vid kollision med solids
            bullet_solids = pg.sprite.groupcollide(bullets, solids, True, False)
            for bullet in bullet_solids:
                bullet.kill

            # Samma sak vid kollision med enemy
            bullet_enemies = pg.sprite.groupcollide(bullets, enemies, True, False)
            for hit in bullet_enemies:
                bullet.kill
                score += 1
                if level_1:
                    if enemy1_alive:
                        enemy1_alive = False
                elif level_2:
                    if enemy2_alive:
                        enemy2_alive = False
                elif level_3:
                    if enemy3_alive:
                        enemy3_alive = False

            # Kollision mellan player och enemies
            collision = pg.sprite.spritecollide(player, enemies, False)
            for enemy in collision:
                score = 0
                pg.quit()
                Game()


            # Gör så att alla sprites är på sin nya position
            all_sprites.draw(screen)            
            pg.display.flip()

            # Gör så att spelet fungerar på samma sätt oavsätt fps
            dt = self.clock.tick(60) / 1000

Game()
