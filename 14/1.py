
rocks = []
cols = 0

with open("14/data") as file:
    for line in file:
        cols = len(line)
        rocks.append([*line.strip()])

rows = len(rocks)

s = 0

for c in range(cols):
    top = 0
    for r in range(rows):
        if rocks[r][c] == "#":
            top = r + 1
        elif rocks[r][c] == "O":
            rocks[r][c] = "."
            rocks[top][c] = "O"
            s += rows - top
            top += 1

print(s)
