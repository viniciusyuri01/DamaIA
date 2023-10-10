import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura, altura = 400, 400
tamanho_casa = largura // 8
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Damas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Função para desenhar o tabuleiro


def desenhar_tabuleiro():
    for row in range(8):
        for col in range(8):
            cor = BRANCO if (row + col) % 2 == 0 else PRETO
            pygame.draw.rect(tela, cor, (col * tamanho_casa,
                             row * tamanho_casa, tamanho_casa, tamanho_casa))

# Função principal do jogo


def main():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        desenhar_tabuleiro()
        pygame.display.flip()


if __name__ == "__main__":
    main()
