t = int(input())
for _ in range(t):
    n, k = map(int, input().split(' '))
    popularity = [int(pop) for pop in input().split(' ')]
    newpop = []
    count = 0
    for i in range(len(popularity) - 1):
        if popularity[i] < popularity[i + 1]:
            newpop.append(popularity[i + 1])
            count += 1
        if count == k:
            break
    print(newpop)
