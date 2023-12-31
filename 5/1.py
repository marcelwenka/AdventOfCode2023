from collections import namedtuple
Map = namedtuple("Map", ["start", "end", "mapping"])

dicts = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": []
}
seeds = None

with open("5/data") as file:
    seeds = list(map(int, file.readline().replace('seeds: ', '').split()))
    file.readline()
    for name, d in dicts.items():
        line = file.readline().strip()
        if line != f"{name} map:":
            print(line, name)
            raise Exception("Unexpected dictionary name")
        line = file.readline().strip()
        while line != "":
            value, key, count = map(int, line.split())
            d.append(Map(key, key + count - 1, value))
            line = file.readline().strip()

values = seeds
for d in dicts.values():
    new = []
    for v in values:
        map = next((x for x in d if x.start <= v <= x.end), None)
        if map:
            new.append(v - map.start + map.mapping)
        else:
            new.append(v)
    values = new

print(min(values))
