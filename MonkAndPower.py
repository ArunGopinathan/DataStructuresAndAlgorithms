n = int(input())
arr = [int(x) for x in input().split(' ')]
arr2 = [int(x) for x in input().split(' ')]
count = 0

while len(arr) > 0 and len(arr2) > 0:
    if arr2[0] == arr[0]:
        arr2.pop(0)
        arr.pop(0)
        count += 1
    else:
        arr.append(arr.pop(0))
        count += 1
print(count)