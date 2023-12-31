
result = 0
with open("15/data") as file:
    data = file.readline().split(",")
    for step in data:
        s = 0
        for c in step:
            s += ord(c)
            s = s * 17 % 256
        result += s
print(result)
        