
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

node = "AAA"
iters = 0
while node != "ZZZ":
    move = moves[iters % len(moves)]
    iters += 1
    if move == "L":
        node = network[node][0]
    else:
        node = network[node][1]

print(iters)
