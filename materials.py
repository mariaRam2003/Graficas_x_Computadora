class Material:
    def __init__(self, diffuse=(1, 1, 1), spec=1.0, ks=0.0):
        self.diffuse = diffuse
        self.spec = spec
        self.ks = ks

def diffuse(r, g, b):
    return (r, g, b)

def nieve():
    return Material(diffuse=(1, 1, 1), spec=0.5, ks=0.2)

def duro():
    return Material(diffuse=(0.3, 0.3, 0.3), spec=0.2, ks=0.1)

def zanahoria():
    return Material(diffuse=(1, 0.5, 0), spec=0.4, ks=0.3)