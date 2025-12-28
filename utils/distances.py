import math

def minkowski(a, b, p):
    # Formülün aslı: Mutlak değerlerin p. kuvvetlerinin toplamının (1/p). kuvveti
    return (abs(b[0] - a[0])**p + abs(b[1] - a[1])**p) ** (1/p)

def manhattan(a, b):
    # Manhattan, Minkowski'nin p=1 halidir
    return minkowski(a, b, 1)

def euclidean(a, b):
    # Euclidean, Minkowski'nin p=2 halidir
    return minkowski(a, b, 2)
