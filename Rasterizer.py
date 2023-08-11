from gl import Renderer, V2, V3, color
import shaders

width = 580
height = 580 

rend = Renderer(width, height)

# Le damos los shaders que se utilizaran
rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.negativeFragmentShader

rend.glCameraMatrix(translate=(0,-0.5,0),
                   rotate=(0,0,0))

#rend.glLookAt(camPos=(0,0,0),
 #       eyePos=(0,0,0))

rend.glLoadModel(filename="men.obj", 
                 textureName="menTexture.bmp", 
                 translate=(width/4, height/5, 0), 
                 scale=(40,40,40), 
                 rotate=(0,-90,0))

rend.glRender()

rend.glFinish('output.bmp')