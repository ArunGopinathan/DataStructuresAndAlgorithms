N = int(input())
list1 = []
for k in range(0, N):
    tid, z, p, l, c, s = map(int, input().split(' '))
    newScore = p * 50 + l * 5 + c * 10 + s * 20
    list1.append((tid, newScore - z, newScore))

# print list1
list1.sort()
list1.sort(key=lambda tup: tup[1])
# print list1
list1 = list1[::-1]
for tup in list1[:5]:
    print(tup[0], tup[2])
