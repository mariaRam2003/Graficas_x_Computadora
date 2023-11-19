import pygame
import glm
import math
from pygame.locals import *

from gl import Renderer
from model import Model
from shaders import *
from obj import Obj

# Musica
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("objects/audio/song.mp3")

pygame.mixer.music.play(-1)

width = 960
height = 540

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

renderer = Renderer(screen)
actual_Vertex_shader = vertex_shader
actual_Fragment_shader = fragment_shader
renderer.setShader(actual_Vertex_shader, actual_Fragment_shader)
is_dragging = False
old_position = None
auto_rotate = True

comand_list = '''LISTA DE QUE PUEDES HACER

MODELOS:
Right Arrow = Siguiente Modelo
Left Arrow = Anterior Modelo

ZOOM:
+ Key = Aumentar Zoom
- Key = Disminuir Zoom

ROTACION:
Mouse drag = Rotar el modelo
w = Rotar hacia arriba
s = Rotar hacia abajo
a = Rotar hacia la izquierda
d = Rotar hacia la derecha

SHADERS:
r = Reset Shaders
1 = Gourad Fragment Shader
2 = Multicolor Fragment Shader
3 = Noise Fragment Shader
4 = Cool Fragment Shader
'''
print(comand_list)

modelIndex = 0 
models = []

def modelsChange(direction):
    global modelIndex
    global models
    if direction == "R":
        if modelIndex == len(models) - 1:
            modelIndex = 0
        else:
            modelIndex += 1
    else:
        if modelIndex == 0:
            modelIndex = len(models) - 1
        else:
            modelIndex -= 1

    renderer.scene.clear()
    renderer.scene.append(models[modelIndex]['model'])
    renderer.lightIntensity = models[modelIndex]['lightIntensity']
    renderer.target = models[modelIndex]['lookAt']
    renderer.cameraPosition = glm.vec3(0.0, 0.0, 0.0)
    renderer.dirLight = models[modelIndex]['dirLight']

# Lista de objetos a renderizar

# Estatua
obj = Obj("objects/Estatua.obj").parse_data()
model = Model(obj)
model.loadTexture("objects/textures/texture.bmp")
model.loadNoiseTexture("objects/textures/metal.jpg")
model.position.z = -15
model.position.y = -2
model.rotation.x = 0
model.scale = glm.vec3(0.05, 0.05, 0.05)
modelData = {"model": model, 
             "lightIntensity": 5.0, 
             "lookAt": glm.vec3(model.position.x, model.position.y + 2 , model.position.z),
             "dirLight": glm.vec3(0, 0, -1)}
models.append(modelData)

# Rocket
obj = Obj("objects/rocket.obj").parse_data()
model = Model(obj)
model.loadTexture("objects/textures/texture.bmp")
model.loadNoiseTexture("objects/textures/metal.jpg")
model.position.z = -15
model.position.y = -2
model.rotation.x = 0
model.scale = glm.vec3(1, 1, 1)
modelData = {"model": model,
             "lightIntensity": 5.0,
             "lookAt": glm.vec3(model.position.x, model.position.y + 2 , model.position.z),
             "dirLight": glm.vec3(0, 0, -1)}
models.append(modelData)

# Pumpkin
obj = Obj("objects/pumpkin.obj").parse_data()
model = Model(obj)
model.loadTexture("objects/textures/texture.bmp")
model.loadNoiseTexture("objects/textures/metal.jpg")
model.position.z = -15
model.position.y = -2
model.rotation.x = 0
model.scale = glm.vec3(8, 8, 8)
modelData = {"model": model,
             "lightIntensity": 5.0,
             "lookAt": glm.vec3(model.position.x, model.position.y + 2 , model.position.z),
             "dirLight": glm.vec3(0, 0, -1)}
models.append(modelData)

# Porsche
obj = Obj("objects/porsche.obj").parse_data()
model = Model(obj)
model.loadTexture("objects/textures/texture.bmp")
model.loadNoiseTexture("objects/textures/metal.jpg")
model.position.z = -15
model.position.y = -2
model.rotation.x = 0
model.scale = glm.vec3(0.05, 0.05, 0.05)
modelData = {"model": model,
             "lightIntensity": 5.0,
             "lookAt": glm.vec3(model.position.x, model.position.y + 2 , model.position.z),
             "dirLight": glm.vec3(0, 0, -1)}
