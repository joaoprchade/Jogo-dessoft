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

assets = {}
# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
assets['image'] = pygame.image.load('mapa.jpg').convert()
assets['image'] = pygame.transform.scale(assets['image'], (WIDTH, HEIGHT))

#imagem do zumbi
ZUMBI_WIDTH = 225*0.5
ZUMBI_HEIGHT = 225*0.5
assets['zumbi_img'] = pygame.image.load('zumbi.png').convert_alpha()
assets['zumbi_img'] = pygame.transform.scale(assets['zumbi_img'], (ZUMBI_WIDTH, ZUMBI_HEIGHT))

#planta e tiro
PLANT_WIDHT = 55
PLANT_HEIGHT = 55

assets['planta_img'] = pygame.image.load('planta.png').convert_alpha()
assets['planta_img'] = pygame.transform.scale(assets['planta_img'] , (PLANT_WIDHT, PLANT_HEIGHT))
assets['bullet_img'] = pygame.image.load('tiro.png').convert_alpha()

dance = []
for i in range(12):
    # Os arquivos de animação são numerados de 00 a 12
    filename = 'Peashooter_{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (32, 32))
    dance.append(img)
    assets['dance'] = dance







#muisc
pygame.mixer.music.load('theme.mp3')
pygame.mixer.music.set_volume(0.2)
assets['hit_sound'] = pygame.mixer.Sound('hit.mp3')
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
        self.rect.x = 1800
        self.rect.y = random.choice(spawns_z)
        self.speedx = random.randint(1,6)
        self.speedy = 0

        # animaçao zumbis
        self.sprites = []
        self.sprites.append(pygame.image.load('Zombie_0.png'))
        self.sprites.append(pygame.image.load('Zombie_1.png'))
        self.sprites.append(pygame.image.load('Zombie_2.png'))
        self.sprites.append(pygame.image.load('Zombie_3.png'))
        self.sprites.append(pygame.image.load('Zombie_4.png'))
        self.sprites.append(pygame.image.load('Zombie_5.png'))
        self.sprites.append(pygame.image.load('Zombie_6.png'))
        self.sprites.append(pygame.image.load('Zombie_7.png'))
        self.sprites.append(pygame.image.load('Zombie_8.png'))
        self.sprites.append(pygame.image.load('Zombie_9.png'))
        self.sprites.append(pygame.image.load('Zombie_10.png'))
        self.sprites.append(pygame.image.load('Zombie_11.png'))
        self.sprites.append(pygame.image.load('Zombie_12.png'))
        self.sprites.append(pygame.image.load('Zombie_13.png'))
        self.sprites.append(pygame.image.load('Zombie_14.png'))
        self.sprites.append(pygame.image.load('Zombie_15.png'))
        self.sprites.append(pygame.image.load('Zombie_16.png'))
        self.sprites.append(pygame.image.load('Zombie_17.png'))
        self.sprites.append(pygame.image.load('Zombie_18.png'))
        self.sprites.append(pygame.image.load('Zombie_19.png'))
        self.sprites.append(pygame.image.load('Zombie_20.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

    def update(self):
        # Atualizando a posição do zumbi
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0:
            self.rect.x = 800
            self.rect.y = random.choice(spawns_z)
            self.speedx = random.randint(3,10)
            self.speedy = 0

        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]


class sun(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(spawns_s)
        self.rect.y = 0
        self.speedx = 0
        self.speedy = random.randint(1,6)

        self.sprites = []
        self.sprites.append(pygame.image.load('Sun_0.png'))
        self.sprites.append(pygame.image.load('Sun_1.png'))
        self.sprites.append(pygame.image.load('Sun_2.png'))
        self.sprites.append(pygame.image.load('Sun_3.png'))
        self.sprites.append(pygame.image.load('Sun_4.png'))
        self.sprites.append(pygame.image.load('Sun_5.png'))
        self.sprites.append(pygame.image.load('Sun_6.png'))
        self.sprites.append(pygame.image.load('Sun_7.png'))
        self.sprites.append(pygame.image.load('Sun_8.png'))
        self.sprites.append(pygame.image.load('Sun_9.png'))
        self.sprites.append(pygame.image.load('Sun_10.png'))
        self.sprites.append(pygame.image.load('Sun_11.png'))
        self.sprites.append(pygame.image.load('Sun_12.png'))
        self.sprites.append(pygame.image.load('Sun_13.png'))
        self.sprites.append(pygame.image.load('Sun_14.png'))
        self.sprites.append(pygame.image.load('Sun_15.png'))
        self.sprites.append(pygame.image.load('Sun_16.png'))
        self.sprites.append(pygame.image.load('Sun_17.png'))
        self.sprites.append(pygame.image.load('Sun_18.png'))
        self.sprites.append(pygame.image.load('Sun_19.png'))
        self.sprites.append(pygame.image.load('Sun_20.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        
        

    def update(self):
        # Atualizando a posição do sol
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.y > 300 :
            self.speedy = 0
            self.speedx = 0
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]



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

        self.sprites = []
        self.sprites.append(pygame.image.load('Peashooter_0.png'))
        self.sprites.append(pygame.image.load('Peashooter_1.png'))
        self.sprites.append(pygame.image.load('Peashooter_2.png'))
        self.sprites.append(pygame.image.load('Peashooter_3.png'))
        self.sprites.append(pygame.image.load('Peashooter_4.png'))
        self.sprites.append(pygame.image.load('Peashooter_5.png'))
        self.sprites.append(pygame.image.load('Peashooter_6.png'))
        self.sprites.append(pygame.image.load('Peashooter_7.png'))
        self.sprites.append(pygame.image.load('Peashooter_8.png'))
        self.sprites.append(pygame.image.load('Peashooter_9.png'))
        self.sprites.append(pygame.image.load('Peashooter_10.png'))
        self.sprites.append(pygame.image.load('Peashooter_11.png'))
        self.sprites.append(pygame.image.load('Peashooter_12.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]


    def update(self):
        # Atualizando a posição da planta
        self.rect.y += self.speedy
        

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

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
        self.speedx = 10  # Velocidade fixa para direita

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

#spawns dos sois 
spawns_s = [60, 60*2, 60*3, 60*4 , 60*5 , 60*6, 60*7 , 60*8, 60*9, 600 ]
sol_y = - 10
sol_x = random.choice(spawns_s)



#define os fps
clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

#criando a planta
player = plantas(assets['planta_img'], all_sprites, all_bullets, assets['bullet_img'])
all_sprites.add(player)



# Criando grupo de zumbis
zombies = pygame.sprite.Group()
for i in range (10):
    zumbi = zumbis(assets['zumbi_img'])
    all_sprites.add(zumbi)
    zombies.add(zumbi)


# Criando grupo de sois 
suns = pygame.sprite.Group()
for i in range (1):
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
    for kills in hs: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
        # O meteoro e destruido e precisa ser recriado
        assets['hit_sound'].play()
        m = zumbis(img)
        all_sprites.add(m)
        zombies.add(m)
        



        


    
    # atualiza a posição dos zumbis
    
    suns.update()
    all_sprites.update()
    
    
    
    # ----- Gera saídas

    #faz o mapa
    window.blit(assets['image'], (0, 0)) #mapa
    
    #desenha os elementos
    all_sprites.draw(window)
    
    suns.draw(window)

    moving_sprites = pygame.sprite.Group()
    moving_sprites.update()

    
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

