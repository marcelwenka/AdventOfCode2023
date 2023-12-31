
import numpy as np

matrices = []

with open("13/data") as file:
    matrix = []
    for line in file:
        line = line.strip()
        if not line:
            matrices.append(matrix)
            matrix = []
        else:
            matrix.append([int(c == "#") for c in line])
    matrices.append(matrix)

s = 0

def get_symmetry(matrix):
    rows, _ = matrix.shape
    for r in range(rows - 1):
        h = True
        for i in range(min(r + 1, rows - r - 1)):
            if (matrix[r - i, :] != matrix[r + i + 1, :]).any():
                h = False
                break
        if h:
            return r + 1
    return 0

for matrix in matrices:
    matrix = np.matrix(matrix)
    horz = get_symmetry(matrix)
    vert = get_symmetry(matrix.transpose())
    s += vert + horz * 100

print(s)
