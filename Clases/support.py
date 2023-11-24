from os import walk
import pygame
from config import *

def import_folder(path):

    surface_list = []

    for _,__,img_files in walk(path):
        for img in img_files:
            full_path = f"{path}\{img}"
            imagen = pygame.image.load(full_path).convert_alpha()
            img_surface = pygame.transform.scale(imagen,(P_WIDTH,P_HEIGHT))
            surface_list.append(img_surface)

    return surface_list
