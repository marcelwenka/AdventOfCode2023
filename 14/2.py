
import numpy as np

rocksdict = { ".": 0, "#": 1, "O": 2 }

rocks = []
with open("14/data") as file:
    for line in file:
        cols = len(line)
        rocks.append([rocksdict[c] for c in line.strip()])
rocks = np.matrix(rocks)
size = len(rocks)

def tilt(board):
    for c in range(size):
        top = 0
        for r in range(size):
            if board[r, c] == 1:
                top = r + 1
            elif board[r, c] == 2:
                board[r, c] = 0
                board[top, c] = 2
                top += 1

cycle = 0
init = 0
prevs = [rocks.copy()]
for _ in range(1000000000):
    for _ in range(4):
        tilt(rocks)
        rocks = np.rot90(rocks, k=-1)
    for i, prev in enumerate(prevs):
        if (rocks == prev).all():
            cycle = len(prevs) - i
            init = i + 1
            break
    if cycle:
        break
    prevs.append(rocks.copy())

add = 1000000000 - init - (1000000000 - init) // cycle * cycle + 1

for _ in range(add):
    for _ in range(4):
        tilt(rocks)
        rocks = np.rot90(rocks, k=-1)

s = 0
for c in range(size):
    for r in range(size):
        if rocks[r, c] == 2:
            s += size - r
print(s)
