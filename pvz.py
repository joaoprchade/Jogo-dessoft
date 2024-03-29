# ===== Inicialização =====
# ----- Importa e inicia pacotes
# lagostinha
from typing import final
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
font = pygame.font.SysFont('Pokemon GB.ttf', 60)


# ----- Inicia assets
assets['menu_img'] = pygame.image.load(
    'assets/Imagens/menu_final.png').convert()
assets['menu_img'] = pygame.transform.scale(
    assets['menu_img'], (WIDTH, HEIGHT))

assets['image'] = pygame.image.load('assets/Imagens/mapa.jpg').convert()
assets['image'] = pygame.transform.scale(assets['image'], (WIDTH, HEIGHT))

assets['game_over'] = pygame.image.load(
    'assets/Imagens/game_over.png').convert()
assets['game_over'] = pygame.transform.scale(
    assets['game_over'], (WIDTH, HEIGHT))

# imagem do zumbi
ZUMBI_WIDTH = 225*0.5
ZUMBI_HEIGHT = 225*0.5
assets['zumbi_img'] = pygame.image.load(
    'assets/Imagens/zumbi.png').convert_alpha()
assets['zumbi_img'] = pygame.transform.scale(
    assets['zumbi_img'], (ZUMBI_WIDTH, ZUMBI_HEIGHT))

# spawns (linha1,linha2...)! em y !!
l1 = 35
l2 = 115
l3 = 185
l4 = 255
l5 = 330
spawns_z = [l1, l2, l3, l4, l5]

# planta e tiro
PLANT_WIDHT = 55
PLANT_HEIGHT = 55

assets['planta_img'] = pygame.image.load(
    'assets/Imagens/planta.png').convert_alpha()
assets['planta_img'] = pygame.transform.scale(
    assets['planta_img'], (PLANT_WIDHT, PLANT_HEIGHT))
assets['bullet_img'] = pygame.image.load(
    'assets/Imagens/tiro.png').convert_alpha()


dance = []
for i in range(12):
    # Os arquivos de animação são numerados de 00 a 12
    filename = 'assets/Imagens/Peashooter_{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (32, 32))
    dance.append(img)
    assets['dance'] = dance

# muisc
pygame.mixer.music.load('assets/Imagens/theme.mp3')
pygame.mixer.music.set_volume(0.2)
assets['hit_sound'] = pygame.mixer.Sound('assets/Imagens/hit.mp3')
# sol
SUN_WIDTH = 225*0.2
SUN_HEIGHT = 225*0.2
sun_img = pygame.image.load('assets/Imagens/sol.png').convert_alpha()
sun_img = pygame.transform.scale(sun_img, (SUN_WIDTH, SUN_HEIGHT))

qtd_sois = 0
la = 1


class Personagem(pygame.sprite.Sprite):
    def __init__(self, img, rect, current_sprite, speedy, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = rect
        self.current_sprite = current_sprite
        self.speedy = speedy
        self.rect.x = x
        self.rect.y = y


class Zumbis(Personagem):
    def __init__(self, img, x, y):
        super().__init__(img, img.get_rect(), 0, 0, 1800, random.choice(spawns_z))

        self.vivo = False
        self.speedx = random.randint(1, 6) * la

        # animaçao zumbis
        self.sprites = []
        self.aggregate_sprites()

        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()

    def aggregate_sprites(self):
        for i in range(20 + 1):
            self.sprites.append(pygame.image.load(
                f'assets/Imagens/Zombie_{i}.png'))

    def aggregate_sprites(self):
        for i in range(20 + 1):
            self.sprites.append(pygame.image.load(
                f'assets/Imagens/Zombie_{i}.png'))

    def update(self):
        # Atualizando a posição do zumbi
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.x < 0:
            self.rect.x = 800
            self.rect.y = random.choice(spawns_z)
            self.speedx = random.randint(3, 10)
            self.speedy = 0
            if self.vivo:
                vidas.vidas -= 1
                self.vivo = False
        else:
            self.vivo = True

        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]


class Sun(Personagem):
    def __init__(self, img):
        super().__init__(img, img.get_rect(), 0,
                         random.randint(1, 4), random.choice(spawns_s), -500)

        self.speedx = 0

        self.sprites = []
        self.aggregate_sprites()

        self.image = self.sprites[self.current_sprite]

    def aggregate_sprites(self):
        for i in range(20 + 1):
            self.sprites.append(pygame.image.load(
                f'assets/Imagens/Sun_{i}.png'))

    def update(self):
        # Atualizando a posição do sol
        self.rect.x -= self.speedx
        self.rect.y += self.speedy
        if self.rect.y > 300:
            self.speedy = 0
            self.speedx = 0
        self.current_sprite += 1
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]


