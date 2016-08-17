import sys

t = int(sys.stdin.readline())

for _ in range(t):
    z, n = map(int, sys.stdin.readline().strip().split(' '))
    whole = 0
    arr = sys.stdin.readline().strip().split(' ')
    for i in range(len(arr)):
        if i == 0:
            whole = int(arr[i])
        else:
            whole &= int(arr[i])
    if whole & z == 0:
        print("Yes")
    else:
        print("No")
