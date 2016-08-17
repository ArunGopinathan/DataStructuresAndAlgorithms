
for _ in range(int(input())):
    n, m, s = map(int, input().strip().split())
    bla = (s + m - 1) % n
    if bla != 0:
        print(bla)
    else:
        print(n)
