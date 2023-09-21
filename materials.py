
class Material(object):
    def __init__(self, diffuse = (1,1,1)):
        self.diffuse = diffuse

def diffuse(r, g, b):
    return (r, g, b)