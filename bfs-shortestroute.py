from collections import deque
import sys

t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    tree = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        x, y = map(int, input().strip().split())
        if y not in tree[x]:
            tree[x].append(y)
    s = int(input())
    visited = [-1] * (n + 1)
    queue = deque(tree[s])
    visited[s] = 6
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            visited[node] = 6
            queue.extend(tree[node])
    del (visited[0])
    del (visited[s])
    print(' '.join(map(str, visited)))
