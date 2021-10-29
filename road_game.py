import pygame
from plyer import notification
from random import randint
import sys
import os
pygame.init()

def restart():
    ''' Reestarta o jogo. '''
    python = sys.executable
    os.execl(python, python, * sys.argv)

#configurações iniciais
x = 340 
y = 300
pos_x = 220
pos_y = 800
pos_outroy = 700
x_amarelo = 340
y_amarelo = 1200
velocidade = 10
velocidade_outros = 20
timer = 0
tempo_segundo = 0

#carregando as imagens e arrumando as escalas
fundo = pygame.image.load('tela.png')
fundo = pygame.transform.scale(fundo, (800, 600))
carro = pygame.image.load('carro.png')
carro = pygame.transform.scale(carro, (95, 95))
carro_amarelo = pygame.image.load('carro_amarelo.png')
carro_amarelo = pygame.transform.scale(carro_amarelo, (110, 95))
policia = pygame.image.load('policia.png')
policia = pygame.transform.scale(policia, (95, 95))
conversivel = pygame.image.load('conversivel.png')
conversivel = pygame.transform.scale(conversivel, (105, 95))

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Criando um jogo com Python')

font = pygame.font.SysFont('times new roman', 30)
texto = font.render('Tempo: ', True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

gameover = font.render("Perdeu! Aperte r para reiniciar", True, (255,255,255), (0,0,0))
pos_msg = gameover.get_rect()
pos_msg.center = janela.get_rect().center

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    #configurando os comandos do teclado
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_LEFT] and x >= 230:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 470:
        x += velocidade
    if comandos[pygame.K_r] and y == 4000:
        restart()

    #atualizando a posição dos demais carros, ou seja, quando eles saem da tela pela parte de cima (-200), 
    #retornam em alguma posição aleatoria pela parte de baixo, para promover a dinâmica do jogo
    if pos_y <= -200:
        pos_y = randint(1500, 2000)
    pos_y -= velocidade

    if pos_outroy <= -200:
        pos_outroy = randint(800, 1200)
    pos_outroy -= velocidade + 3

    if y_amarelo <= -200:
        y_amarelo = randint(800, 2000)
    y_amarelo -= velocidade

    #verificando colisoes
    if (x - 85) < pos_x and (y + 95) > pos_y and y < pos_y: #colisão com policia
        y = 4000 
        notification.notify(title='Muito ruim!', message='Você perdeu')

    if (x + 75) > (pos_x + 230) and (y + 105) > pos_outroy and y < pos_outroy: #colisão com conversivel
        y = 4000 
        notification.notify(title='Muito ruim!', message='Você perdeu')

    if (x - 85) < x_amarelo and x > x_amarelo and (y + 95) > y_amarelo and y < y_amarelo: #colisão carro amarelo
        y = 4000 
        notification.notify(title='Muito ruim!', message='Você perdeu')
    if (x + 95) > x_amarelo and x < (x_amarelo + 95) and (y + 95) > y_amarelo and y < y_amarelo: #colisão carro amarelo
        y = 4000 
        notification.notify(title='Muito ruim!', message='Você perdeu')

    #atualizando o cronometro
    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render('Tempo: '+str(tempo_segundo), True, (255,255,255), (0,0,0))
        timer = 0

    #atualizando a janela
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(policia,(pos_x, pos_y))
    janela.blit(conversivel,(pos_x + 230, pos_outroy))
    janela.blit(carro_amarelo,(x_amarelo,  y_amarelo))
    janela.blit(texto, pos_texto)
    if y == 4000:
        janela.blit(gameover, pos_msg)
    pygame.display.update()

pygame.quit()
