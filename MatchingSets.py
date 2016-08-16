n = int(input())
x = list(map(int, input().split(' ')))
y = list(map(int, input().split(' ')))
diff = []
for i in range(n):
    if abs(x[i] - y[i]) != 0:
        diff.append(abs(x[i] - y[i]))
if len(diff) == len(x):
    print(-1)
else:
    set_diff = set(diff)
    print(set_diff.pop())
