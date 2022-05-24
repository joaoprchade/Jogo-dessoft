# ===== Inicialização =====
# ----- Importa e inicia pacotes
# lagostinha
import pygame
import random

pygame.init()
pygame.mixer.init()

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

#imagem do zumbi
ZUMBI_WIDTH = 225*0.5
ZUMBI_HEIGHT = 225*0.5
zumbi_img = pygame.image.load('zumbi.png').convert_alpha()
zumbi_img = pygame.transform.scale(zumbi_img, (ZUMBI_WIDTH, ZUMBI_HEIGHT))

#planta e tiro
PLANT_WIDHT = 55
PLANT_HEIGHT = 55

planta_img = pygame.image.load('planta.png').convert_alpha()
planta_img = pygame.transform.scale(planta_img, (PLANT_WIDHT, PLANT_HEIGHT))
bullet_img = pygame.image.load('tiro.png').convert_alpha()

#muisc
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.set_volume(0.4)
#sol
SUN_WIDTH = 225*0.2
SUN_HEIGHT = 225*0.2
sun_img = pygame.image.load('sol.png').convert_alpha()
sun_img = pygame.transform.scale(sun_img, (SUN_WIDTH, SUN_HEIGHT))


class zumbis(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = random.choice(spawns_z)
        self.speedx = random.randint(1,10)
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
        self.rect.y = 0
        self.speedx = 0
        self.speedy = 2


    def update(self):
        # Atualizando a posição do sol
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.y > 300 :
            self.speedy = 0
            self.speedx = 0



class plantas(pygame.sprite.Sprite):
    def __init__(self, img, all_sprites, all_bullets, bullet_img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.right = 160
        self.rect.centery = HEIGHT /2
        
        self.speedy = 0
        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.bullet_img = bullet_img


    def update(self):
        # Atualizando a posição da planta
        self.rect.y += self.speedy
        

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        # A nova bala sera criada no centro vertical da planta (um pouco acima para encaixar na boca)
        new_bullet = Bullet(self.bullet_img, self.rect.right, self.rect.centery)
        self.all_sprites.add(new_bullet)
        self.all_bullets.add(new_bullet)

class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, right, centery):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centery = centery - 16
        self.rect.right = right
        self.speedx = 5  # Velocidade fixa para direita

    def update(self):
        # A bala só se move no eixo x
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.left < 0:
            self.kill()



        



game = True
        
        







#spawns (linha1,linha2...)! em y !!
l1 = 35
l2 = 115
l3 = 185
l4 = 255
l5 = 330
spawns_z = [l1,l2,l3,l4,l5]

spawns_s = [60, 60*2, 60*3, 60*4, 60*5 , 60*6, 60*7, 60*8, 60*9, 600]
sol_y = - 10
sol_x = random.choice(spawns_s)




#define os fps
clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

#criando a planta
player = plantas(planta_img, all_sprites, all_bullets, bullet_img)
all_sprites.add(player)



# Criando grupo de zumbis
zombies = pygame.sprite.Group()
for i in range (10):
    zumbi = zumbis(zumbi_img)
    all_sprites.add(zumbi)
    zombies.add(zumbi)


# Criando grupo de sois 
suns = pygame.sprite.Group()
for i in range (10):
    sol = sun(sun_img)
    suns.add(sol)





# ===== Loop principal ======
pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_UP:
                player.speedy -= 8
            if event.key == pygame.K_DOWN:
                player.speedy += 8
            if event.key == pygame.K_SPACE:
                player.shoot()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_UP:
                player.speedy += 8
            if event.key == pygame.K_DOWN:
                player.speedy -= 8

    hs = pygame.sprite.groupcollide(zombies, all_bullets, True, True) 
    hits = pygame.sprite.spritecollide(player, zombies, True)
    # atualiza a posição dos zumbis
    
    suns.update()
    all_sprites.update()
    
    
    
    # ----- Gera saídas

    #faz o mapa
    window.blit(image, (0, 0)) #mapa
    
    #desenha os elementos
    all_sprites.draw(window)
    

    

    hits = pygame.sprite.spritecollide(player, zombies, True)
    
    
    suns.draw(window)


    





    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

