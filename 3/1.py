from collections import namedtuple
Number = namedtuple("Number", ["row", "start", "end", "number"])
specialchars = "!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"

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
for n in numbers:
    isPartNumber = False
    for i in range(max(0, n.row - 1), min(n.row + 2, len(matrix))):
        for j in range(max(0, n.start - 1), min(n.end + 2, linelenght)):
            if matrix[i][j] in specialchars:
                isPartNumber = True
    if isPartNumber:
        s += n.number
print(s)
