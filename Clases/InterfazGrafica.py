import pygame
from CaracterGrafico import *
from Jugador import *
from config import *
from Bloque import *

class InterfazGrafica:
    def __init__(self,mapa,surface):
        self.display_surface = surface
        self.setup_mapa(mapa)
        self.mapa_var = 0

    def setup_mapa(self,layout):                
        self.bloques = pygame.sprite.Group()
        self.jugador = pygame.sprite.GroupSingle()

        for fila_index,fila in enumerate(layout):
            for col_index,col in enumerate(fila):

                x = col_index * bloque_size
                y = fila_index * bloque_size

                if col == "X":
                    bloque = Bloque((x,y),bloque_size)
                    self.bloques.add(bloque)
                
                if col == "P":
                    jugador = Jugador((x,y),6,'P1','sprite',2)
                    self.jugador.add(jugador)


    def ejecutar(self):
        self.bloques.update(self.mapa_var)
        self.bloques.draw(self.display_surface)

        self.jugador.update()
        self.jugador.draw(self.display_surface)