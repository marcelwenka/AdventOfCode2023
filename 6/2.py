
# trywialne rozwiązanie z części pierwszej zwraca wynik w około 7 sekund
with open("6/data") as file:
    time = int(file.readline().replace("Time:", "").replace(" ", ""))
    distance = int(file.readline().replace("Distance:", "").replace(" ", ""))
    p1 = 0
    p2 = time // 2
    while True:
        pivot = (p1 + p2) // 2
        if (time - pivot) * pivot > distance:
            p2 = pivot
        else:
            p1 = pivot
        if p2 - p1 <= 1:
            print(time - 2 * p2 + 1)
            exit()
