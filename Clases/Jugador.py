from Caracter import *
from support import import_folder
import pygame


class Jugador(Caracter):

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.jump()

    def import_assets(self):
        
        player_path = 'Assets\Player\\'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[]}

        for animation in self.animations.keys():
            full_path = player_path + animation
            self.animations[animation] = import_folder(full_path)

    def update(self):
        self.get_input()


