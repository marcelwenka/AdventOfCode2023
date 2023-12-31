
from math import lcm

moves = None
network = dict()

with open("8/data") as file:
    moves = file.readline().strip()
    file.readline()
    line = file.readline()
    while line:
        node, dirs = line.strip().split(" = ")
        left, right = dirs.strip("()").split(", ")
        network[node] = (left, right)
        line = file.readline()

nodes = list((node, node) for node in network.keys() if node[-1] == "A")
endings = { n[0]:[] for n in nodes }
visited = set()

iters = 0
while len(nodes) > 0:
    midx = iters % len(moves)
    move = moves[midx]
    iters += 1
    new = []
    for start, node in nodes:
        n = network[node][0 if move == "L" else 1]
        key = (start, n, midx)
        if key not in visited:
            visited.add(key)
            new.append((start, n))
            if n[-1] == "Z":
                endings[start].append(iters)
    nodes = new

possibilities = [[]]
for ends in endings.values():
    new = []
    for end in ends:
        for p in possibilities:
            new.append([*p, end])
    possibilities = new

minimum = float("inf")
for p in possibilities:
    l = lcm(*p)
    if l < minimum:
        minimum = l

print(minimum)
