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

class sun(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(spawns_s)
        self.rect.y = 00
        self.speedx = 0
        self.speedy = 2


    def update(self):
        # Atualizando a posição do sol
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.y > 300 :
            self.speedy = 0
            self.speedx = 0
        


game = True
        
        


#imagem do zumbi
ZUMBI_WIDTH = 225*0.5
ZUMBI_HEIGHT = 225*0.5
zumbi_img = pygame.image.load('zumbi.png').convert_alpha()
zumbi_img = pygame.transform.scale(zumbi_img, (ZUMBI_WIDTH, ZUMBI_HEIGHT))

#sol
SUN_WIDTH = 225*0.2
SUN_HEIGHT = 225*0.2
sun_img = pygame.image.load('sol.png').convert_alpha()
sun_img = pygame.transform.scale(sun_img, (SUN_WIDTH, SUN_HEIGHT))






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
FPS = 30


# Criando grupo de zumbis
zombies = pygame.sprite.Group()
for i in range (10):
    zumbi = zumbis(zumbi_img)
    zombies.add(zumbi)

# Criando grupo de sois 
suns = pygame.sprite.Group()
for i in range (10):
    sol = sun(sun_img)
    suns.add(sol)



# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # atualiza a posição dos zumbis
    zombies.update()
    suns.update()
    
    
    # ----- Gera saídas

    #faz o mapa
    window.blit(image, (0, 0)) #mapa
    
    #desenha os elementos
    zombies.draw(window)

    suns.draw(window)

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

