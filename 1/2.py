
s = 0
digitnames = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
with open("1/data") as file:
    for line in file:
        digits = []
        for i,c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for key,value in digitnames.items():
                if line[i:i+len(value)] == value:
                    digits.append(key)
        s += int(digits[0] + digits[-1])
print(s)
