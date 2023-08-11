from mathLib import matMatMult
import numpy as np


def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["viewMatrix"]

    # Convertir el vértice a una matriz columna 4x1 agregando un valor de 1
    vt = [[vertex[0]], [vertex[1]], [vertex[2]], [1]]
    # Realizar la multiplicación de la matriz del modelo con el vértice
    vt = matMatMult(vpMatrix, matMatMult(projectionMatrix, matMatMult(viewMatrix, matMatMult(modelMatrix, vt))))
    # Convertir la matriz resultado de nuevo a un vértice (lista)
    vt = [vt[0][0],vt[1][0],vt[2][0]]
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
      dLight = kwargs["dLight"]
      normal = kwargs["triangleNormal"]

      dLight = np.array(dLight)
      intensity = np.dot(normal, -dLight)

      color = [1,1,1]
      color[0] *= intensity
      color[1] *= intensity
      color[2] *= intensity


      if intensity > 0:
            return color
      else:
            return (0,0,0)

      return color

def toonShader(**kwargs):

      texture = kwargs["texture"]
      tA, tB, tC = kwargs["texCoords"]
      nA, nB, nC = kwargs["normals"]
      dLight = kwargs["dLight"]
      u, v, w = kwargs["bCoords"]

      b = 1.0
      g = 1.0
      r = 1.0

      if texture != None:

            tU = u * tA[0] + V * tB[0] + w * tC[0]
            tV = u * tA[1] + V * tB[1] + w * tC[1]

            textureColor = tecture.getColor(tU, tV)
            b *= textureColor[2]
            g *= textureColor[1]
            r *= textureColor[0]

      normal = [u * nA[0] + v * nB[0] + w * nC[0],
                u * nA[1] + v * nB[1] + w * nC[1],
                u * nA[2] + v * nB[2] + w * nC[2]]

      dLight = np.array(dLight)
      intensity = np.dot(normal, -dLight)

      if intensity <= 0.25:
            intensity = 0.2
      elif intensity <= 0.5:
            intensity = 0.45
      elif intensity <= 0.75:
            intensity = 0.7
      elif intensity <= 1.0:
            intensity = 0.95

      b *= intensity
      g *= intensity
      r *= intensity

      if intensity > 0:
            return r, g, b
      else:
            return[0,0,0]

def negativeFragmentShader(**kwargs):
      texCoords = kwargs["texCoords"]
      texture = kwargs["texture"]
      
      if texture != None:
            color = texture.getColor(texCoords[0], texCoords[1])
      else:
            color = (1, 1, 1)

      negative_color = [1 - c for c in color]

      return negative_color