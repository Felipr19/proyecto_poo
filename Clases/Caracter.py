import pygame


class Caracter(pygame.sprite.Sprite):
    def __init__(self,pos,velocidad,nombre,sprite,salud):
        super().__init__()
        self.nombre = nombre
        self.sprite = sprite
        self.salud = salud
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.velocidad = velocidad
        self.direction = pygame.math.Vector2(0,0)

    def mostrar_estado(self):
        print(f"{self.nombre}: Salud={self.salud}, Velocidad={self.velocidad}")

    def update(self):
        self.rect.x += self.direction.x * self.velocidad