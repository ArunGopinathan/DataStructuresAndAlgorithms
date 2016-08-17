from collections import Counter

t = int(input())
for _ in range(t):
    s = Counter(list(input()))
    t = Counter(list(input()))
    diff = s - t
    diff2 = t - s
    comb = list(diff.elements()) + list(diff2.elements())
    print(len(comb))
