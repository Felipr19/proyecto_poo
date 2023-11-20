from abc import ABC
from Caracter import *

class Enemigos(ABC):
    def __init__(self, nombre, damage, velocidad):
        self.nombre = nombre
        self.damage = damage
        super().__init__(nombre, salud=damage * 10, velocidad=velocidad)


    def atacar(self):
        print(f"{self.nombre} ataca con {self.damage} de daño.")

    def recoger_atributos(self):
        return {
            "nombre": self.nombre,
            "salud": self.damage * 10,
        }
    