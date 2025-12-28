def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


# [...]

def euclidean(a, b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
