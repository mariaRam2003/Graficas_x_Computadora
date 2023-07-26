import struct # to convert data to bytes
from collections import namedtuple
from obj import Obj
from math import sin, cos

V2 = namedtuple('Point2', ['x', 'y']) # 2D point
V3 = namedtuple('Point2', ['x', 'y', 'z']) # 3D point

POINTS = 0
LINES = 1
TRIANGLES = 2
QUADS = 3

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l', d)

def color(r, g, b):
    # mul by 255 to get the color in bytes caus r, g, b are in range 0-1
    return bytes([int(b * 255), 
                  int(g * 255),
                  int(r * 255)])

# pasar V2 a puntos
def toV2(point):
    return V2(point[0], point[1])



class Model(object):
    def __init__ (self, filename, transalate=(0,0,0), rotate = (0,0,0), scale = (1,1,1)):
        model = Obj(filename)

        self.vertices = model.vertices
        self.texcoords = model.texcoords
        self.normals = model.normals
        self.faces = model.faces

        self.translate = transalate
        self.rotate = rotate        
        self.scale = scale

class Renderer(object):
    # width and height of a frame
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.glClearColor(0, 0, 0)
        self.glClear()

        self.glColor(1, 1, 1)

        self.objects = []

        self.vertexShader = None
        self.fragmentShader = None

        self.primitiveType = TRIANGLES
        self.vertexBuffer = []

    # Dibuja un poligono con coordenadas (x,y)
    def drawPolygon(self, *points):
        for i in range(len(points)):
            v0 = toV2(points[i])
            v1 = toV2(points[(i + 1) % len(points)])
            self.glLine(v0, v1)
    
    # Aplicando algoritmo scanline
    def scanline_fill(self, *points, fill_color=None):
        if not fill_color:
            fill_color = self.currColor
            
        # Encontrando y_min y y_max
        y_values = [int(point.y) for point in points]
        y_min = min(y_values)
        y_max = max(y_values)
        
        # Iterar scanlines
        for y in range(y_min, y_max + 1):
            intersections = []
            
            # Encontrar intersecciones del scanline con los bordes del poligono
            for i in range(len(points)):
                p1 = points[i]
                p2 = points[(i + 1) % len(points)]
                
                if p1.y != p2.y:
                    # Asegurarnos de que p1 tenga la coordenada y mas baja
                    if p1.y > p2.y:
                        p1, p2 = p2, p1
                        
                if p1.y <= y < p2.y or p2.y <= y < p1.y:
                    # Calcular la coordenada x de la interseccion
                    x_intersect = int(p1.x + (y - p1.y) * (p2.x -p1.x) / (p2.y - p1.y))
                    intersections.append(x_intersect)
            
            # Sort a las intersecciones
            intersections.sort()
            
            # Llenar los pixeles que estan entre las intersecciones
            for i in range(0, len(intersections), 2):
                x_start = intersections[i]
                x_end = intersections[i + 1] if i + 1 < len(intersections) else intersections[i]
                
            for x in range(x_start, x_end + 1):
                self.glPoint(x, y, fill_color)
            

    def glTriangle(self, v0, v1, v2, clr=None):
        self.glLine(v0, v1, clr or self.currColor)
        self.glLine(v1, v2, clr or self.currColor)
        self.glLine(v2, v0, clr or self.currColor)
    
    def glModelMatrixNoNP(self, translate = (0,0,0), scale=(1,1,1), rotate = (0,0,0)):
        #matriz de tranlacion
        translation = [[1,0,0,translate[0]],
                       [0,1,0,translate[1]],
                       [0,0,1,translate[2]],
                       [0,0,0,1]]
        #matriz de scale
        scaleMat = [[scale[0], 0,0,0],
                    [0,scale[2],0,0],
                    [0,0,scale[2],0],
                    [0,0,0,1]]
        
        

        #Logica para multiplicacion de las 2 matrices
        result = [[0, 0, 0, 0] for _ in range(4)]

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    result[i][j] += translation[i][k] * scaleMat[k][j]

        return result


    def glAddVertices(self, vertices):
        for vertex in vertices:
            self.vertexBuffer.append(vertex) 

    def glPrimitiveAssembly(self, tVertices):
        primitives = []

        # Convert the vertices to triangles
        if self.primitiveType == TRIANGLES:
            for i in range(0, len(tVertices), 3):
                triangle = []
                triangle.append(tVertices[i])
                triangle.append(tVertices[i+1])
                triangle.append(tVertices[i+2])
                primitives.append(triangle)
        return primitives


    def glLoadModel(self, filename, translate = (0,0,0), rotate = (0,0,0), scale = (1,1,1)):
        self.objects.append(Model(filename, translate,rotate,scale))


    # determining the color of each pixel
    def glClearColor(self, r,g,b):
        self.clearColor = color(r,g,b)

    def glColor(self, r,g,b):
        self.currColor = color(r,g,b)

    # filling the frame with a single color
    def glClear(self):
        self.pixels = [[self.clearColor for y in range(self.height)] 
                       for x in range(self.width)]
        
    def glPoint(self, x, y, clr = None):
        if(x < self.width and x >= 0 and y < self.height and y >= 0): # check if the point is inside the frame
            self.pixels[int(x)][int(y)] = clr or self.currColor

    def glLine(self, v0, v1, clr = None):
        '''        
        # bresenham's line algorithm
        # y = mx + b
        m = (v1.y - v0.y) / (v1.x - v0.x)
        y = v0.y # the y value of the first point

        for x in range(v0.x, v1.x + 1):
            self.glPoint(x, int(y))
            y += m
        '''

        x0 = int(v0[0])
        x1 = int(v1[0])
        y0 = int(v0[1])
        y1 = int(v1[1])

        # check if the line is steep
        if x0 == x1 and y0 == y1:
            self.glPoint(x0, y0)
            return
        
        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        steep = dy > dx

        # if the line is steep, we transpose the image, it means rotating 90 degrees theoretically
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1

        # if the initial point is bigger than the last point, we swap them
        if x0 > x1:    
            x0, x1 = x1, x0
            y0, y1 = y1, y0

        dy = abs(y1 - y0)
        dx = abs(x1 - x0)

        offset = 0
        limit = 0.5
        m = dy/dx
        y = y0
         
        for x in range(x0, x1 + 1):
            if steep:
                self.glPoint(int(y), x, clr or self.currColor)
            else:
                self.glPoint(x, int(y), clr or self.currColor)
            
            offset += m

            if offset >= limit:
                y += 1 if y0 < y1 else -1; limit += 1
        
    # generating the file, framebuffer, image    
    def glFinish(self, filename):
        with open(filename, 'wb') as file:
            # link to the format http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm
            # header 
            file.write(char('B'))
            file.write(char('M'))
            file.write(dword(14 + 40 + self.width * self.height * 3)) # file size, 14 is the header size, 40 is the info header size and 3 is the number of bytes per pixel
            file.write(dword(0))
            file.write(dword(14 + 40)) # offset where the image starts

            # info header
            file.write(dword(40))
            file.write(dword(self.width))   
            file.write(dword(self.height))
            file.write(word(1)) # number of color planes, what is planes? like layers?
            file.write(word(24)) # number of bits per pixel, this will define the color depth
            file.write(dword(0)) # compression method
            file.write(dword(self.width * self.height * 3)) # raw image size

            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))
            file.write(dword(0))

            # color table, bitmap data
            for y in range(self.height):
                for x in range(self.width):
                    file.write(self.pixels[x][y])

    def glRender(self):
        transformedVerts = []

        for model in self.objects:
            mMat2 = self.glModelMatrixNoNP(model.translate, model.scale, model.rotate)

            for face in model.faces:
                vertCount = len(face)

                v0 = model.vertices [face[0][0] - 1]
                v1 = model.vertices [face[1][0] - 1]
                v2 = model.vertices [face[2][0] - 1]
                if vertCount == 4:
                    v3 = model.vertices [face[3][0] - 1]

                if self.vertexShader:
                    v0 = self.vertexShader(v0,modelMatrix = mMat2)
                    v1 = self.vertexShader(v1,modelMatrix = mMat2)
                    v2 = self.vertexShader(v2,modelMatrix = mMat2)
                    if vertCount == 4:
                        v3 = self.vertexShader(v3, modelMatrix = mMat2)
                
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
                               primColor[2])
        else:
            primColor = self.currColor

        for prim in primitives:
            if self.primitiveType == TRIANGLES:
                self.glTriangle(prim[0], prim[1], prim[2], primColor)

        # Dibujar el polígono 1 con las coordenadas proporcionadas
        # 1
        self.drawPolygon((165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410), (193, 383))
        self.scanline_fill(V2(165, 380), V2(185, 360), V2(180, 330), V2(207, 345), V2(233, 330), V2(230, 360), V2(250, 380), V2(220, 385), V2(205, 410), V2(193, 383))
        
        # 2
        self.drawPolygon((321, 335), (288, 286), (339, 251), (374, 302))
        self.scanline_fill(V2(321, 335), V2(288, 286), V2(339, 251), V2(374, 302))
        
        # 3
        self.drawPolygon((377, 249), (411, 197), (436, 249))
        self.scanline_fill(V2(377, 249), V2(411, 197), V2(436, 249))
        
        # 4
        self.drawPolygon((413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52), (750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230), (597, 215), (552, 214), (517, 144), (466, 180))
        self.scanline_fill(V2(413, 177), V2(448, 159), V2(502, 88), V2(553, 53), V2(535, 36), V2(676, 37), V2(660, 52), V2(750, 145), V2(761, 179), V2(672, 192), V2(659, 214), V2(615, 214), V2(632, 230), V2(580, 230), V2(597, 215), V2(552, 214), V2(517, 144), V2(466, 180))
        
        # 5
        self.drawPolygon((682, 175), (708, 120), (735, 148), (739, 170))
        self.scanline_fill(V2(682, 175), V2(708, 120), V2(735, 148), V2(739, 170), fill_color=color(0, 0, 0))