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
raytracer.envMap = pygame.image.load("textures/Background.jpg")

raytracer.rtClearColor(0.5, 0.5, 0.5)
raytracer.rtColor(1, 1, 1)

# Pumpkin opaca1
raytracer.scene.append(
    Sphere(position=(-6, -3, -16), radius=1, material=Material.pumpkin())
)

# Pumpkin opaca2
raytracer.scene.append(
    Sphere(position=(-2, -3, -16), radius=1, material=Material.pumpkin())
)

# Pumpkin opaca3
raytracer.scene.append(
    Sphere(position=(2, -3, -16), radius=1, material=Material.pumpkin())
)

# Pumpkin opaca4
raytracer.scene.append(
    Sphere(position=(6, -3, -16), radius=1, material=Material.pumpkin())
)

# Spiderweb opaca
raytracer.scene.append(
    Pyramid(position=(-6, 1.6, -14), width=1.5, height=1.5, depth=1.5, rotation=(180,0,0), material=Material.spiderweb())
)

# # Frankeistein Reflectivo
# raytracer.scene.append(
#     AABB(position=(4, -1.5, -10), size=(2,2,2), material=Material.skull())
# )

# Adornito reflectivo 1
raytracer.scene.append(
    Entity(position=(-6, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(0,0,0), material=Material.adorno())
)
raytracer.scene.append(
    Entity(position=(-6, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(180,0,0), material=Material.adorno())
)

# Jack Skellington1
raytracer.scene.append(
    Entity(position=(-3, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(0,0,0), material=Material.bone())
)
raytracer.scene.append(
    Entity(position=(-3, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(180,0,0), material=Material.bone())
)
raytracer.scene.append(
    Sphere(position=(-3, 6, -15), radius=1, material=Material.skull())
)

# Adornito reflectivo 2
raytracer.scene.append(
    Entity(position=(0, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(0,0,0), material=Material.adorno())
)
raytracer.scene.append(
    Entity(position=(0, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(180,0,0), material=Material.adorno())
)

# Jack Skellington2
raytracer.scene.append(
    Entity(position=(3, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(0,0,0), material=Material.bone())
)
raytracer.scene.append(
    Entity(position=(3, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(180,0,0), material=Material.bone())
)
raytracer.scene.append(
    Sphere(position=(3, 6, -15), radius=1, material=Material.skull())
)

# Adornito reflectivo 3
raytracer.scene.append(
    Entity(position=(6, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(0,0,0), material=Material.adorno())
)
raytracer.scene.append(
    Entity(position=(6, 5, -15), width=1.4, height=1.4, depth=1.4, rotation=(180,0,0), material=Material.adorno())
)

# Blood
raytracer.scene.append(
    Disk(position=(-2, -6, -13), radius=2, normal=(0, 1, 0), material=Material.blood())
)

raytracer.scene.append(
    Disk(position=(-2.5, -6.5, -13), radius=1, normal=(0, 1, 0), material=Material.blood())
)
raytracer.scene.append(
    Disk(position=(-3, -6.5, -13), radius=1, normal=(0, 1, 0), material=Material.blood())
)
raytracer.scene.append(
    Disk(position=(0, -6.5, -13), radius=0.5, normal=(0, 1, 0), material=Material.blood())
)
raytracer.scene.append(
    Disk(position=(1, -6.5, -13), radius=0.5, normal=(0, 1, 0), material=Material.blood())
)
raytracer.scene.append(
    Disk(position=(0.5, -6.5, -15), radius=0.3, normal=(0, 1, 0), material=Material.blood())
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
pygame.image.save(sub, "result.png")

pygame.quit()
