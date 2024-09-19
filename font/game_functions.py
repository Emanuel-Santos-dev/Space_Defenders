import pygame
import random
from .player import Player
from .enemy import Enemy
from .settings import SCREEN_HEIGHT, SCREEN_WIDTH

# Variáveis para controle de pontuação e recorde
high_score = 0

def handle_events(player):
    """Gerencia os eventos do jogo, como pressionar teclas e sair do jogo."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]:
        player.update(keys_pressed)
    if keys_pressed[pygame.K_SPACE]:
        player.shoot()

def update_game_state(all_sprites, enemies, player, keys_pressed, score):
    """Atualiza o estado do jogo e retorna a pontuação atualizada."""
    
    # Atualiza todos os sprites, passando os argumentos necessários
    for sprite in all_sprites:
        if isinstance(sprite, Player):
            sprite.update(keys_pressed)
        else:
            sprite.update()

    # Verifica se algum tiro do jogador colidiu com inimigos
    for bullet in player.bullets:
        hits = pygame.sprite.spritecollide(bullet, enemies, True)
        if hits:
            bullet.kill()
            score += 10  # Incrementa a pontuação ao destruir um inimigo

    # Verifica se algum tiro dos inimigos colidiu com o jogador
    for enemy in enemies:
        for bullet in enemy.bullets:
            if bullet.rect.colliderect(player.rect):
                player.kill()  # Remove o jogador se atingido
                return score  # Retorna a pontuação, encerrando o jogo

    # Cria novos inimigos se necessário
    if len(enemies) == 0:
        for i in range(5):  # Adicione um número fixo de inimigos
            x = random.randint(0, SCREEN_WIDTH - 50)
            y = random.randint(-150, -50)
            enemy = Enemy(x, y)
            enemies.add(enemy)
            all_sprites.add(enemy)

    # Atualiza a posição dos tiros
    for enemy in enemies:
        if random.randint(1, 100) > 98:  # Chance de disparar
            enemy.shoot()

    return score  # Retorna a pontuação atualizada




def draw_game_state(screen, all_sprites, stars, score):
    """Desenha o estado atual do jogo na tela."""
    screen.fill((0, 0, 0))  # Cor de fundo preta
    
    # Desenha as estrelas
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), star, 1)
    
    # Desenha todos os sprites
    all_sprites.draw(screen)
    
    # Exibe a pontuação atual no canto superior esquerdo
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score[0]}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

def game_over(screen, score):
    """Exibe a tela de Game Over e permite que o jogador volte ao menu principal."""
    global high_score

    # Verifica e atualiza o recorde
    if score > high_score:
        high_score = score

    font = pygame.font.Font(None, 74)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 0))
    screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))

    continue_text = font.render("Press ENTER to go to Main Menu", True, (255, 255, 255))
    screen.blit(continue_text, (SCREEN_WIDTH // 2 - continue_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False
                return  # Voltar ao menu principal


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((2, 2))  # Tamanho da estrela
        self.image.fill((255, 255, 255))  # Cor da estrela
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, 3)  # Velocidade de movimento

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:  # Voltar ao topo se sair da tela
            self.rect.bottom = 0
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.speed = random.randint(1, 3)  # Atualizar velocidade aleatoriamente

def create_stars(num_stars, screen_width, screen_height):
    """Cria uma lista de estrelas para o fundo do jogo."""
    stars = pygame.sprite.Group()
    for _ in range(num_stars):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        star = Star(x, y)
        stars.add(star)
    return stars
