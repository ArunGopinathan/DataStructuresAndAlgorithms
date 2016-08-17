for _ in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split(' ')]
    k = int(input())
    flag = 0
    print(1<<n)
    for i in range(1, 1 << n):
        print("i val:"+str(i))
        val = 0
        for j in range(n):
            print("j val:"+str(j))
            print(str(1 << j))
            if i & (1 << j):
                val += A[j]
        if val == k:
            flag = 1
            break
    if flag:
        print("YES")
    else:
        print("NO")
