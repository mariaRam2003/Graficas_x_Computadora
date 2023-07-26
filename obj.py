class Obj(object):
    def __init__(self, filename):
        with open(filename,"r") as file:
            self.lines = file.read().splitlines()
        
        self.vertices = []
        self.texcoords = []
        self.normals = []
        self.faces = []

        for line in self.lines:
            try:
                prefix, value = line.split(" ", 1)
            except:
                continue

            if prefix == "v": #vertices
               self.vertices.append(list(map(float, value.split(" "))))
            elif prefix == "vt": #texture coordinates
               self.texcoords.append(list(map(float, value.split(" "))))
            elif prefix == "vn": #normals
               self.normals.append(list(map(float, value.split(" "))))
            elif prefix == "f": #Faces
               self.faces.append([(list(map(int, vert.split("/")))) for vert in value.split(" ")])