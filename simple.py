n = 5
print(1 << n)
for i in range(1, 1 << n):
    print("i value:"+i)
    val = 0
    for j in range(n):
        print("j value:"+j)
        if i & (1<<j):
            print("i & 1<<h"+ 1<<j)
