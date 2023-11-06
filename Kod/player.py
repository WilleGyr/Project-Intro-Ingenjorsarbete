import pygame

img = pygame.image.load("Data_files/images/entities/player/idle/00.png")

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, solids):
        super().__init__()
        self.image = img
        self.image = pygame.transform.scale(img, (20, 40))
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)
        self.on_ground = False
        self.solids = solids

    def update(self, dt):
        # Rörelse på x-axeln
        self.pos.x += self.vel.x * dt
        self.rect.x = self.pos.x

        # kollision i x-led
        collisions = pygame.sprite.spritecollide(self, self.solids, False)
        for solid in collisions:
            if self.vel.x > 0:  
                self.rect.right = solid.rect.left  
            elif self.vel.x < 0:  
                self.rect.left = solid.rect.right  
            self.pos.x = self.rect.x 

        # Rörelse i y-led
        self.pos.y += self.vel.y * dt
        self.rect.y = self.pos.y + 1
        if self.vel.y > 0:
            self.on_ground = False

        # kollision i y-led
        collisions = pygame.sprite.spritecollide(self, self.solids, False)
        for solid in collisions:
            if self.vel.y > 0:
                self.rect.bottom = solid.rect.top
                self.vel.y = 0
                self.on_ground = True
            elif self.vel.y < 0:
                self.rect.top = solid.rect.bottom  
                self.vel.y = 0
            self.pos.y = self.rect.y 
        
        #Ger en konstant rörelse neråt
        self.vel.y += 800 * dt


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(pygame.Color('grey'))
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.math.Vector2(400 * direction, 0)

    def update(self, dt):
        # skottet åker i konstant hastighet oavsett fps
        self.rect.x += self.vel.x * dt

