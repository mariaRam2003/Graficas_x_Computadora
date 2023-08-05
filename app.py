from gl import Renderer
from math import pi
import shaders
import random


width = 2024
height = 3000

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader # type: ignore
rend.fragmentShader = shaders.fragmentShader # type: ignore

rend.glLoadModel("Carro.obj", translate = (width/2, height/1.3, 0), scale = (50,50,50), rotate = (0, 90, 0))

rend.glLoadModel("Carro.obj", translate = (width/2, height/2, 0), scale = (50,50,50), rotate = (0, -90, 0))

rend.glLoadModel("Carro.obj", translate = (width/2, height/4, 0), scale = (50,50,50), rotate = (90, 90, 0))

rend.glRender()

rend.glFinish('Model.bmp')

