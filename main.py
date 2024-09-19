import pygame
import random
import pickle
import os
from font.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from font.player import Player
from font.enemy import Enemy
from font.game_functions import create_stars, update_game_state
from font.menu import main_menu

# Função para carregar o high score de um arquivo
def load_high_score():
    if os.path.exists('high_score.pkl'):
        with open('high_score.pkl', 'rb') as f:
            return pickle.load(f)
    return 0  # Se o arquivo não existir, retorna 0

# Função para salvar o high score em um arquivo
def save_high_score(score):
    with open('high_score.pkl', 'wb') as f:
        pickle.dump(score, f)

def main():
    global high_score
    high_score = load_high_score()  # Carrega o high score

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Defenders")

    clock = pygame.time.Clock()

    # Inicializa os sons
    pygame.mixer.music.load('assets/sounds/soundtrack.mp3')
    laser_sound = pygame.mixer.Sound('assets/sounds/laser_beam.mp3')
    pygame.mixer.music.set_volume(0.5)  # Ajusta o volume da trilha sonora
    laser_sound.set_volume(0.5)  # Ajusta o volume do som de disparo

    while True:
        main_menu(screen, high_score)  # Passa a pontuação mais alta para o menu
        score = start_game(screen, clock, laser_sound)  # Recebe a pontuação do jogo
        if score > high_score:
            high_score = score  # Atualiza a pontuação mais alta
            save_high_score(high_score)  # Salva a nova pontuação mais alta

def start_game(screen, clock, laser_sound):
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    stars = create_stars(100, SCREEN_WIDTH, SCREEN_HEIGHT)  # Criar estrelas

    for i in range(5):
        x = random.randint(0, SCREEN_WIDTH - 50)
        y = random.randint(-100, -40)
        enemy = Enemy(x, y)
        enemies.add(enemy)
        all_sprites.add(enemy)

    running = True
    score = 0

    # Toca a trilha sonora quando o jogo começa
    pygame.mixer.music.play(-1)  # -1 para tocar em loop

    while running:
        keys_pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    laser_sound.play()  # Toca o som do laser

        score = update_game_state(all_sprites, enemies, player, keys_pressed, score)

        screen.fill((0, 0, 0))  # Limpa a tela

        # Desenha as estrelas
        for star in stars:
            pygame.draw.rect(screen, (255, 255, 255), star)

        # Desenha todos os sprites
        all_sprites.draw(screen)
        player.bullets.draw(screen)  # Desenha as balas do jogador
        for enemy in enemies:
            enemy.draw(screen)  # Desenha os inimigos e suas balas
            enemy.bullets.draw(screen)  # Desenha as balas dos inimigos

        pygame.display.flip()  # Atualiza a tela
        clock.tick(FPS)

        # Verifica se o jogador morreu
        if not player.alive():
            running = False  # Sai do loop se o jogador morreu

    pygame.mixer.music.stop()  # Para a música quando o jogo termina
    # Exibe a tela de game over e retorna a pontuação
    game_over(screen, score)
    return score  # Retorna a pontuação para ser usada no menu

def game_over(screen, score):
    global high_score

    # Atualiza o recorde se necessário
    if score > high_score:
        high_score = score
        save_high_score(high_score)  # Salva o novo high score imediatamente

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

if __name__ == "__main__":
    main()
