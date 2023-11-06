import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):

        self.enemy_img = pygame.image.load('Data_files/images/entities/enemy/idle/00.png')
        self.rev_enemy_img = pygame.transform.flip(pygame.image.load('Data_files/images/entities/enemy/idle/00.png'), True, False)


    def render_enemy(self, surf, e_type, loc, dir):
        #GROUND_LEVEL = 540

        if e_type == 1:
            img = pygame.transform.scale(self.enemy_img, (6*6, 4*15)) # Image + size
            rev_img = pygame.transform.scale(self.rev_enemy_img, (6*6, 4*15)) # Image + size
            pos = [loc[0], loc[1] - 4*15] # Location

            if dir:
                surf.blit(img, pos)
            else:
                surf.blit(rev_img, pos)
            
        elif e_type == 2:
            img = pygame.transform.scale(self.enemy_img, (8*6, 5*15))
            rev_img = pygame.transform.scale(self.rev_enemy_img, (8*6, 5*15)) # Image + size
            pos = (loc[0], loc[1] - 5*15)
            surf.blit(img, pos)

            if dir:
                surf.blit(img, pos)
            else:
                surf.blit(rev_img, pos)

        else:
            img = pygame.transform.scale(self.enemy_img, (14*6, 8*15))
            rev_img = pygame.transform.scale(self.rev_enemy_img, (14*6, 8*15)) # Image + size
            pos = (loc[0], loc[1] - 8*15)
            surf.blit(img, pos)

            if dir:
                surf.blit(img, pos)
            else:
                surf.blit(rev_img, pos)
