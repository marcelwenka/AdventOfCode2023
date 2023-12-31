
result = 1
with open("6/data") as file:
    times = map(int, file.readline().replace("Time:", "").strip().split())
    distances = map(int, file.readline().replace("Distance:", "").strip().split())
    for time, distance in zip(times, distances):
        possibilities = 0
        for t in range(time + 1):
            if (time - t) * t > distance:
                possibilities += 1
        result *= possibilities
print(result)
