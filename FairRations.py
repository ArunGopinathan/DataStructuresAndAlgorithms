N = int(input().strip())
B = list(map(int, input().strip().split(' ')))
steps = 0
if sum(B) % 2:
    print('NO')
else:
    for j in range(len(B) - 1):
        if B[j] % 2:
            B[j + 1] = B[j + 1] + 1
            steps += 2
    print(steps)
