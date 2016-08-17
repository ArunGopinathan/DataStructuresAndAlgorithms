from collections import Counter

t = int(input())
for _ in range(t):
    c = Counter((input()))
    arr = [c[x] for x in ('r', 'u', 'b', 'y')]
    minimum = min(arr)
    if minimum > 0:
        print(minimum)
    else:
        print(0)
