
import networkx as nx
import matplotlib.pyplot as plt
from operator import itemgetter
from tqdm import trange

graph = nx.DiGraph()
start = None
row = 0
column = 0

def left(r, c):
    return (r, c - 1)
def right(r, c):
    return (r, c + 1)
def up(r, c):
    return (r - 1, c)
def down(r, c):
    return (r + 1, c)

def connect_node(node, dir1, dir2):
    graph.add_edge(node, dir1(*node))
    graph.add_edge(node, dir2(*node))

with open("10/data") as file:
    for row, line in enumerate(file):
        for column, c in enumerate(line):
            node = (row, column)
            if c == "J":
                connect_node(node, up, left)
            elif c == "F":
                connect_node(node, right, down)
            elif c == "L":
                connect_node(node, up, right)
            elif c == "7":
                connect_node(node, left, down)
            elif c == "|":
                connect_node(node, up, down)
            elif c == "-":
                connect_node(node, left, right)
            elif c == "S":
                start = node

for dir in [left, up, right, down]:
    if graph.has_edge(dir(*start), start):
        graph.add_edge(start, dir(*start))

graph = graph.to_undirected(reciprocal=True)
graph.remove_nodes_from(list(nx.isolates(graph)))

enclosure = list(map(itemgetter(0), nx.find_cycle(graph, source=start)))

def get_axis(axis):
    if axis == 0:
        return up, down, 0, 1
    elif axis == 1:
        return left, right, 1, 0
    else:
        raise Exception("Unknown axis!")

def is_inside(s, axis):
    before, after, x1, x2 = get_axis(axis)
    befores, afters = 0, 0
    for node in [node for node in enclosure if node[x1] == s[x1] and node[x2] < s[x2]]:
        if graph.has_edge(node, before(*node)):
            afters += 1
        if graph.has_edge(node, after(*node)):
            befores += 1
    return befores % 2 == 1 and afters % 2 == 1

s = 0

for r in trange(row):
    for c in range(column):
        if (r, c) not in enclosure and is_inside((r, c), 0) and is_inside((r, c), 1):
            s += 1

print(s)

# pos = { x:(x[1], row - x[0]) for x in graph.nodes }
# nx.draw(graph, pos=pos, with_labels=True)
# plt.show()
