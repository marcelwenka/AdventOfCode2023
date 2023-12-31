
from collections import Counter
from functools import cmp_to_key

order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
orderdict = { v:k for v,k in zip(order, range(len(order))[::-1]) }

strengths = ["five", "four", "full", "three", "two", "one", "high"]
strengthdict = { v:k for v,k in zip(strengths, range(len(order))[::-1]) }

def getStrength(hand):
    freqs = Counter(hand)
    counts = sorted(freqs.values())
    counts.reverse()
    if counts[0] == 5:
        return "five"
    elif counts[0] == 4:
        return "four"
    elif counts[0] == 3 and counts[1] == 2:
        return "full"
    elif counts[0] == 3:
        return "three"
    elif counts[0] == 2 and counts[1] == 2:
        return "two"
    elif counts[0] == 2:
        return "one"
    return "high"

def compare(item1, item2):
    h1, _, s1 = item1
    h2, _, s2 = item2
    if strengthdict[s1] < strengthdict[s2]:
        return 1
    elif strengthdict[s1] > strengthdict[s2]:
        return -1
    else:
        for x,y in zip(h1, h2):
            if orderdict[x] > orderdict[y]:
                return -1
            elif orderdict[x] < orderdict[y]:
                return 1
        raise Exception("Two equal hands")

hands = []
with open("7/data") as file:
    for line in file:
        hand,bid = line.split()
        hands.append((hand, int(bid), getStrength(hand)))
hands.sort(key=cmp_to_key(compare))
hands.reverse()

print(sum(b * (i + 1) for b,i in zip((b for _,b,_ in hands), range(len(hands)))))
