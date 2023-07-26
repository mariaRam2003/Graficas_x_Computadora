from gl import Renderer,  V3, color
from math import pi
import shaders
import random

width = 1024
height = 512

rend = Renderer(width, height)

rend.vertexShader = shaders.vertexShader # type: ignore
rend.fragmentShader = shaders.fragmentShader # type: ignore

rend.glRender()

rend.glFinish('Model.bmp')