# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 635*1.3
HEIGHT = 380*1.3
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lsvmsss')


# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
mapa_img = pygame.image.load('Jogo-dessoft/assets/Imagens/mapa.jpg').convert()
image = pygame.transform.scale(mapa_img, (WIDTH, HEIGHT))


ZUMBI_WIDTH = 225*0.5
ZUMBI_HEIGHT = 225*0.5
zumbi_img = pygame.image.load('Jogo-dessoft/assets/Imagens/zumbi.png').convert()
zumbi_img_small = pygame.transform.scale(zumbi_img, (ZUMBI_WIDTH, ZUMBI_HEIGHT))

zumbi_x = 635
zumbi_y = 330


zumbi_speedx = 0.01

#spawns (linha1,linha2...) precisa descobrir a altura de cada uma!!
l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0

spawns = [l1,l2,l3,l4,l5]





# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    zumbi_x -= zumbi_speedx

    #if zumbi_x < 10:
        #print("Os zumbis devoraram seus miólos")
    # ----- Gera saídas

    #window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (0, 0))
    window.blit(zumbi_img_small, (zumbi_x, zumbi_y))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

