import pygame
from pygame.locals import *
from sys import exit
from random import randint
import math



pygame.init() 

x = 800
y = 650
janela = pygame.display.set_mode((x,y))
pygame.display.set_caption('Jogo de Luta')
musica_de_fundo = pygame.mixer.music.load('sunrise-sound-effect-free-download.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

barulho_colisao = pygame.mixer.Sound('smw_bubble_pop.wav')

fundo = pygame.image.load('fundo.jpg')
fundo = pygame.transform.scale(fundo,(x,y))

leo = pygame.image.load('leo-removebg-preview.png')
leo = pygame.transform.scale(leo,(210,210))

leo_attack = pygame.image.load('leo2-removebg-preview.png')
leo_attack = pygame.transform.scale(leo_attack,(210,210))
leo_hit = pygame.image.load('leo3-removebg-preview.png')
leo_hit = pygame.transform.scale(leo_hit,(210,210))

xl, yl = [y/2, y/2]
def posicao_leo(n,id):
    global xl,yl  

    if id == 'd':
        if xl+210 > x:
            xl += -5
        elif xl < 0:
            xl += 5
        else: 
            xl += n
    elif id == 's':
        if yl < 0:
            yl += 5
        elif yl+210> y:
            yl -= 5
        else:
            yl += n
    

miya = pygame.image.load('miya-removebg-preview.png')
miya = pygame.transform.scale(miya, (210,210))
miya_attack = pygame.image.load('miya2-removebg-preview.png')
miya_attack = pygame.transform.scale(miya_attack, (210,210))
miya_hit = pygame.image.load('miya3-removebg-preview.png')
miya_hit = pygame.transform.scale(miya_hit, (210,210))


xm,ym = [y/2 + 100, y/2 + 100]
def posicao_miya(n,id):
    global xm,ym  


    if id == 'h':
        while n > 0:
            ym += 10
            xm += 10
            n -= 1
    elif id == 'd':
        if xm+210 > x:
            xm += -5
        elif xm < 0:
            xm += 5
        else: 
            xm += n
    elif id == 's':
        if ym < 0:
            ym += 5
        elif ym+210> y:
            ym -= 5
        else:
            ym += n


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    left, middle, right = pygame.mouse.get_pressed()

    al = pygame.Rect((xl+100,yl+100),(200,210)) 
    bm = pygame.Rect((xm+100,ym+100),(200,210))
    
    janela.blit(fundo,(0,0))
    
    if pygame.key.get_pressed()[K_a]:
        posicao_leo(-5,'d')
    if pygame.key.get_pressed()[K_d]:
        posicao_leo(5,'d') 
    if pygame.key.get_pressed()[K_w]:
        posicao_leo(-5,'s')
    if pygame.key.get_pressed()[K_s]:
        posicao_leo(5,'s')

    if left:
        janela.blit(leo_attack,(xl,yl))
        a = pygame.Rect((xl+210,yl+210), (50, 50))
        if a.colliderect(bm):
            janela.blit(miya_hit,(xm,ym))
            posicao_leo(abs(xm-xl)**2,'h')
            barulho_colisao.play()

    else:
        janela.blit(leo,(xl,yl))

    if pygame.key.get_pressed()[K_j]:
        posicao_miya(-5,'d')
    if pygame.key.get_pressed()[K_l]:
        posicao_miya(5,'d') 
    if pygame.key.get_pressed()[K_i]:
        posicao_miya(-5,'s')
    if pygame.key.get_pressed()[K_k]:
        posicao_miya(5,'s')

    if pygame.key.get_pressed()[K_h]:
        janela.blit(miya_attack,(xm,ym))
        b = pygame.Rect((xm+130,ym), (50, 50))
        if b.colliderect(al):
            janela.blit(leo_hit,(xl,yl))
            posicao_leo(abs(xm-xl)**2,'h')
            barulho_colisao.play()
    else:
        janela.blit(miya,(xm,ym))

    pygame.display.update()