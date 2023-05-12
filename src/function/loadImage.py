import pygame

def loadImage(path:str, size:tuple):
    return pygame.transform.scale(pygame.image.load(path), size)