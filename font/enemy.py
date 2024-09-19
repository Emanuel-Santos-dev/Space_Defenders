import pygame
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        enemy_image = pygame.image.load('assets/images/enemy_char.png').convert_alpha()
        self.image = pygame.transform.scale(enemy_image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = ENEMY_SPEED
        self.direction = 1
        self.bullets = pygame.sprite.Group()
        self.shoot_delay = pygame.time.get_ticks() + 1000

    def update(self):
        self.rect.x += self.speed_x * self.direction

        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 80

        now = pygame.time.get_ticks()
        if now >= self.shoot_delay:
            self.shoot()
            self.shoot_delay = now + 1500

        self.bullets.update()

        if self.rect.bottom > SCREEN_HEIGHT:
            self.kill()

    def shoot(self):
        # Carrega a imagem do laser do inimigo
        bullet_image = pygame.image.load('assets/images/enemy_laser_beam.png').convert_alpha()
        bullet_image = pygame.transform.scale(bullet_image, (10, 30))  
        bullet_rect = bullet_image.get_rect(midtop=self.rect.midbottom)
        bullet = EnemyBullet(bullet_image, bullet_rect)
        self.bullets.add(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, image, rect):
        super().__init__()
        self.image = image
        self.rect = rect
        self.speed = 7

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
