import pygame,sys
from config import *
from InterfazGrafica import *

#setup de pygame
pygame.init()
screen = pygame.display.set_mode((W_WIDTH,W_HEIGTH))
reloj = pygame.time.Clock()
mapa = InterfazGrafica(mapa,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    mapa.ejecutar()

    pygame.display.update()
    reloj.tick(60)