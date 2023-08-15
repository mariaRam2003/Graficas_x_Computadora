from gl import Renderer, V2, V3, color
import shaders

width = 580
height = 580 

shader_functions = [
    shaders.grayscaleInvertShader,
    shaders.pixelatedShader,
    shaders.negativeFragmentShader
]

for shader_func in shader_functions:
    rend = Renderer(width, height)
    
    rend.vertexShader = shaders.vertexShader
    rend.fragmentShader = shader_func
    
    rend.glCameraMatrix(translate=(0, -0.5, 0), rotate=(0, 0, 0))
    
    rend.glLoadModel(filename="men.obj", 
                     textureName="menTexture.bmp", 
                     translate=(width / 4, height / 5, 0), 
                     scale=(40, 40, 40), 
                     rotate=(0, -90, 0))
    
    rend.glRender()

    output_filename = f'output_{shader_func.__name__}.bmp'
    rend.glFinish(output_filename)