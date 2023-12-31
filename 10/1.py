
import networkx as nx
import math
import matplotlib.pyplot as plt

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

# pos = { x:(x[1], row - x[0]) for x in graph.nodes }
# nx.draw(graph, pos=pos)
# plt.show()

cycle = nx.find_cycle(graph, source=start)
print(math.ceil(len(cycle) / 2))
