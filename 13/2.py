
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

def get_symmetry(matrix):
    rows, _ = matrix.shape
    for r in range(rows - 1):
        d = 0
        for i in range(min(r + 1, rows - r - 1)):
            d += (matrix[r - i, :] != matrix[r + i + 1, :]).sum()
            if d > 1:
                h = False
                break
        if d == 1:
            return r + 1
    return 0

s = 0

for matrix in matrices:
    matrix = np.matrix(matrix)
    horz = get_symmetry(matrix)
    vert = get_symmetry(matrix.transpose())
    s += vert + horz * 100

print(s)
