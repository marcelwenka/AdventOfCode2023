
import numpy as np

matrix = []
galaxies = []

with open("11/data") as file:
    for row, line in enumerate(file):
        matrix.append(list(int(c == "#") for c in line.strip()))
        galaxies.extend((row, column) for column, c in enumerate(line) if c == "#")
matrix = np.asarray(matrix)

def get_all_zeros(axis):
    return list(i for i,x in enumerate(np.all(matrix == 0, axis=axis, keepdims=False)) if x)

columns = get_all_zeros(0)
rows = get_all_zeros(1)

def get_expansions(s, e, elems):
    return len(list(c for c in elems if s < c < e))

def get_asix_expansions(s, e, axis):
    if axis == 1:
        return get_expansions(s, e, rows)
    elif axis == 0:
        return get_expansions(s, e, columns)
    else:
        raise Exception("Unknown axis!")

s = 0

for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i + 1:]:
        sy, ey = min(g1[0], g2[0]), max(g1[0], g2[0])
        sx, ex = min(g1[1], g2[1]), max(g1[1], g2[1])
        s += ey - sy + ex - sx + get_asix_expansions(sx, ex, 0) + get_asix_expansions(sy, ey, 1)

print(s)
