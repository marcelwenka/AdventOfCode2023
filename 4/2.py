
d = { }
with open("4/data") as file:
    for i,line in enumerate(file):
        d[i] = d.get(i, 0) + 1
        _, numbers = line.split(':')
        left, right = numbers.split('|')
        winning = list(map(int, left.split()))
        count = 0
        for o in map(int, right.split()):
            if o in winning:
                count += 1
        for j in range(i + 1, i + count + 1):
            d[j] = d.get(j, 0) + d[i]
print(sum(d.values()))
