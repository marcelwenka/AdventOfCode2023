
s = 0
with open("4/data") as file:
    for line in file:
        _, numbers = line.split(':')
        left, right = numbers.split('|')
        winning = list(map(int, left.split()))
        p = -1
        for o in map(int, right.split()):
            if o in winning:
                p += 1
        if p >= 0:
            s += 2 ** p
print(s)
