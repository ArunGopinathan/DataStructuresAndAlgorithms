import sys

t = int(sys.stdin.readline())
total = 0
ans = 0
# setting all bits 31 bits to 1
for i in range(32):
    total += (1 << i)

for _ in range(t):
    n = int(sys.stdin.readline())
    arr = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    result = "NO"
    if n == 1:
        if arr[0] > 0 and (arr[0] & (arr[0] - 1)) == 0:
            result = "YES"
    else:
        for i in range(32):
            ans = total
            for j in range(n):
                if arr[j] & (1 << i):
                    ans &= arr[j]
            if ans > 0 and (ans & (ans - 1)) == 0:
                result = "YES"
                break
    print(result)
