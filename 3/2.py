from collections import namedtuple
Number = namedtuple("Number", ["row", "start", "end", "number"])

matrix = []
numbers = []
linelenght = None
with open("3/data") as file:
    for i,line in enumerate(file):
        linelenght = len(line)
        matrix.append(line)
        current = ''
        start = -1
        for j,c in enumerate(line):
            if c.isdigit():
                current += c
                if start == -1:
                    start = j
            elif current != '':
                numbers.append(Number(i, start, j - 1, int(current)))
                current = ''
                start = -1
        if current != '':
            numbers.append(Number(i, start, len(line), int(current)))
s = 0
for i,row in enumerate(matrix):
    for j,column in enumerate(row):
        if column == '*':
            adjacent = list(filter(lambda x: i - 1 <= x.row <= i + 1 and x.start - 1 <= j <= x.end + 1, numbers))
            if len(adjacent) == 2:
                s += adjacent[0].number * adjacent[1].number
print(s)
