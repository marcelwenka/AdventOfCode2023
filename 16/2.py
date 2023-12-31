
from tqdm import trange

matrix = []

with open("16/data") as file:
    for line in file:
        matrix.append([*line.strip()])
size = len(matrix)

def getEnergy(dirs):
    visited = []
    for _ in range(size):
        row = []
        for c in range(size):
            row.append([])
        visited.append(row)
    while dirs:
        newdirs = []
        for y, x, yd, xd in dirs:
            if y < 0 or y >= size or x < 0 or x >= size:
                continue
            if (yd, xd) not in visited[y][x]:
                visited[y][x].append((yd, xd))
                if matrix[y][x] == "|" and xd != 0:
                    newdirs.append((y - 1, x, -1, 0))
                    newdirs.append((y + 1, x, 1, 0))
                elif matrix[y][x] == "-" and yd != 0:
                    newdirs.append((y, x - 1, 0, -1))
                    newdirs.append((y, x + 1, 0, 1))
                elif matrix[y][x] == "/":
                    newdirs.append((y - xd, x - yd, -xd, -yd))
                elif matrix[y][x] == "\\":
                    newdirs.append((y + xd, x + yd, xd, yd))
                else:
                    newdirs.append((y + yd, x + xd, yd, xd))
        dirs = newdirs
    return sum(sum(1 for x in line if x) for line in visited)

m = 0
for r in trange(size):
    dirs = [(r, 0, 0, 1)]
    m = max(m, getEnergy(dirs))
    dirs = [(r, size - 1, 0, -1)]
    m = max(m, getEnergy(dirs))
    dirs = [(0, r, 1, 0)]
    m = max(m, getEnergy(dirs))
    dirs = [(size - 1, r, -1, 0)]
    m = max(m, getEnergy(dirs))
print(m)
