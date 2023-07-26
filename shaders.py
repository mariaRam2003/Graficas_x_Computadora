def vertexShader(vertex, modelMatrix):
    vt = [
        vertex[0],
        vertex[1],
        vertex[2],
        1
    ]

    #multiplicar vt con el modelo matriz 4x4
    vt_result = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            vt_result[i] += modelMatrix[i][j] * vt[j]

    vt_result = [
        vt_result[0] / vt_result[3],
        vt_result[1] / vt_result[3],
        vt_result[2] / vt_result[3]
    ]

    return vt_result

def fragmentShader(**kwargs):
    color = (0.5, 0.5, 0.5)
    return color