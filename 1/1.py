
s = 0
with open("1/data") as file:
    for line in file:
        digits = [c for c in line if c.isdigit()]
        s += int(digits[0] + digits[-1])
print(s)
