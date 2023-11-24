import pygame
from Jugador import *
from config import *
from Bloque import *

class InterfazGrafica:
    def __init__(self,mapa,surface):
        self.display_surface = surface
        self.setup_mapa(mapa)
        self.mapa_var = 0

    #seting del mapa --> crea bloques y jugador

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
                    jugador = Jugador((x,y),VELOCIDAD,'P1','sprite',2)
                    self.jugador.add(jugador)

    #despalazamiento de la camara 

    def camara_x(self):

        jugador = self.jugador.sprite
        jugador_x = jugador.rect.centerx
        direction_x = jugador.direction.x

        if jugador_x < W_WIDTH/4 and direction_x < 0:
            self.mapa_var = VELOCIDAD
            jugador.velocidad = 0
        elif jugador_x > W_WIDTH - W_WIDTH/4 and direction_x > 0:
            self.mapa_var = -VELOCIDAD
            jugador.velocidad = 0
        else:
            self.mapa_var = 0
            jugador.velocidad = VELOCIDAD

    def horizontal_collision(self):

        jugador = self.jugador.sprite
        jugador.rect.x += jugador.direction.x * jugador.velocidad

        for sprite in self.bloques.sprites():
            if sprite.rect.colliderect(jugador.rect):
                if jugador.direction.x > 0:
                    jugador.rect.right = sprite.rect.left
                elif jugador.direction.x < 0:
                    jugador.rect.left = sprite.rect.right

    def vertical_collision(self):
        
        jugador = self.jugador.sprite
        jugador.aplly_gravedad()

        for sprite in self.bloques.sprites():
                if sprite.rect.colliderect(jugador.rect):
                    if jugador.direction.y > 0:
                        jugador.rect.bottom = sprite.rect.top
                    elif jugador.direction.y < 0:
                        jugador.rect.top = sprite.rect.bottom
                        jugador.direction.y = 0



    def ejecutar(self):

        self.bloques.update(self.mapa_var)
        self.camara_x()
        self.bloques.draw(self.display_surface)

        font = pygame.font.Font(None, 36)
        text = font.render(f"Valor de x: {self.jugador.sprite.gravedad   }", True, 'white')
        self.display_surface.blit(text, (10, 10))


        self.jugador.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.jugador.draw(self.display_surface)
