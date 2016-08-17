import sys
n = int(sys.stdin.readline().strip())
arr = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if len(arr)>0:
            del arr[-1]
        elif len(arr)==0:
            break
    else:
        arr.append(num)
print(str(sum(arr)))


