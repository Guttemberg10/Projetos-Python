# Jogo de luta entre dois pokémons
# Guttemberg
# 16/11/2022

from random import random
import pygame
from pygame.locals import *
from sys import exit
from random import randrange

pygame.init()

largura = 436
altura = 322
relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
fundo = pygame.image.load("sprites/fundo.png")

# Variáveis de ataque dos jogadores:
cont_mov_pik = 0
cont_mov_bul = 0

pygame.mixer.music.load("sound/musica_fundo.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.7)
fonte = pygame.font.SysFont('comic sans', 33, True, False)
fonte_nomes = pygame.font.SysFont('comic sans', 18, True, False)

# Importando sons em variáveis
pika_sound = pygame.mixer.Sound("sound/Pikachu.wav")
bulb_sound = pygame.mixer.Sound("sound/Bulbasaur.wav")
bulb_atack = pygame.mixer.Sound("sound/chicote_bulb.wav")
pika_atack = pygame.mixer.Sound("sound/choque_pika.wav")

pikachu = pygame.image.load("sprites/pikachu.png")
pikachu = pygame.transform.scale(pikachu, (1600 * 2, 1000 * 2))
x_pikachu = 0
x = 82
y = 208
y_pikachu = 85
x_fundo = -101

bul = pygame.image.load("sprites/bulb.png")
bul = pygame.transform.scale(bul, (1600 * 2, 1000 * 2))
y_bul = 0
x_bul = 0
xb = 168
yb = 134

vida_1 = 186
ajustador = 30 #Ajusta o sangue do p1
vida_2 = 186

while True:
    relogio.tick(10)
    key = pygame.key.get_pressed()
    key_b = pygame.key.get_pressed()
    mensagem = 'KO'
    nome1 = 'Pikachu'
    nome2 = 'Bulbasauro'
    texto_KO = fonte.render(mensagem, False, (255, 255, 255))
    texto_nome1 = fonte_nomes.render(nome1, False, (255, 255, 0))
    texto_nome2 = fonte_nomes.render(nome2, False, (255, 255, 0))
    texto_KO_luz = fonte.render(mensagem, False, (21, 0, 96))

# Movimentação do P1:
    if key[K_d]:
        x += 10
        y_pikachu = 250
        if x_pikachu > 5:
            x_pikachu = 0
        if x >= 346:
            x = 346
        if colisao_p1.colliderect(colisao_p_p2):
            x = xb + 15
    elif key[K_a]:
        x -= 10
        y_pikachu = 168
        if x_pikachu > 5:
            x_pikachu = 0
        if x <= 10:
            x = 10
    else:
        if y_pikachu == 250 or x_pikachu > 6 and y_pikachu == 85:
            y_pikachu = 85
            x_pikachu = 0
        if y_pikachu == 168 or x_pikachu > 6 and y_pikachu == 0:
            y_pikachu = 0
            x_pikachu = 0

# Movimentação do P2:
    if cont_mov_bul == 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_r:
                    cont_mov_bul = 1
                    x_bul = 0
                    bulb_atack.play()
                    if y_bul == 0 or y_bul == 320:
                        y_bul = 635
                    elif y_bul == 160 or y_bul == 476:
                        y_bul = 790
                elif event.key == pygame.K_e:
                    x_pikachu = 0
                    cont_mov_pik = 1
                    pika_atack.play()
                    if y_pikachu == 0:
                        y_pikachu = 330
                    if y_pikachu == 85:
                        y_pikachu = 410
        if key_b[K_LEFT]:
            y_bul = 320
            if x_bul > 3:
                x_bul = 0
            xb -= 10
            if xb <= -100:
                xb = -100
            if colisao_p_p2.colliderect(colisao_p1):
                xb = x - 15
        elif key_b[K_RIGHT]:
            y_bul = 476
            if x_bul > 3:
                x_bul = 0
            xb += 10
            if xb >= largura - 190:
                xb = largura - 190
        else:
            if y_bul == 320:
                y_bul = 0
            elif y_bul == 476:
                y_bul = 160
            if x_bul > 8 and y_bul == 0 or x_bul > 8 and y_bul == 476 or y_bul == 160 and x_bul > 8:
                x_bul = 0
        if x >= largura - 90:
            x = largura - 90
        if x <= 10:
            x = 10

        if key[K_a] and key_b[K_LEFT]:
            if x_fundo >= -3:
                x_fundo = -3
            else:
                x_fundo += 10
        elif key[K_d] and key_b[K_RIGHT]:
            if x_fundo <= -157:
                x_fundo = x_fundo
            else:
                x_fundo -= 10
    colisao_p2 = pygame.draw.rect(tela, (255, 255, 0, 0), (xb + 20, yb + 75, 157, 86)) #Retângulo de colisão p2
    colisao_p1 = pygame.draw.rect(tela, (255, 255, 0, 0), (x - 15, y, 92, 86)) #Retângulo de colisão p1
    colisao_p_p2 = pygame.draw.rect(tela, (255, 255, 0, 0), (xb + 90, yb + 65, 85, 86)) #Retângulo de colisão pessoal p2
    tela.blit(fundo, (x_fundo, 0), (0, 0, 594, altura)) #Fundo
    tela.blit(pikachu, (x, y), (x_pikachu * 107, y_pikachu, 100, 86)) #P1
    tela.blit(bul, (xb, yb), (x_bul * 176, y_bul, 169, 200)) #P2
    pygame.draw.rect(tela, (255, 255, 255), (29, 19, 375, 22)) #Borda da barra:
    pygame.draw.rect(tela, (255, 0, 0), (30, 20, 373, 20)) #Barra de sangue (vermelho)
    pygame.draw.rect(tela, (238, 255, 0), (ajustador, 20, vida_1, 20)) #Barra de vida do p1
    pygame.draw.rect(tela, (238, 255, 0), (217, 20, vida_2, 20)) #Barra de vida do p2
    pygame.draw.rect(tela, (255, 255, 255), (216, 19, 1, 22)) #Divisão dos sangues
    pygame.draw.rect(tela, (255, 0, 255), (216, 19, 1, 22)) #Retêngulo de colisão p2
    tela.blit(texto_KO_luz, (200, 6)) #Sombra do texto principal:
    tela.blit(texto_KO, (198, 4)) #Texto principal (KO)
    tela.blit(texto_nome1, (40, 40)) #Nome do p1
    tela.blit(texto_nome2, (299, 40)) #Nome do p2
    x_bul += 1
    x_pikachu += 1

    pika_ale = randrange(0, 350)
    if pika_ale == 2:
        pika_sound.play()
    bulb_ale = randrange(0, 350)
    if bulb_ale == 2:
        bulb_sound.play()

    if cont_mov_bul == 1:
        x_bul +=1
# Golpe do P2:
    if x_bul >= 16 and y_bul == 635 or x_bul >= 16 and y_bul == 320:
        y_bul = 0
        if colisao_p2.colliderect(colisao_p1):
            vida_1 = vida_1 - 10
            ajustador = ajustador + 10
        cont_mov_bul = 0
    elif x_bul >= 16 and y_bul == 790 or x_bul >= 16 and y_bul == 476:
        y_bul = 160
        if colisao_p2.colliderect(colisao_p1):
            vida_1 = vida_1 - 10
            ajustador = ajustador + 10
        cont_mov_bul = 0
# Ataque do P1:
    if cont_mov_pik == 1:
        if x_pikachu >= 4 and y_pikachu == 330:
            y_pikachu = 0
            cont_mov_pik = 0
            if colisao_p1.colliderect(colisao_p2):
                vida_2 = vida_2 - 10
        elif x_pikachu >= 4 and y_pikachu == 410:
            y_pikachu = 85
            cont_mov_pik = 0
            if colisao_p1.colliderect(colisao_p2):
                vida_2 = vida_2 - 10
    if xb >= 266:
        xb = 266
    if x_fundo <= -157:
        x_fundo = -157
    if x_fundo >= -3:
        x_fundo = -3
    if xb <= -98:
        xb = -98
    pygame.display.flip()
