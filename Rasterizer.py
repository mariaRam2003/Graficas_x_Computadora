from gl import Renderer, V2, V3, color
import shaders

width = 580
height = 580 

rend = Renderer(width, height)

rend.vertexShader=shaders.vertexShader
rend.fragmentShader=shaders.fragmentShader

#rend.glCameraMatrix(translate=(0,0,0),
#                   rotate=(0,0,0))

## Medium Shot
rend.glLookAt(camPos=(0,0,3),
         eyePos=(0,0,0))



rend.glLoadModel(filename="Silla.obj", 
                 textureName="texturaSilla.bmp", 
                 translate=(width/3.6, height/6, 0), 
                 scale=(450,450,450), 
                 rotate=(0,180,0))

rend.glRender()

rend.glFinish('MediumShot.bmp')

## Low angle shot
rend.glLookAt(camPos=(0, 1, 3),
             eyePos=(0, -2, -3))

rend.glClear()  # Clear the previous render

rend.glRender()
rend.glFinish('LowAngleShot.bmp')

## High angle shot
rend.glLookAt(camPos=(0, 3, 1),
            eyePos=(0, 0, 0))

rend.glClear()  # Clear the previous render

rend.glRender()
rend.glFinish('HighAngleShot.bmp')

## Dutch angle shot

rend.glLookAt(camPos=(5, 1, 3), eyePos=(0, 0, 0))

rend.glClear()  # Clear the previous render

rend.glRender()
rend.glFinish('DutchAngleShot.bmp')