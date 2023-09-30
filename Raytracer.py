import pygame
from pygame.locals import *

from rt import Raytracer

from figures import *
from lights import Ambient 
from lights import Directional
from lights import Point
import materials as Material

width = 720
height = 720

pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

# Crear RayTracer
raytracer = Raytracer(screen)
raytracer.environmentMap = pygame.image.load("textures/background.bmp")
raytracer.rtClearColor(0.5, 0.5, 0.5)
raytracer.rtColor(1, 1, 1)

# Crear 2 pelotas transparentes
raytracer.scene.append(
    Sphere(position=(-1, -0.5, -3), radius=0.4, material=Material.glass())
)
raytracer.scene.append(
    Sphere(position=(-1, 1, -3), radius=0.4, material=Material.diamond())
)

# Crear 2 pelotas reflectivas
raytracer.scene.append(
    Sphere(position=(0, -0.5, -3), radius=0.4, material=Material.metal())
)
raytracer.scene.append(
    Sphere(position=(0, 1, -3), radius=0.4, material=Material.blueMetal())
)

# Crear 2 pelotas opacas
raytracer.scene.append(
    Sphere(position=(1, -0.5, -3), radius=0.4, material=Material.earth())
)
raytracer.scene.append(
    Sphere(position=(1, 1, -3), radius=0.4, material=Material.balloon())
)

# Luces en la escena
raytracer.lights.append(
    Ambient(intensity=0.5)
)
raytracer.lights.append(
    Directional(direction=(-1, -1, -1), intensity=0.3)
)
raytracer.lights.append(
    Point(position=(2.5, 0, -5), intensity=1)
)

isRunning = True
raytracer.rtClear()
raytracer.rtRender()

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

rect = pygame.Rect(0, 0, width, height)
sub = screen.subsurface(rect)

pygame.quit()