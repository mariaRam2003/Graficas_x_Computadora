import pygame
from pygame.locals import *

from rt import Raytracer

from figures import *
from lights import *
from materials import Material, diffuse

width = 512
height = 512

pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

# Crear RayTracer
raytracer = Raytracer(screen)
raytracer.rtClearColor(0.25,0.25,0.25)

# Crear Material
brick = Material( diffuse(1, 0.4, 0.4) )

# Esfera
raytracer.scene.append( Sphere(position = (0,0,-5), radius = 1, material = brick))

# Luces en la escena
raytracer.lights.append( AmbientLight(intensity = 0.8))
raytracer.lights.append( DirectionalLight(direction = (0,-1,-1), intensity = 0.1))

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunnig = False

    raytracer.rtClear()
    
    raytracer.rtPoint(100,100)
    raytracer.rtPoint(200,200)
    raytracer.rtPoint(300,300)

    raytracer.rtRender()


    pygame.display.flip()

pygame.quit()