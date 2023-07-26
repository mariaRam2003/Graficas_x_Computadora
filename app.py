from gl import Renderer,  V3, color
from math import pi
import shaders
import random


width = 2024
height = 2024

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader # type: ignore
rend.fragmentShader = shaders.fragmentShader # type: ignore

rend.glLoadModel("Carro.obj", translate = (width/2, height/6, 0), scale = (85,85,85), rotate = (-pi/2, pi, pi/2))

rend.glRender()

rend.glFinish('Model.bmp')