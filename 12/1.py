
from tqdm import tqdm
from collections import namedtuple
import re

PartList = namedtuple('PartList', ['questionMarks', 'partsCount', 'partClusters'])
Cluster = namedtuple('Cluster', ['start', 'length', 'end'])

all = 0

def subs(text, i, c):
    return text[:i] + c + text[i + 1:]

def fill_recursive(line, i, expected_regex):
    s = 0
    if i == len(line):
        if re.match(expected_regex, line):
            return 1
        else:
            return 0
    if line[i] == "?":
        line = subs(line, i, ".")
        s += fill_recursive(line, i + 1, expected_regex)
        line = subs(line, i, "#")
        s += fill_recursive(line, i + 1, expected_regex)
    else:
        s += fill_recursive(line, i + 1, expected_regex)
    return s

with open("12/data") as file:
    for line in tqdm(file):
        parts, sizes = line.split(' ')
        sizes = list(map(int, sizes.split(',')))
        expected = "^\.*" + "\.+".join("#" * s for s in sizes) + "\.*$"
        all += fill_recursive(parts, 0, expected)

print(all)
