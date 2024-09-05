import pygame
import random

# Inicializando o Pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simulação de Fordismo')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Frames por segundo
FPS = 60

# Classe para representar o produto na linha de produção
class Produto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stage = 0  # Fase de produção
        self.color = WHITE  # Cor inicial do produto

    def update(self):
        # Movendo o produto na linha de produção
        self.x += 2

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))

    def process(self):
        # Simulando as diferentes fases do produto na linha de produção
        if self.stage == 0:
            self.color = BLUE  # Montagem
        elif self.stage == 1:
            self.color = GREEN  # Pintura
        elif self.stage == 2:
            self.color = RED  # Embalagem

# Classe para representar uma máquina na linha de produção
class Maquina:
    def __init__(self, x, y, stage):
        self.x = x
        self.y = y
        self.stage = stage  # Qual fase da produção esta máquina representa

    def draw(self, screen):
        pygame.draw.rect(screen, GRAY, (self.x, self.y, 60, 60))

    def processar_produto(self, produto):
        # Se o produto estiver nesta fase da produção, processá-lo
        if produto.x >= self.x and produto.stage == self.stage:
            produto.stage += 1
            produto.process()

# Função principal
def main():
    clock = pygame.time.Clock()
    
    # Criação de máquinas (3 máquinas representando 3 fases de produção)
    maquinas = [
        Maquina(200, HEIGHT // 2 - 30, 0),  # Montagem
        Maquina(400, HEIGHT // 2 - 30, 1),  # Pintura
        Maquina(600, HEIGHT // 2 - 30, 2),  # Embalagem
    ]
    
    # Lista para armazenar os produtos
    produtos = []

    # Contador de tempo para gerar novos produtos
    product_timer = 0

    # Loop principal do jogo
    running = True
    while running:
        screen.fill(WHITE)
        
        # Saída do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    if produtos:
                        produto = produtos[0]
                        produto.stage += 1
                        produto.process()

        # Gerar um novo produto a cada intervalo de tempo
        product_timer += 1
        if product_timer >= 120:  # Gera um produto a cada 2 segundos
            produtos.append(Produto(50, HEIGHT // 2 - 25))
            product_timer = 0

        # Atualizar e desenhar cada produto
        for produto in produtos:
            produto.update()
            produto.draw(screen)
            for maquina in maquinas:
                maquina.processar_produto(produto)

        # Desenhar as máquinas
        for maquina in maquinas:
            maquina.draw(screen)

        # Atualizar a tela
        pygame.display.flip()

        # Manter o jogo rodando na velocidade correta
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()