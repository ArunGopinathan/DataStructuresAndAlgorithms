def check(span):
    i = 0
    S = []
    global pw
    while i + span <= len(st):
        q = s[i + span] - s[i]
        q *= pw[1000000 - i]
        if q in S:
            return True
        S.append(q)
        i += 1
    return False


st = input()
prime = 31
pw = [0] * 1000001
s = [0] * 10000001

pw[0] = 1
i = 1
while i < 1000001:
    pw[i] = pw[i - 1] * prime
    i += 1

for i in range(1, len(st) + 1):
    s[i] = s[i - 1] + ord(st[i - 1]) * pw[i - 1]

l = 0
r = len(st)

while l < r:
    mid = (l + r + 1) // 2
    if (check(mid)):
        l = mid
    else:
        r = mid - 1
print(l)
