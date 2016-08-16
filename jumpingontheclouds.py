n, k = map(int, input().split(' '))
c = list(map(int, input().split(' ')))
E = 100
if len(c) < k:
    print("np")
else:
    next = 0
    i = 0
    while True:
        nexti = (i + k) % n
        if c[nexti] == 1:
            E -= 3
        else:
            E -= 1
        if nexti == 0:
            break
        i += k

print(E)
