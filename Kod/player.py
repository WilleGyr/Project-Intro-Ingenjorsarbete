import pygame as pg
from MapLoader import World 

pg.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
GRAY = pg.Color('gray24')
GRAVITY = 800


class Player(pg.sprite.Sprite):

    def __init__(self, pos, blocks):
        super().__init__()
        self.image = pg.Surface((30, 50))
        self.image.fill(pg.Color(0, 110, 170))
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pg.math.Vector2(0, 0)
        self.pos = pg.math.Vector2(pos)
        self.blocks = blocks
        self.on_ground = False

    def update(self, dt):
        # Move along x-axis.
        self.pos.x += self.vel.x * dt
        self.rect.x = self.pos.x

        collisions = pg.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:  # Horizontal collision occurred.
            if self.vel.x > 0:  # Moving right.
                self.rect.right = block.rect.left  # Reset the rect pos.
            elif self.vel.x < 0:  # Moving left.
                self.rect.left = block.rect.right  # Reset the rect pos.
            self.pos.x = self.rect.x  # Update the actual x-position.

        # Move along y-axis.
        self.pos.y += self.vel.y * dt
        # +1 to check if we're on a platform each frame.
        self.rect.y = self.pos.y + 1
        # Prevent air jumping when falling.
        if self.vel.y > 0:
            self.on_ground = False

        collisions = pg.sprite.spritecollide(self, self.blocks, False)
        for block in collisions:  # Vertical collision occurred.
            if self.vel.y > 0:  # Moving down.
                self.rect.bottom = block.rect.top  # Reset the rect pos.
                self.vel.y = 0  # Stop falling.
                self.on_ground = True
            elif self.vel.y < 0:  # Moving up.
                self.rect.top = block.rect.bottom  # Reset the rect pos.
                self.vel.y = 0  # Stop jumping.
            self.pos.y = self.rect.y  # Update the actual y-position.

        # Stop the player at screen bottom.
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.vel.y = 0
            self.rect.bottom = WINDOW_HEIGHT
            self.pos.y = self.rect.y
            self.on_ground = True
        else:
            self.vel.y += GRAVITY * dt  # Gravity
class Bullet(pg.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        self.image = pg.Surface((10, 5))
        self.image.fill(pg.Color('red'))
        self.rect = self.image.get_rect(topleft=pos)
        self.vel = pg.math.Vector2(400 * direction, 0)

    def update(self, dt):
        self.rect.x += self.vel.x * dt

def main():
    clock = pg.time.Clock()
    done = False
    dt = 0

    all_sprites = pg.sprite.Group()
    blocks = pg.sprite.Group()
    bullets = pg.sprite.Group()

    player = Player((300, 100), blocks)
    all_sprites.add(player)



    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    player.vel.x = -220
                if event.key == pg.K_d:
                    player.vel.x = 220
                if event.key == pg.K_SPACE:  # Jump
                    if player.on_ground:
                        player.vel.y = -470
                        player.pos.y -= 20
                        player.on_ground = False
                if event.key == pg.K_f:  # Fire a bullet
                    bullet = Bullet(player.rect.midright, 1)
                    bullets.add(bullet)
                    all_sprites.add(bullet)
            elif event.type == pg.KEYUP:
                if event.key == pg.K_a and player.vel.x < 0:
                    player.vel.x = 0
                elif event.key == pg.K_d and player.vel.x > 0:
                    player.vel.x = 0

        all_sprites.update(dt)

        # Remove bullets that go off-screen
        for bullet in bullets.copy():
            if bullet.rect.right > WINDOW_WIDTH:
                bullets.remove(bullet)
                all_sprites.remove(bullet)

        screen.fill(GRAY)
        all_sprites.draw(screen)

        pg.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    main()
    pg.quit()
