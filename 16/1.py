
matrix = []

with open("16/data") as file:
    for line in file:
        matrix.append([*line.strip()])

size = len(matrix)
visited = []
for _ in range(size):
    row = []
    for c in range(size):
        row.append([])
    visited.append(row)
dirs = [(0, 0, 0, 1)]

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

for line in visited:
    print(*["#" if c else "." for c in line], sep="")

print(sum(sum(1 for x in line if x) for line in visited))
