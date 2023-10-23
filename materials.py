import pygame

OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2

class Material:
    def __init__(self, diffuse=(1, 1, 1), spec=1.0, ks=0.0, ior=1.0, type=OPAQUE, texture=None):
        self.diffuse = diffuse
        self.spec = spec
        self.ks = ks
        self.ior = ior
        self.type = type
        self.texture = texture


def glass():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=64, ks=0.15, ior=1.5, type=TRANSPARENT)

def diamond():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=128, ks=0.2, ior=2.417, type=TRANSPARENT)

def metal():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=64, ks=0.2, type=REFLECTIVE)

def blueMetal():
    return Material(diffuse=(0.2, 0.2, 0.8), spec=32, ks=0.15, type=REFLECTIVE)

def balloon():
    return Material(diffuse=(1, 0, 0), spec=32, ks=0.0, ior=1.0, type=OPAQUE)

def brick():
    return Material(diffuse=(1, 0.3, 0.2), spec=8, ks=0.01)


def grass():
    return Material(diffuse=(0.2, 0.8, 0.2), spec=32, ks=0.1)


def water():
    return Material(diffuse=(0.2, 0.2, 0.8), spec=256, ks=0.5)

def diffuse(r, g, b):
    return (r, g, b)

def nieve():
    return Material(diffuse=(1, 1, 1), spec=0.5, ks=0.2)

def duro():
    return Material(diffuse=(0.3, 0.3, 0.3), spec=0.2, ks=0.1)

def zanahoria():
    return Material(diffuse=(1, 0.5, 0), spec=0.4, ks=0.3)

def ceiling():
    return Material(diffuse=(0.8, 0.8, 0.8), spec=32, ks=0.5)


def floor():
    return Material(diffuse=(0.5, 0.5, 0.5), spec=32, ks=0.5, type=REFLECTIVE)


def wall():
    return Material(diffuse=(0.7, 0.7, 0.7), spec=32, ks=0.5)


def cube():
    return Material(diffuse=(1, 0, 0), spec=64, ks=0.15, type=OPAQUE)

def green():
    return Material(texture=pygame.image.load("textures/green.jpg"), type=OPAQUE)

def pumpkin():
    return Material(texture=pygame.image.load("textures/pumpkin.png"), type=OPAQUE)

def adorno():
    return Material(diffuse=(0.5, 0.1, 0.5), spec=64, ks=0.2, ior=2, type=REFLECTIVE)

def spiderweb():
    return Material(texture=pygame.image.load("textures/spiderweb2.jpeg"), type=OPAQUE)     

def frankeistein():
    return Material(texture=pygame.image.load("textures/frankeistein.jpg"), type=REFLECTIVE)     

def bone():
    return Material(texture=pygame.image.load("textures/Jack.jpg"), type=OPAQUE )    

def skull():
    return Material(texture=pygame.image.load("textures/skull.png"), type=OPAQUE)

def blood():
    return Material(diffuse=(0.8, 0.1, 0.1), spec=128, ks=0.8, ior=1.33, type=REFLECTIVE)      
