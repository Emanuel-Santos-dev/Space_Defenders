import pygame
import sys
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT  # Importa as configurações da pasta 'font'

def draw_text(surface, text, size, color, x, y):
    """Desenha o texto na superfície fornecida."""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def main_menu(screen, high_score):
    """Exibe o menu principal do jogo, incluindo a pontuação mais alta."""
    pygame.display.set_caption("Menu Principal")
    clock = pygame.time.Clock()
    menu_running = True
    
    # Inicializa o módulo de fontes
    pygame.font.init()
    
    while menu_running:
        screen.fill((0, 0, 0))  # Cor de fundo preta

        draw_text(screen, "Space Defenders", 64, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150)
        draw_text(screen, f"Pontuação mais alta: {high_score}", 36, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
        draw_text(screen, "Pressione Enter para Jogar", 36, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text(screen, "Pressione Esc para Sair", 36, (255, 255, 255), SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True  # Retorna para iniciar o jogo
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()
        clock.tick(60)
