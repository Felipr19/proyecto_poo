from os import walk
import pygame
from config import *

def import_folder(path):

    surface_list = []

    for _,__,img_files in walk(path):
        for img in img_files:
            full_path = f"{path}\{img}"
            imagen = pygame.image.load(full_path).convert_alpha()
            WIDTH = 406
            height = imagen.get_size()[1]
            NEW_WIDTH = 50
            new_height = (NEW_WIDTH*height)/WIDTH
            img_surface = pygame.transform.scale(imagen,(NEW_WIDTH,new_height))
            surface_list.append(img_surface)

    return surface_list
