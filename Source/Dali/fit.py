import numpy as np

def LinearMap(data, m, q):
    return [m * x + q for x in data]

def ParabolicMap(data, a, b, c):
    return [a * x ** 2 + b * x + c for x in data]

def ArmonicMap(data, A, B, w1, w2, p1, p2):
    return [A * np.sin(w1 * x + p1) + B * np.cos(w2 * x + p2) for x in data]
