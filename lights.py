import mathLib as ml

class Light:
    def __init__(self, intensity=1, color=(1, 1, 1), lightType="LIGHT"):
        self.intensity = intensity
        self.color = color
        self.type = lightType

    def getColor(self):
        return [self.color[0] * self.intensity,
                self.color[1] * self.intensity,
                self.color[2] * self.intensity]

    def getDiffuseColor(self, intercept):
        return None

    def getSpecularColor(self, intercept, viewPosition):
        return None
    

class Ambient(Light):
    def __init__(self, intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "AMBIENT")


def reflect(normal, direction):
    reflectValue = ml.sub_vector(ml.MultVectorEsc(2 * ml.producto_punto(normal, direction), normal), direction)
    return ml.norm_vector(reflectValue)

class Directional(Light):
    def __init__(self, direction=(0, 1, 0), intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "DIRECTIONAL")
        self.direction = ml.norm_vector(direction)

    def getDiffuseColor(self, intercept):
        direction = [i * -1 for i in self.direction]

        intensity = ml.producto_punto(intercept.normal, direction) * self.intensity
        intensity = max(0, min(1, intensity))
        intensity *= 1 - intercept.obj.material.ks

        return [i * intensity for i in self.color]

    def getSpecularColor(self, intercept, viewPosition):
        direction = [i * -1 for i in self.direction]

        reflectDirection = reflect(intercept.normal, direction)

        viewDirection = ml.sub_vector(viewPosition, intercept.point)
        viewDirection = ml.norm_vector(viewDirection)

        intensity = max(0, min(1, ml.producto_punto(reflectDirection, viewDirection))) ** intercept.obj.material.spec
        intensity *= self.intensity
        intensity *= intercept.obj.material.ks

        return [i * intensity for i in self.color]


class Point(Light):
    def __init__(self, position=(0, 0, 0), intensity=1, color=(1, 1, 1)):
        super().__init__(intensity, color, "POINT")
        self.position = position

    def getDiffuseColor(self, intercept):
        direction = ml.sub_vector(self.position, intercept.point)
        radius = ml.VectorMag(direction)
        direction = ml.DivVectorEsc(direction, radius)

        intensity = ml.producto_punto(intercept.normal, direction) * self.intensity
        intensity *= 1 - intercept.obj.material.ks

        if radius != 0:
            intensity /= radius ** 2
        intensity = max(0, min(1, intensity))

        return [i * intensity for i in self.color]

    def getSpecularColor(self, intercept, viewPosition):
        direction = ml.sub_vector(self.position, intercept.point)
        radius = ml.VectorMag(direction)
        direction = ml.DivVectorEsc(direction, radius)

        reflectDirection = reflect(intercept.normal, direction)

        viewDirection = ml.sub_vector(viewPosition, intercept.point)
        viewDirection = ml.norm_vector(viewDirection)

        intensity = max(0, min(1, ml.producto_punto(reflectDirection, viewDirection))) ** intercept.obj.material.spec
        intensity *= self.intensity
        intensity *= intercept.obj.material.ks

        if radius != 0:
            intensity /= radius ** 2
        intensity = max(0, min(1, intensity))

        return [i * intensity for i in self.color]