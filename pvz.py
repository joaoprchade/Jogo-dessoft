# ===== Inicialização =====
# ----- Importa e inicia pacotes
# lagostinha
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 635*1.3
HEIGHT = 380*1.3
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lsvmsss')


# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
mapa_img = pygame.image.load('mapa.jpg').convert()
image = pygame.transform.scale(mapa_img, (WIDTH, HEIGHT))


class zumbis(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = random.choice(spawns_z)
        self.speedx = 1
        self.speedy = 0


    def update(self):
        # Atualizando a posição do zumbi
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        
        


#imagem do zumbi
ZUMBI_WIDTH = 225*0.5
ZUMBI_HEIGHT = 225*0.5
zumbi_img = pygame.image.load('zumbi.png').convert_alpha()
zumbi_img_small = pygame.transform.scale(zumbi_img, (ZUMBI_WIDTH, ZUMBI_HEIGHT))

SUN_WIDTH = 225*0.2
SUN_HEIGHT = 225*0.2
sun_img = pygame.image.load('sol.png').convert_alpha()
sun_img_small = pygame.transform.scale(sun_img, (SUN_WIDTH, SUN_HEIGHT))






sol_speed = 2

#spawns (linha1,linha2...)! em y !!
l1 = 35
l2 = 115
l3 = 185
l4 = 255
l5 = 330

spawns_z = [l1,l2,l3,l4,l5]

#spawns dos sois 
spawns_s = [60, 60*2, 60*3, 60*4 , 60*5 , 60*6, 60*7 , 60*8, 60*9, 600 ]



sol_y = - 10
sol_x = random.choice(spawns_s)



#define os fps
clock = pygame.time.Clock()
FPS = 60


# Criando dois zumbis
zumbi1 = zumbis(zumbi_img)
zumbi2 = zumbis(zumbi_img) 
# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # atualiza a posição dos zumbis
    zumbi1.update()
    zumbi2.update()
    sol_y += sol_speed
    if sol_y > 300:
        sol_speed = 0
    
    # ----- Gera saídas

    #faz o mapa (o mapa aparece em 0,0, os zumbis nas coordenadas rect(atualizado com o handout de classes) )
    window.blit(image, (0, 0)) #mapa
    window.blit(zumbi_img_small, (zumbi1.rect)) #zumbi1
    window.blit(zumbi_img_small, (zumbi2.rect)) #zumbi2

    window.blit(sun_img_small, (sol_x, sol_y)) #sol

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

