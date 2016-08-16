n, m = map(int, input().strip().split(' '))
spacestations = [False] * n
for i in input().strip().split(' '):
    spacestations[int(i)] = True
print(spacestations)
distances = []
for i in range(n):
    if spacestations[i]:
        distances.append(0)
    else:
        count = 0
        nearestDistances = []
        if i < n // 2:
            for j in range(n // 2):
                if spacestations[j]:
                    nearestDistances.append(abs(i - j))
        distances.append(min(nearestDistances))
print(max(distances))
