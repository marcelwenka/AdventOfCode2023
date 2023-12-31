
ids = []
possibilites = { "red": 12, "green": 13, "blue": 14 }
with open("2/data") as file:
    for line in file:
        maxes = { "red": 0, "green": 0, "blue": 0 }
        game, results = line.split(":")
        id = game.replace("Game ", "")
        for round in results.split(";"):
            for single in round.split(','):
                countstr,ball = single.strip().split(' ')
                count = int(countstr)
                if maxes[ball] < count:
                    maxes[ball] = count
        if all(maxes[pk] <= pv for pk,pv in possibilites.items()):
            ids.append(int(id))
print(sum(ids))
