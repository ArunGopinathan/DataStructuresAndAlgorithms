n = int(input())

A = []
maximum3 = []
for x in input().strip().split(' '):
    val = int(x)
    if len(maximum3) + 1 < 3:
        print(-1)
        maximum3.append(val)
        maximum3.sort(reverse=True)
    else:
        if len(maximum3) + 1 == 3:
            maximum3.append(val)
            maximum3.sort(reverse=True)
        else:
            if val >= maximum3[0]:
                maximum3[2] = maximum3[1]
                maximum3[1] = maximum3[0]
                maximum3[0] = val
            elif val >= maximum3[1]:
                maximum3[2] = maximum3[1]
                maximum3[1] = val
            elif val >= maximum3[2]:
                maximum3[2] = val
        mul = maximum3[0] * maximum3[1] * maximum3[2]
        print(mul)
