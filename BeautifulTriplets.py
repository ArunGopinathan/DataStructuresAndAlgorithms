n, d = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
length = len(arr)
count = 0
for i in range(length):
    if (i + d) in arr and (i + 2 * d) in arr:
        count += 1
print(count)
