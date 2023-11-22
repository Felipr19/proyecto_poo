import pygame

#Jugador y enemigos que interactuan en el juego

class Caracter(pygame.sprite.Sprite):
    def __init__(self,pos,velocidad,nombre,sprite,salud):
        super().__init__()
        self.nombre = nombre
        self.sprite = sprite
        self.salud = salud

        #parte grafica y hitbox
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        
        #moviemiento 
        self.velocidad = velocidad
        self.direction = pygame.math.Vector2(0.0,0.0)
        self.gravedad = 0
        self.vel_salto = -16

    def mostrar_estado(self):
        print(f"{self.nombre}: Salud={self.salud}, Velocidad={self.velocidad}")

    def aplly_gravedad(self):
        self.direction.y += self.gravedad
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.vel_salto
        
    def update(self):
        pass
       
