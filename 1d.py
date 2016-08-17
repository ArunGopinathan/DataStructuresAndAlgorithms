import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr = []
    count = 1;
    arr = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            count += 1
        else:
            arr[i] = arr[i - 1]
    print(str(count))
