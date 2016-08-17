import sys
import math
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = bin(int(sys.stdin.readline().strip())).count("1")
    print(str(n))