class Plantas(Personagem):
    def __init__(self, img, all_sprites, all_bullets, bullet_img):
        # Construtor da classe mãe (Sprite).
        super().__init__(img, img.get_rect(), 0, 0, 160, HEIGHT / 2)

        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.bullet_img = bullet_img

        self.sprites = []
        self.aggregate_sprites()

        self.image = self.sprites[self.current_sprite]

    def aggregate_sprites(self):
        for i in range(12 + 1):
            self.sprites.append(pygame.image.load(
                f'assets/Imagens/Peashooter_{i}.png'))

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
        new_bullet = Bullet(
            self.bullet_img, self.rect.right, self.rect.centery)
        self.all_sprites.add(new_bullet)
        self.all_bullets.add(new_bullet)


class Bullet(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, right, centery):

        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.y = centery - 16
        self.rect.x = right
        self.speedx = 10  # Velocidade fixa para direita

    def update(self):
        # A bala só se move no eixo x
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.left < 0:
            self.kill()


class vidas:
    vidas = 3


# spawns dos sois
spawns_s = [60, 60*2, 60*3, 60*4, 60*5, 60*6, 60*7, 60*8, 60*9, 600]
sol_y = - 10
sol_x = random.choice(spawns_s)

# define os fps
clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()

# criando a planta
player = Plantas(assets['planta_img'], all_sprites,
                 all_bullets, assets['bullet_img'])
all_sprites.add(player)

# Criando grupo de zumbis
zombies = pygame.sprite.Group()
for i in range(5):
    zumbi = Zumbis(assets['zumbi_img'], 1800, random.choice(spawns_z))
    all_sprites.add(zumbi)
    zombies.add(zumbi)

# Criando grupo de sois
suns = pygame.sprite.Group()
for i in range(1):
    sol = Sun(sun_img)
    suns.add(sol)


def draw_text(texto, font, cor, x, y):
    img = font.render(texto, True, cor)
    window.blit(img, (x, y))


vel_px = 8
vel_py = 8

# ===== Loop principal ======
pygame.mixer.music.play(loops=-1)


game = True
menu = True
jogo = False
end = False
start = True

while game:

    vidas.vidas = 3
    while menu:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jogo = True
                    menu = False
                    start = True
         # ----- Gera saídas
        # faz o mapa
        window.blit(assets['menu_img'], (0, 0))  # mapa
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    while jogo:
        clock.tick(FPS)

        if vidas.vidas == 0:
            end = True
            jogo = False
            start = False

        draw_text('{}'.format(qtd_sois), font, (0, 0, 0), 50, 50)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_w:
                    player.speedy -= vel_py
                if event.key == pygame.K_s:
                    player.speedy += vel_px
                if event.key == pygame.K_SPACE:
                    player.shoot()
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_w:
                    player.speedy += vel_py
                if event.key == pygame.K_s:
                    player.speedy -= vel_px
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and sol.rect.y > 15:
                    sol.rect.y = -500
                    sol.rect.x = random.choice(spawns_s)
                    sol.speedy = random.randint(1, 6)
                    qtd_sois += 25
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u and qtd_sois >= 100:
                    vel_py += 2
                    vel_px += 2
                    qtd_sois -= 100

        hs = pygame.sprite.groupcollide(
            zombies, all_bullets, True, True, pygame.sprite.collide_mask)
        # As chaves são os elementos do primeiro grupo (zumbis) que colidiram com alguma bala
        for kills in hs:
            # O zumbi e destruido e precisa ser recriado
            assets['hit_sound'].play()
            m = Zumbis(img, 1800, random.choice(spawns_z))
            all_sprites.add(m)
            zombies.add(m)
            zombies.update()
        '''if vidas == 0:
            pygame.quit()'''

        # atualiza a posição dos sois
        suns.update()
        all_sprites.update()

        # ----- Gera saídas
        # faz o mapa
        window.blit(assets['image'], (0, 0))  # mapa

        # desenha os elementos
        all_sprites.draw(window)

        suns.draw(window)
        draw_text('{} '.format(qtd_sois), font, (255, 255, 0), 50, 50)
        window.blit(sun_img, (10, 45))
        moving_sprites = pygame.sprite.Group()
        moving_sprites.update()

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

        while end:
            # ----- Trata eventos
            for event in pygame.event.get():
                # ----- Verifica consequências
                if event.type == pygame.QUIT:
                    game = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jogo = True
                        end = False
                        vidas.vidas = 3
                        qtd_sois = 0

            # ----- Gera saídas
            # faz o mapa
            window.blit(assets['game_over'], (0, 0))  # mapa
            # ----- Atualiza estado do jogo
            pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
