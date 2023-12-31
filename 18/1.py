
from collections import namedtuple
from tqdm import trange

P2D = namedtuple("P2D", ["x", "y"])
Vertical = namedtuple("Vertical", ["x", "y1", "y2"])

x, y = 0, 0
verticals = []
points = []

with open("18/data") as file:
    for line in file:
        d, l, _ = line.split()
        l = int(l)
        if d == "R":x += l
        if d == "L":x -= l
        if d == "U":
            verticals.append(Vertical(x, y - l, y))
            y -= l
        if d == "D":
            verticals.append(Vertical(x, y, y + l))
            y += l
        points.append(P2D(x, y))

area = sum(v.y2 - v.y1 - 1 for v in verticals) + len(set(points)) # avoiding case when vertical lines overlap
xmin = min(map(lambda p: p.x, points))
xmax = max(map(lambda p: p.x, points))
ymin = min(map(lambda p: p.y, points))
ymax = max(map(lambda p: p.y, points))

for x in trange(xmin, xmax + 1):
    for y in range (ymin, ymax + 1):
        ups, downs, ins = 0, 0, 0
        for v in verticals:
            if v.x >= x: continue
            if y < v.y1 or v.y2 < y: continue
            if v.y1 < y < v.y2: ins += 1
            elif v.y1 == y: ups += 1
            elif v.y2 == y: downs += 1
            else: raise Exception("Unexpected type of vertical line.")
        vertCirc = any(filter(lambda v: v.x == x and v.y1 <= y <= v.y2, verticals))
        if ((ins + ups) % 2 == 1 or (ins + downs) % 2 == 1) and not vertCirc:
            area += 1

print(area)
