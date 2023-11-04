import pygame
import glm
from pygame.locals import *

from gl import Renderer
from model import Model
from shaders import *
from obj import Obj


width = 960
height = 540

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

renderer = Renderer(screen)
actual_Vertex_shader = vertex_shader
actual_Fragment_shader = fragment_shader
renderer.setShader(actual_Vertex_shader, actual_Fragment_shader)

comand_list = '''c = Command List
r = Reset Shaders
1 = Gourad Fragment Shader
2 = Multicolor Fragment Shader
3 = Noise Fragment Shader
4 = Metal Fragment Shader
'''
print(comand_list)

#Model loading
obj = Obj("objects/Estatua/Estatua.obj")
objData = []
for face in obj.faces:
    if len(face) == 3:
        for vertexInfo in face:
            vertexId, texcoordId, normalId = vertexInfo
            vertex = obj.vertices[vertexId - 1]
            normals = obj.normals[normalId - 1]
            uv = obj.texcoords[texcoordId - 1]
            uv = [uv[0], uv[1]]
            objData.extend(vertex + uv + normals)
    elif len(face) == 4:
        for i in [0, 1, 2]:
            vertexInfo = face[i]
            vertexId, texcoordId, normalId = vertexInfo
            vertex = obj.vertices[vertexId - 1]
            normals = obj.normals[normalId - 1]
            uv = obj.texcoords[texcoordId - 1]
            uv = [uv[0], uv[1]]
            objData.extend(vertex + uv + normals)
        for i in [0, 2, 3]:
            vertexInfo = face[i]
            vertexId, texcoordId, normalId = vertexInfo
            vertex = obj.vertices[vertexId - 1]
            normals = obj.normals[normalId - 1]
            uv = obj.texcoords[texcoordId - 1]
            uv = [uv[0], uv[1]]
            objData.extend(vertex + uv + normals)


model = Model(objData)
model.loadTexture("objects/Estatua/texture.bmp")
model.loadNoiseTexture("objects/Estatua/metal.jpg")
model.position.z = -10
model.position.y = -2
model.rotation.x = -90
model.scale = glm.vec3(0.20, 0.20, 0.20)
renderer.scene.append(model)
renderer.lightIntensity = 5.0
renderer.dirLight = glm.vec3(0.0, 0.0, -1.0)

isRunning = True
while isRunning:
    deltaTime = clock.tick(60) / 1000.0
    renderer.elapsedTime += deltaTime
    keys = pygame.key.get_pressed()

    if keys[K_RIGHT]:
        renderer.clearColor[0] += deltaTime
    if keys[K_LEFT]:
        renderer.clearColor[0] -= deltaTime
    if keys[K_UP]:
        renderer.clearColor[1] += deltaTime
    if keys[K_DOWN]:
        renderer.clearColor[1] -= deltaTime
    if keys[K_SPACE]:
        renderer.clearColor[2] += deltaTime
    if keys[K_LSHIFT]:
        renderer.clearColor[2] -= deltaTime

    if keys[K_d]:
        model.rotation.y += deltaTime * 50
    if keys[K_a]:
        model.rotation.y -= deltaTime * 50
    if keys[K_w]:
        model.rotation.x += deltaTime * 50
    if keys[K_s]:
        model.rotation.x -= deltaTime * 50

    if keys[K_p] or keys[K_KP_PLUS]:
        model.zoom *= 1.01  # Aumenta el zoom en un 1%
    if keys[K_MINUS] or keys[K_KP_MINUS]:
        model.zoom /= 1.01  # Reduce el zoom en un 1%

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
            
            renderer.setShader(actual_Vertex_shader, actual_Fragment_shader)

    renderer.render()
    pygame.display.flip()

pygame.quit()
