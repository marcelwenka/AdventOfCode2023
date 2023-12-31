
from collections import namedtuple

P2D = namedtuple("P2D", ["x", "y"])

area = 0
x, y = 0, 0
prev = P2D(0, 0)

# triangle area given vertex coordinates p1, p2, p3
# 1/2 |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|

# simplified formula where p1 is (0,0)
# 1/2 |x2 * y3 - x3 * y2|

# the modulus is dropped to accomodate for substracting the area in a non-convex polygon
# for every side half of its length is added to accomodate for the fact that sides have a "thickness" of 1
# 1 is added at the end to accomodate for not inluding the corners in the "thinkness" calculation
# the remaining corners cancel out when overlapping

with open("18/data") as file:
    for line in file:
        _, _, c = line.split()
        color = c.strip("()#")
        l = int(color[:5], 16)
        d = color[-1]
        if d == "0": x += l
        if d == "2": x -= l
        if d == "3": y -= l
        if d == "1": y += l
        area += (prev.x * y) - (x * prev.y) + l
        prev = P2D(x, y)

print(area // 2 + 1)
