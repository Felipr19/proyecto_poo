import pygame

#Jugador y enemigos que interactuan en el juego

class Caracter(pygame.sprite.Sprite):
    def __init__(self,pos,velocidad,nombre,sprite,salud):
        super().__init__()
        self.nombre = nombre
        self.sprite = sprite
        self.salud = salud
        
        #player status
        self.status = 'idle'
        self.orientacion_D = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_rigth = False

        #moviemiento 
        self.velocidad = velocidad
        self.direction = pygame.math.Vector2(0,0)
        self.gravedad = 0.8
        self.vel_salto = -18

        #parte grafica y hitbox
        self.frame_index = 0
        self.animation_speed = 0.1
        self.import_assets()
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

    def import_assets(self):
        pass

    def animate(self):
        pass

    def aplly_gravedad(self):
        self.direction.y += self.gravedad
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.vel_salto

    def update(self):
        self.animate()
       