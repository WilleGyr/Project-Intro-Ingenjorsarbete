import pygame, json

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
GRAY = pygame.Color('gray24')
GRAVITY = 800

img = pygame.image.load("Data_files/images/entities/player/idle/00.png")

"""with open ("solids/solidsLevel1.json", "r") as file:
    level1Solids = json.load(file)

solid = pygame.sprite.Group()

for x, y in level1Solids:
    solid.add(Solids(x, y, 20, 20))"""    

class Player(pygame.sprite.Sprite):

    def __init__(self, pos, solids):
        super().__init__()
        self.image = img
        self.image = pygame.transform.scale(img, (20, 40))
        #self.image.fill(pygame.Color(0, 110, 170))
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)
        self.on_ground = False
        self.solids = solids

    def update(self, dt):
        # Move along x-axis.
        self.pos.x += self.vel.x * dt
        self.rect.x = self.pos.x

        collisions = pygame.sprite.spritecollide(self, self.solids, False)
        for solid in collisions:  # Horizontal collision occurred.
            if self.vel.x > 0:  # Moving right.
                self.rect.right = solid.rect.left  # Reset the rect pos.
            elif self.vel.x < 0:  # Moving left.
                self.rect.left = solid.rect.right  # Reset the rect pos.
            self.pos.x = self.rect.x  # Update the actual x-position.

        # Move along y-axis.
        self.pos.y += self.vel.y * dt
        # +1 to check if we're on a platform each frame.
        self.rect.y = self.pos.y + 1
        # Prevent air jumping when falling.
        if self.vel.y > 0:
            self.on_ground = False

        collisions = pygame.sprite.spritecollide(self, self.solids, False)
        for solid in collisions:  # Vertical collision occurred.
            if self.vel.y > 0:  # Moving down.
                self.rect.bottom = solid.rect.top  # Reset the rect pos.
                self.vel.y = 0  # Stop falling.
                self.on_ground = True
            elif self.vel.y < 0:  # Moving up.
                self.rect.top = solid.rect.bottom  # Reset the rect pos.
                self.vel.y = 0  # Stop jumping.
            self.pos.y = self.rect.y  # Update the actual y-position.

        # Stop the player at screen bottom.
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.vel.y = 0
            self.rect.bottom = WINDOW_HEIGHT
            self.pos.y = self.rect.y
            self.on_ground = True
        else:
            self.vel.y += GRAVITY * dt 

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, damage):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pygame.math.Vector2(400 * direction, 0)
        self.damage = damage  # Bullet's damage value

    def update(self, dt):
        self.rect.x += self.vel.x * dt

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, max_health):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(pygame.Color('green'))
        self.rect = self.image.get_rect(topleft=pos)
        self.health = max_health  # Enemy's health
        self.max_health = max_health


    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()  # Remove the enemy when health is zero or less

def main():
    clock = pygame.time.Clock()
    done = False
    dt = 0

    all_sprites = pygame.sprite.Group()
    blocks = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player((300, 100), blocks)
    all_sprites.add(player)

    enemy = Enemy((600, 570), max_health=50)  # Adjust max health as needed
    all_sprites.add(enemy)
    enemies.add(enemy)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.vel.x = -220
                if event.key == pygame.K_d:
                    player.vel.x = 220
                if event.key == pygame.K_SPACE:  # Jump
                    if player.on_ground:
                        player.vel.y = -470
                        player.pos.y -= 20
                        player.on_ground = False
                if event.key == pygame.K_f:  # Fire a bullet
                    bullet = Bullet(player.rect.midright, 1, damage=10)  # Pass damage value
                    bullets.add(bullet)
                    all_sprites.add(bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.vel.x < 0:
                    player.vel.x = 0
                elif event.key == pygame.K_d and player.vel.x > 0:
                    player.vel.x = 0

        all_sprites.update(dt)

        # Remove bullets that go off-screen
        for bullet in bullets.copy():
            if bullet.rect.right > WINDOW_WIDTH:
                bullets.remove(bullet)
                all_sprites.remove(bullet)

        # Check for collisions between bullets and enemies
        hits = pygame.sprite.groupcollide(bullets, enemies, True, False)
        for bullet, enemy_list in hits.items():
            for enemy in enemy_list:
                enemy.take_damage(bullet.damage)  # Call the enemy's take_damage method

        screen.fill(GRAY)
        all_sprites.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()
    pygame.quit()
