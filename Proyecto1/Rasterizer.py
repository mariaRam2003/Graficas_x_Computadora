from gl import Renderer, V2,V3, color
import random, shaders
width = 800
height = 500

rend = Renderer(width, height)

rend.glBackgroundTexture('./fondo/texture.bmp')
rend.clearBackground()


rend.glClearColor(0.5,0.5,0.5)

rend.vertexShader=shaders.vertexShader

rend.glLookAt(camPos=(0,-1.5,-0.6),
             eyePos=(0,-2,-3))

#Walker
rend.fragmentShader=shaders.negativeShader  
rend.glDirectionalLight(2,0,-1)
rend.glLoadModel(filename="./objetos/Walker/object.obj", 
                 textureName="./objetos/Walker/texture.bmp", 
                 translate=(0.5, -2, -2), 
                 scale=(0.1,0.1,0.1), 
                 rotate=(0,90,0))
rend.glRender()

#DarthVader
rend.fragmentShader=shaders.grayscaleShader
rend.glDirectionalLight(-0.5,0,-0.5)
rend.glLoadModel(filename="./objetos/LordVaider/object.obj", 
                 textureName="./objetos/LordVaider/texture.bmp", 
                 translate=(-0.4, -3, -3), 
                 scale=(1,1,1), 
                 rotate=(0,0,0))
rend.glRender()

#Cajita de StarWars
rend.fragmentShader=shaders.grayscaleShader
rend.glDirectionalLight(0.5,0,-1)
rend.glLoadModel(filename="./objetos/Cajita/object.obj", 
                 textureName="./objetos/Cajita/texture.bmp", 
                 translate=(-2, -3, -3), 
                 scale=(0.4,0.4,0.4), 
                 rotate=(-5,0,0))
rend.glRender()

#LightSaber
rend.fragmentShader=shaders.pixelShader
rend.glDirectionalLight(-1,-0.6,0)
rend.glLoadModel(filename="./objetos/LightSaber/object.obj", 
                 textureName="./objetos/LightSaber/texture.bmp", 
                 translate=(-0.9, -1.9, -2.7), 
                 scale=(0.0015,0.0015,0.0015), 
                 rotate=(30,-30,0))
rend.glRender()

rend.glFinish("StarWarsLordVaiderScene.bmp")