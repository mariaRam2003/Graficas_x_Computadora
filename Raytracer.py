import pygame
from pygame.locals import *

from rt import Raytracer

from figures import *
from lights import Ambient 
from lights import Directional
from lights import Point
import materials as Material

width = 512
height = 512

pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

# Crear RayTracer
raytracer = Raytracer(screen)
raytracer.rtClearColor(0.25,0.25,0.25)

# Crear bolitas del muñeco con material Nieve
raytracer.scene.append(
    Sphere(position=(0, -1.5, -5), radius=1, material=Material.nieve())
)
raytracer.scene.append(
    Sphere(position=(0, -0.3, -5), radius=0.8, material=Material.nieve())
)
raytracer.scene.append(
    Sphere(position=(0, 0.7, -5), radius=0.7, material=Material.nieve())
)

# Crear botones del muñeco con material duro
raytracer.scene.append(
    Sphere(position=(0, 0, -2), radius=0.04, material=Material.duro())
)
raytracer.scene.append(
    Sphere(position=(0, -0.7, -2), radius=0.04, material=Material.duro())
)
raytracer.scene.append(
    Sphere(position=(0, -0.35, -2), radius=0.04, material=Material.duro())
)

# Crear boca del muñeco con material duro
raytracer.scene.append(
    Sphere(position=(0.03, 0.15, -2), radius=0.02, material=Material.duro())
)
raytracer.scene.append(
    Sphere(position=(-0.03, 0.15, -2), radius=0.02, material=Material.duro())
)
raytracer.scene.append(
    Sphere(position=(0.08, 0.175, -2), radius=0.02, material=Material.duro())
)
raytracer.scene.append(
    Sphere(position=(-0.08, 0.175, -2), radius=0.02, material=Material.duro())
)

# Crear nariz del muñeco con material zanahoria
raytracer.scene.append(
    Sphere(position=(0, 0.33, -2), radius=0.08, material=Material.zanahoria())
)

# Crear ojos del muñeco con material duro
raytracer.scene.append(
    Sphere(position=(0.1, 0.4, -2), radius=0.04, material=Material.duro())
)
raytracer.scene.append(
    Sphere(position=(-0.1, 0.4, -2), radius=0.04, material=Material.duro())
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
                isRunnig = False

    pygame.display.flip()

pygame.quit()