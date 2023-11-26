from Caracter import *
from support import import_folder
from config import VELOCIDAD, VELOCIDAD_MAX
import pygame


class Jugador(Caracter):

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.orientacion_D = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.orientacion_D = False
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            if self.on_ground:
                self.jump()

        if keys[pygame.K_z]:
            self.run = True
            if self.velocidad < VELOCIDAD_MAX:
                self.velocidad += 0.08
                if self.velocidad > VELOCIDAD_MAX:
                    self.velocidad = VELOCIDAD_MAX
        else:
            self.run = False
            if self.velocidad > VELOCIDAD:
                self.velocidad -= 0.08
                if self.velocidad < VELOCIDAD:
                    self.velocidad = VELOCIDAD

    def import_assets(self):
        
        player_path = 'Assets\Player\\'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[],'walk':[]}

        for animation in self.animations.keys():
            full_path = player_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        
        animation = self.animations[self.status]

        #cambio de velocidad animacion
        if self.animation_speed <= 0.55 and self.velocidad > 8:
            self.animation_speed += 0.03
        elif self.animation_speed >= 0.1:
            self.animation_speed -= 0.03

        #loop del index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        frame = animation[int(self.frame_index)]

        if self.orientacion_D:
            self.image = frame
        else: 
            self.image = pygame.transform.flip(frame,True,False).convert_alpha()

        if self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)


    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 0.8:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                if self.run:
                    self.status = 'run'
                else:
                    self.status = 'walk'
            else: 
                self.status = 'idle'
        

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()


