import sys
t = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().strip().split(' ')]
result = 0
for i in range(t):
    result |= arr[i]
print(str(result))
