from math import isclose

def barycentricCoords(A, B, C, P):

    areaPCB = (B[1] - C[1]) * (P[0] - C[0]) + (C[0] - B[0]) * (P[1] - C[1])
    areaABC = (B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1])
    areaACP = (C[1] - A[1]) * (P[0] - C[0]) + (A[0] - C[0]) * (P[1] - C[1])
    
    try:
        u = pcbArea / abcArea
        v = acpArea / abcArea
        w = 1 - u - v
    except:
        u = v = w = -1
    return u, v, w