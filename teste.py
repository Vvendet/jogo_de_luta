import pygame 
from pygame.locals import *
from sys import exit

pygame.init()
tela = pygame.display.set_mode((640, 480))
musica = pygame.mixer.music.load('sunrise-sound-effect-free-download.mp3')
pygame.mixer.music.play(-1)

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
            