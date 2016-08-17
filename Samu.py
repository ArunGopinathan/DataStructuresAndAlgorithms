import sys
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().strip().split(' '))
    total = 0
    total = int(sys.stdin.readline().strip(),2);
    for i in range(1,n):
        total ^= int(sys.stdin.readline().strip(),2)
    if total > 0:
        print(str(bin(total).count("1")))
    else:
        print(str(k))


