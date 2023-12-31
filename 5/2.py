from collections import namedtuple
Map = namedtuple("Map", ["start", "end", "count", "mapping"])
Range = namedtuple("Range", ["start", "end"])

dicts = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": []
}
pairs = None

with open("5/data") as file:
    pairs = list(map(int, file.readline().replace('seeds: ', '').split()))
    file.readline()
    for name, d in dicts.items():
        line = file.readline().strip()
        if line != f"{name} map:":
            print(line, name)
            raise Exception("Unexpected dictionary name")
        line = file.readline().strip()
        while line != "":
            value, key, count = map(int, line.split())
            d.append(Map(key, key + count - 1, count, value))
            line = file.readline().strip()

values = []
for start, count in zip(pairs[0::2], pairs[1::2]):
    values.append(Range(start, start + count - 1))
for d in dicts.values():
    new = []
    for value in values:
        maps = list(sorted((x for x in d if x.start <= value.end and value.start <= x.end), key=lambda x: x.start))
        if len(maps) == 0:
            new.append(Range(value.start, value.end))
        else:
            v = value.start
            m = 0
            while m < len(maps) and v <= value.end:
                map = maps[m]
                if v < map.start:
                    new.append(Range(v, map.start - 1))
                    v = map.start
                else:
                    offset = v - map.start
                    if map.end < value.end:
                        new.append(Range(map.mapping + offset, map.mapping + map.count - 1))
                        v = map.end + 1
                    else:
                        new.append(Range(map.mapping + offset, map.mapping + value.end - map.start))
                        v = value.end + 1
                    m += 1
            if v <= value.end:
                new.append(Range(v, value.end))
    values = new

print(min((x.start for x in values)))
