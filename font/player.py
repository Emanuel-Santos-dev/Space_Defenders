import pygame
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_image = pygame.image.load('assets/images/player_char.png').convert_alpha()
        self.image = pygame.transform.scale(player_image, (50, 50))  # Ajuste do tamanho da nave
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = PLAYER_SPEED
        self.bullets = pygame.sprite.Group()

    def shoot(self):
        # Carrega a imagem do laser do jogador
        bullet_image = pygame.image.load('assets/images/player_laser_beam.png').convert_alpha()
        bullet_image = pygame.transform.scale(bullet_image, (10, 30))  # Ajusta o tamanho do laser
        bullet = Bullet(bullet_image, self.rect.centerx, self.rect.top)
        self.bullets.add(bullet)

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

        self.bullets.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -7  # Velocidade para cima

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()  # Remove o tiro se sair da tela
