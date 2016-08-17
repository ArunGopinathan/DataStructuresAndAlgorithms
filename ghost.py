from collections import Counter

n, m = map(int, input().split(' '))
a = map(int, input().split(' '))
d = Counter()
mv = -1
mq = []
for i in a:
    d[i] += 1
    if d[i] > mv:
        mv = d[i]
        mq = [i]
    elif d[i] == mv:
        mq.append(i)
    print(max(mq), mv)
