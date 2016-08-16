N, C = map(int, input().split())
parent = [1] + list(map(int, input().split()))
color = list(map(int, input().split()))

for i in range(N):
    ans = -1
    if i == 0:
        print(ans, end=' ')
    else:
        c = color[i]
        pid = parent[i] - 1
        z = 0
        while pid != 0 or z != 2:
            # print(id)
            if color[pid] != c:
                pid = parent[pid] - 1
                if pid == 0:
                    z += 1
            elif color[pid] == c:
                ans = pid
                break

        if ans == -1:
            print(-1, end=' ')
        else:
            print(ans + 1, end=' ')