models.append(modelData)

renderer.scene.append(models[modelIndex]['model'])
renderer.lightIntensity = models[modelIndex]['lightIntensity']
renderer.target = models[modelIndex]['lookAt']
renderer.dirLight = models[modelIndex]['dirLight']


isRunning = True
movement_sensitive = 0.1
sens_x = 1
sens_y = 0.1
distance = abs(renderer.cameraPosition.z- models[modelIndex]['model'].position.z)
radius = distance
zoom_sensitive = 0.5
angle = 0.0

# Limitations
camera_rotation_speed = 50.0
camera_vertical_limit = (-40, 80)
camera_zoom_limit = (0.5, 2.0)

camera = models[modelIndex]['model']

while isRunning:
    deltaTime = clock.tick(60) / 1000.0
    renderer.elapsedTime += deltaTime
    keys = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            if event.key == pygame.K_c:
                print(comand_list)
            if event.key == pygame.K_r:
                actual_Fragment_shader = fragment_shader
                actual_Vertex_shader = vertex_shader
            if event.key == pygame.K_1:
                actual_Fragment_shader = gourad_fragment_shader
            if event.key == pygame.K_2:
                actual_Fragment_shader = multicolor_fragment_shader
            if event.key == pygame.K_3:
                actual_Fragment_shader = noise_fragment_shader
            if event.key == pygame.K_4:
                actual_Fragment_shader = metal_fragment_shader
            if event.key == pygame.K_RIGHT:
                modelsChange("R")
                angle = 0.0
                radius = distance
            if event.key == pygame.K_LEFT:
                modelsChange("L")
                angle = 0.0
                radius = distance

            renderer.setShader(actual_Vertex_shader, actual_Fragment_shader)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                is_dragging = True
                old_position = pygame.mouse.get_pos()

            elif event.button == 4:
                if radius > distance * 0.5:
                    radius -= zoom_sensitive             

            elif event.button == 5:
                if radius < distance * 1.5:
                    radius += zoom_sensitive

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  
                is_dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if is_dragging:
                new_position = pygame.mouse.get_pos()
                deltax = new_position[0] - old_position[0]
                deltay = new_position[1] - old_position[1]
                angle += deltax * -sens_x

                if angle > 360:
                    angle = 0

                if distance > renderer.cameraPosition.y + deltay * -sens_y and distance * -1.5 < renderer.cameraPosition.y + deltay * -sens_y:
                    renderer.cameraPosition.y += deltay * -sens_y

                old_position = new_position
            
            # Obtener la rotación actual del modelo
        rotation = models[modelIndex]['model'].rotation

        # Actualizar la rotación del modelo según las teclas presionadas
        if keys[pygame.K_a]:
            rotation.y -= camera_rotation_speed * deltaTime
        if keys[pygame.K_d]:
            rotation.y += camera_rotation_speed * deltaTime
        if keys[pygame.K_w]:
            rotation.x += camera_rotation_speed * deltaTime
        if keys[pygame.K_s]:
            rotation.x -= camera_rotation_speed * deltaTime

        # Limitar la rotación vertical del modelo
        rotation.x = max(camera_vertical_limit[0], min(camera_vertical_limit[1], rotation.x))

        # Aplicar la rotación al modelo
        models[modelIndex]['model'].rotation = rotation

        # Obtener el modelo actual
        model = models[modelIndex]['model']

        # Actualizar el zoom del modelo según las teclas presionadas
        if keys[K_p] or keys[K_KP_PLUS]:
            model.scale *= 1.01  # Aumenta el zoom en un 1%
        if keys[K_MINUS] or keys[K_KP_MINUS]:
            model.scale /= 1.01  # Reduce el zoom en un 1%

    renderer.updateViewMatrix()
    renderer.render()
    pygame.display.flip()

pygame.quit()
