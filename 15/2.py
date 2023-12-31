
def getHash(label):
    s = 0
    for c in label:
        s += ord(c)
        s = s * 17 % 256
    return s

boxes = { i: {} for i in range(256) }
result = 0

with open("15/data") as file:
    data = file.readline().split(",")
    for step in data:
        if "=" in step:
            label, lens = step.split("=")
            box = getHash(label)
            boxes[box][label] = int(lens)
        elif "-" in step:
            label, _ = step.split("-")
            box = getHash(label)
            if label in boxes[box]:
                boxes[box].pop(label)

for box, lenses in boxes.items():
    for index, lens in enumerate(lenses.values()):
        power = (box + 1) * (index + 1) * lens
        result += power

print(result)
