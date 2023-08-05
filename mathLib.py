def matMatMult(m1, m2):
    result = [[0 for _ in range(len(m2[0]))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result


def matMult(m1, m2):
    return [[sum(m1[x][i] * m2[i][y] for i in range(4)) for y in range(4)] for x in range(4)]

def matVectMult(mat, vect):
    return [sum(mat[x][y] * vect[y] for y in range(4)) for x in range(4)]