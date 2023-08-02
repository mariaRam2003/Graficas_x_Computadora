from gl import Renderer, V3, color
import random, shaders
width = 1024
height = 1024

rend = Renderer(width, height)

rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.fragmentShader

rend.glLoadModel( "model.obj", 
                  translate = (width/2, height/2, 0),
                  scale = (200, 200, 200))



rend.glRender()