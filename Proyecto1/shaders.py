import mathLib as ml
import math

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]
    vt = [vertex[0],
          vertex[1],
          vertex[2],
          1]
    mats= ml.normalMatMult([vpMatrix, projectionMatrix, viewMatrix, modelMatrix])
    vt = ml.matVectMult(mats,vt)
    vt = [vt[0]/vt[3], 
          vt[1]/vt[3], 
          vt[2]/vt[3]]
    return vt

def fragmentShader(**kwargs):
      texCoords = kwargs["texCoords"]
      texture = kwargs["texture"]
      if texture != None:
            color = texture.getColor(texCoords[0], texCoords[1])
      else:
            color = (1,1,1)
      return color

def flatShader(**kwargs):
      texCoords = kwargs["texCoords"]
      texture = kwargs["texture"]
      dlight = kwargs["dLight"]
      normal = kwargs["triangleNormal"]

      b=1.0
      g=1.0
      r=1.0

      if texture != None:
            textureColor = texture.getColor(texCoords[0], texCoords[1])
            b *= textureColor[2]
            g *= textureColor[1]
            r *= textureColor[0]

      intensity = ml.producto_punto(normal, ml.negative_tuple(dlight))

      b *= intensity
      g *= intensity
      r *= intensity
      if intensity > 0:
            return r,g,b
      else:
            return [0,0,0]
      
def gouradShader(**kwargs):
    texture= kwargs["texture"]
    tA, tB, tC= kwargs["texCoords"]
    nA, nB, nC= kwargs["normals"]
    dLight = kwargs["dLight"]
    u, v, w= kwargs["bCoords"]
    modelMatrix = kwargs["modelMatrix"]

    b= 1.0
    g= 1.0
    r= 1.0

    if texture != None:
        tU= u * tA[0] + v * tB[0] + w * tC[0]
        tV= u * tA[1] + v * tB[1] + w * tC[1]
        
        textureColor = texture.getColor(tU, tV)    
        b *= textureColor[2]
        g *= textureColor[1]
        r *= textureColor[0]

    normal= [u * nA[0] + v * nB[0] + w * nC[0],
             u * nA[1] + v * nB[1] + w * nC[1],
             u * nA[2] + v * nB[2] + w * nC[2],
             0]
    
    normal = ml.matVectMult(modelMatrix, normal)
    normal = ml.norm_vector((normal[0], normal[1], normal[2]))
    
    intensity = ml.producto_punto(normal, ml.negative_tuple(dLight))
    
    b *= intensity
    g *= intensity
    r *= intensity

    b = min(b, 1.0)
    g = min(g, 1.0)
    r = min(r, 1.0)

    if intensity > 0:
        return r, g, b

    else:
        return [0,0,0]
    

def caricatureCelShader(**kwargs):
    intensity = 0.8
    edgeSens = 0.5
    
    r, g, b = gouradShader(**kwargs)
    
    gintensity = 0.2989 * r + 0.5870 * g + 0.1140 * b
    
    if gintensity > edgeSens:
        return [0, 0, 0]  # Bordes más oscuros
    if gintensity > intensity:
        return r, g, b
    else:
        return [0, 0, 0]

    
def negativeShader(**kwargs):
    r, g, b = gouradShader(**kwargs)  
    
    invR = 1.0 - r
    invG = 1.0 - g
    invB = 1.0 - b
    
    return invR, invG, invB

def noiseShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    u, v, w = kwargs["bCoords"]
    
    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        
        noiseIntensity = 0.05
        
        weight = 0.0
        color = [0.0, 0.0, 0.0]
        
        for offsetY in range(-1, 2):
            for offsetX in range(-1, 2):
                offsetTexX = tU + offsetX * noiseIntensity
                offsetTexY = tV + offsetY * noiseIntensity
                
                baseColor = texture.getColor(offsetTexX, offsetTexY)
                baseWeight = 1.0 
                
                weight += baseWeight
                if baseColor is None:
                  baseColor = [0.0, 0.0, 0.0]   

                color[0] += baseColor[0] * baseWeight
                color[1] += baseColor[1] * baseWeight
                color[2] += baseColor[2] * baseWeight
        
        color[0] /= weight
        color[1] /= weight
        color[2] /= weight
        
        return color
    else:
        return [0.0, 0.0, 0.0] 


#chatGPT help:
# fix this pixelShader:
# def pixelShader(**kwargs):
#     texture = kwargs["texture"]
#     texCoords = kwargs["texCoords"]

#     if texture is not None:
#         tU, tV = texCoords[0]

#         pixel_size = 10  

#         block_x = int(tU * texture.width / pixel_size) * pixel_size
#         block_y = int(tV * texture.height / pixel_size) * pixel_size

#         color = texture.getColor(block_x / texture.width, block_y / texture.height)
#     else:
#         color = (1, 1, 1)

#     return color


def pixelShader(**kwargs):
    texture = kwargs["texture"]
    tA, tB, tC = kwargs["texCoords"]
    u, v, w = kwargs["bCoords"]
    
    if texture is not None:
        tU = u * tA[0] + v * tB[0] + w * tC[0]
        tV = u * tA[1] + v * tB[1] + w * tC[1]
        
        factor=300  
        
        pixelSizeX= 1.0 / factor
        pixelSizeY= 1.0 / factor
        
        blockX = int(tU/pixelSizeX)*pixelSizeX
        blockY = int(tV/pixelSizeY)*pixelSizeY
        
        color = texture.getColor(blockX, blockY)
        
        return color
    else:
        return [0,0,0] 
    


def negativeShader(**kwargs):
    r, g, b = gouradShader(**kwargs)
    invR = 1.0 - r
    invG = 1.0 - g
    invB = 1.0 - b
    return invR, invG, invB

def grayscaleShader(**kwargs):
    r, g, b = gouradShader(**kwargs)
    intensity = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return intensity, intensity, intensity

def toonShader(**kwargs):
    intensity = 5.0
    edgeSens = 0.5
    
    r, g, b = gouradShader(**kwargs)
    
    gintensity = 0.2989 * r + 0.5870 * g + 0.1140 * b
    
    if gintensity > edgeSens:
        return [0, 0, 0]  # Bordes más oscuros
    if gintensity > intensity:
        return [round(r * 2) / 2, round(g * 2) / 2, round(b * 2) / 2]  # Tonos discretos
    else:
        return [0, 0, 0]

def cartoonShaderWithBlackEdge(**kwargs):
    intensity = 0.8
    edgeSens = 0.5
    
    r, g, b = gouradShader(**kwargs)
    
    gintensity = 0.2989 * r + 0.5870 * g + 0.1140 * b
    
    if gintensity > edgeSens:
        return [0, 0, 0]  # Bordes más oscuros
    if gintensity > intensity:
        return r, g, b
    else:
        return [0, 0, 0]