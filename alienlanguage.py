n = int(input())
count = 0
qual = set(input().split(' '))
for _ in range(int(input())):
    girl = set(input().split(' '))
    if len(qual.intersection(girl)) >= len(qual):
        count += 1
print(count)
