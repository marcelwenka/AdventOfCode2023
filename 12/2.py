
def subs(text, i, c):
    return text[:i] + c + text[i + 1:]

def fill_recursive(parts, pi, currentPart, expectedClusters, xi, expected, actual, remaining, blanks):
    s = 0
    if actual + remaining + blanks < expected:
        return 0
    if pi == len(parts):
        if xi == len(expectedClusters):
            return 1
        elif xi == len(expectedClusters) - 1 and currentPart == expectedClusters[xi]:
            return 1
        else:
            raise Exception("Unreachable code encountered!")
    if parts[pi] == "?":
        if currentPart > 0:
            if currentPart == expectedClusters[xi]:
                subs(parts, pi, ".")
                s += fill_recursive(parts, pi + 1, 0, expectedClusters, xi + 1, expected, actual, remaining, blanks - 1)
            elif currentPart < expectedClusters[xi]:
                subs(parts, pi, "#")
                s += fill_recursive(parts, pi + 1, currentPart + 1, expectedClusters, xi, expected, actual + 1, remaining, blanks - 1)
        else:
            if xi < len(expectedClusters):
                subs(parts, pi, "#")
                s += fill_recursive(parts, pi + 1, 1, expectedClusters, xi, expected, actual + 1, remaining, blanks - 1)
                subs(parts, pi, ".")
                s += fill_recursive(parts, pi + 1, 0, expectedClusters, xi, expected, actual, remaining, blanks - 1)
            else:
                subs(parts, pi, ".")
                s += fill_recursive(parts, pi + 1, 0, expectedClusters, xi, expected, actual, remaining, blanks - 1)
    elif parts[pi] == "#":
        if xi == len(expectedClusters):
            return 0
        elif currentPart == expectedClusters[xi]:
            return 0
        else:
            return fill_recursive(parts, pi + 1, currentPart + 1, expectedClusters, xi, expected, actual + 1, remaining - 1, blanks)
    else:
        if currentPart > 0:
            if currentPart != expectedClusters[xi]:
                return 0
            else:
                return fill_recursive(parts, pi + 1, 0, expectedClusters, xi + 1, expected, actual, remaining, blanks)
        else:
            return fill_recursive(parts, pi + 1, 0, expectedClusters, xi, expected, actual, remaining, blanks)
    return s

all = 0

with open("12/data") as file:
    for i, line in enumerate(file):
        parts, sizes = line.split(' ')
        parts = "?".join([parts] * 5)
        sizes = ",".join([sizes] * 5)
        sizes = list(map(int, sizes.split(',')))
        expected = sum(sizes)
        actual = sum(1 for x in parts if x == "#")
        blanks = sum(1 for x in parts if x == "?")
        print(i + 1, parts, sizes)
        s = fill_recursive(parts, 0, 0, sizes, 0, expected, 0, actual, blanks)
        print(s)
        all += s

print(all)
