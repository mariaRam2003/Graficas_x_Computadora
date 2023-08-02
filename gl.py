import struct
from collections import namedtuple
import numpy as np
from obj import Obj
from mathLib import barycentricCoords

V2 = namedtuple('Point2', ['x','y'])
V3 = namedtuple('Point3', ['x','y','z'])

POINTS = 0
LINES = 1
TRIANGLES = 2
QUADS = 3

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    return struct.pack('=h', w)

def dword(d):
    return struct.pack('=l', d)

def color(r, g, b):
    return bytes([int(b), int(g), int(r)])

class Model(object):
    def __init__(self, filename, translate=(0,0,0), rotate=(0,0,0), scale=(1,1,1)):
        model = Obj(filename)

        self.faces = model.faces
        self.vertices = model.vertices
        self.texcoords = model.texcoords
        self.normals = model.normals

        self.translate = translate
        self.rotate = rotate
        self.scale = scale

class Renderer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.glClearColor(0,0,0)
        self.glClear()
        self.glColor(1,1,1)
        self.objects = []
        self.vertexShader = None
        self.fragmentShader = None
        self.primitiveType = TRIANGLES
        self.vertexBuffer=[ ]

    def glAddVertices(self, vertices):
        for vert in vertices:
            self.vertexBuffer.append(vert)

    def glPrimitiveAssembly(self,tVerts):
        primitives = [ ]
        if self.primitiveType == TRIANGLES:
            for i in range(0,len(tVerts), 3):
                triangle = [ ]
                triangle.append(tVerts[i])
                triangle.append(tVerts[i+1])
                triangle.append(tVerts[i+2])
                primitives.append(triangle)
        
        return primitives


    def glClearColor(self, r, g, b):
        self.clearColor = color(r,g,b)

    def glColor(self, r, g, b):
        self.currColor = color(r,g,b)

    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)]
                       for x in range(self.width)]
        
        self.zbuffer = [[float('inf') for y in range(self.height)]
                        for x in range(self.width)]

    
    def glPoint(self, x, y, clr = None):
        if (0 <= x < self.width) and (0 <= y < self.height):
            self.pixels[x][y]=clr or self.currColor

    # BARYCENTRIC TRIANGLE
    def glTriangle_bc(self, A, B, C):

        minX = round(min(A[0], B[0], C[0]))
        maxX = round(max(A[0], B[0], C[0]))
        minY = round(min(A[1], B[1], C[1]))
        maxY = round(max(A[1], B[1], C[1]))

        colorA = color(255, 0, 0) 
        colorB = color(0, 255, 0)
        colorC = color(0, 0, 255)

         for x in range(minX, maxX + 1):
            for y in range(minY, maxY + 1):
                if (0 <= x < self.width) and (0 <= y < self.height):
                    P = (x,y)
                    u, v, w = getBarycentricCoordinates(A, B, C, P)
                    if 0 <= u <= 1 and 0 <= v <= 1 and 0 <= w <= 1:
                        z = u * A[2] + v * B[2] + w * C[2]
                        if z < self.zbuffer[x][y]:
                            self.zbuffer[x][y] = z
                            pixelColor = color( u * colorA[0] + v * colorB[0] + w * colorC[0],
                                                u * colorA[1] + v * colorB[1] + w * colorC[1],
                                                u * colorA[2] + v * colorB[2] + w * colorC[2])
                            self.glPoint(x,y, pixelColor)

    def glModelMatrix(self, translate=(0,0,0), scale=(1,1,1)):
        translateMat = np.matrix([[1,0,0,translate[0]],
                                 [0,1,0,translate[1]],
                                 [0,0,1,translate[2]],
                                 [0,0,0,1]])

    rotMat = self.glRotationMatrix(rotate[0], rotate[1], rotate[2])

        scaleMat = np.matrix([[scale[0],0,0,0],
                              [0,scale[1],0,0],
                              [0,0,scale[2],0],
                              [0,0,0,1]])
        
        return translateMat * scaleMat * rotMat

    def glRotationMatrix(self, pitch = 0, yaw = 0, roll = 0):

        pitch *= pi/100
        yaw *= pi/180
        roll *= pi/180

        pitchMat = np.matrix([[1,0,0,0],
                                [0,cos(pitch), -sin(pitch), 0],
                                ])




    def glLine(self, v0, v1, clr=None):
        #Bresenham line algorithm
        #m=(v1.y-v0.y)/(v1.x-v0.x)
        #y=v0.y
        #for x in range(v0.x, v1.x + 1):
            #self.glPoint(x,int(y))
            #y+=m

        x0=int(v0[0])
        x1=int(v1[0])
        y0=int(v0[1])
        y1=int(v1[1])

        #si el punto 0 es igual al punto 1 solo dibujar un punto
        if x0==x1 and y0==y1:
            self.glPoint(x0,y0)
            return
        
        dy = abs(y1-y0)
        dx = abs(x1-x0)

        steep = dy > dx

        # si la linea tiene pendiente > 1 
        # se intercambian las x por y para poder
        # dibujar la linea de manera vertical en vez de horizontal 
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        
        # Si el punto inicial en X es mayor que el punto final en X
        # intercambiamos los puntos para siempre dibujar de
        # izquierda a derecha
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1-y0)
        dx = abs(x1-x0)


        offset=0
        limit=0.5
        m = dy/dx
        y=y0

        for x in range(x0, x1+1):
            if steep:
                #Dibujar de manera vertical
                self.glPoint(y,x, clr or self.currColor)
            else:
                #Dibujar de manera horizontal
                self.glPoint(x,y, clr or self.currColor)

            offset += m

            if offset >= limit:
                if y0<y1:
                    y+=1
                else:
                    y-=1
                
                limit +=1

    def glLoadModel(self, filename, translate=(0,0,0),rotate=(0,0,0) ,scale=(1,1,1)):
       
        self.objects.append(Model(filename,translate,rotate,scale))

    def glRender(self):
        transformedVerts = []

        for model in self.objects:
            mMatrix = self.glModelMatrix(model.translate, model.scale)

            for face in model.faces:
                vertCount = len(face)
                v0=model.vertices[face[0][0] -1]
                v1=model.vertices[face[1][0] -1]
                v2=model.vertices[face[2][0] -1]
                if vertCount == 4:
                    v3=model.vertices[face[3][0] -1]

                if self.vertexShader:
                    v0=self.vertexShader(v0, modelMatrix=mMatrix)
                    v1=self.vertexShader(v1, modelMatrix=mMatrix)
                    v2=self.vertexShader(v2, modelMatrix=mMatrix)
                    if vertCount == 4:
                        v3=self.vertexShader(v3, modelMatrix=mMatrix)
                
                transformedVerts.append(v0)
                transformedVerts.append(v1)
                transformedVerts.append(v2)
                if vertCount == 4:
                    transformedVerts.append(v0)
                    transformedVerts.append(v2)
                    transformedVerts.append(v3)

        primitives = self.glPrimitiveAssembly(transformedVerts)

        primColor = None
        if self.fragmentShader:
            primColor = self.fragmentShader()
            primColor = color(primColor[0],
                              primColor[1],
                              primColor[2],)
        else:
            primColor = self.currColor

        for prim in primitives:
            if self.primitiveType == TRIANGLES:
                self.glTriangle(prim[0], prim[1], prim[2], primColor)

    def glFinish(self, filename):
        with open(filename, "wb") as file:
            #Header
            file.write(char("B"))
            file.write(char("M"))
            file.write(dword(14+40+(self.width*self.height * 3)))
            file.write(dword(0))
            file.write(dword(14+40))

            #InfoHeader
            file.write(dword(40))
            file.write(dword(self.width))
            file.write(dword(self.height))
            file.write(word(1))
            file.write(word(24))
            file.write(dword(0))
            file.write(dword((self.width*self.height * 3)))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            #ColorTable
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])