input()
diff = 0
for i in map(int, input().split()):
    diff = i - diff
    if diff < 0:
        break
if diff:
    print("NO")
else:
    print("YES")
