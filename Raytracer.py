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
#raytracer.environmentMap = pygame.image.load("textures/desert.bmp")
raytracer.rtClearColor(0.5, 0.5, 0.5)
raytracer.rtColor(1, 1, 1)

# Crear disk
raytracer.scene.append(
    Disk(position=(-2, 0, -5), normal=(1, 0, 0.2), radius=1, material=Material.blueMetal())
)

# Crear cubos
raytracer.scene.append(
    AABB(position=(-1, 0, -6), size=(1, 1, 1), material=Material.cube())
)
raytracer.scene.append(
    AABB(position=(1, 0, -6), size=(1, 1, 1), material=Material.brick())
)

# Crear planos
raytracer.scene.append(
    Plane(position=(0, -1.5, 0), normal=(0, 1, 0), material=Material.floor())
)
raytracer.scene.append(
    Plane(position=(0, 3, 0), normal=(0, -1, 0), material=Material.ceiling())
)
raytracer.scene.append(
    Plane(position=(0, 0, -12), normal=(0, 0, -1), material=Material.wall())
)
raytracer.scene.append(
    Plane(position=(0, 0, 6), normal=(0, 0, 1), material=Material.wall())
)
raytracer.scene.append(
    Plane(position=(-3, 0, 0), normal=(1, 0, 0), material=Material.wall())
)
raytracer.scene.append(
    Plane(position=(3, 0, 0), normal=(-1, 0, 0), material=Material.wall())
)

# Luces en la escena
raytracer.lights.append(
    Ambient(intensity=0.5)
)
# raytracer.lights.append(
#     Directional(direction=(-1, -1, -1), intensity=0.3)
# )
raytracer.lights.append(
    Point(position=(2.5, 0, -5), intensity=1)
)

isRunning = True
raytracer.rtClear()
raytracer.rtRender()

# while isRunning:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             isRunning = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 isRunning = False

rect = pygame.Rect(0, 0, width, height)
sub = screen.subsurface(rect)

pygame.quit()