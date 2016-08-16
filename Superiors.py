from collections import deque

#bfs
def calculate(tree):
    queue = deque(tree[0])
    handshakes = fistbumps = nodes = level = 0
    while queue:
        for _ in range(len(queue)):
            root = queue.popleft()
            handshakes += level
            fistbumps += nodes - level
            nodes += 1
            queue.extend(tree[root])
        level += 1
    return handshakes, fistbumps


t = int(input())
for _ in range(t):
    n = int(input())
    superiors = [int(v) for v in input().strip().split(' ')]
    tree = {i: [] for i in range(n+1)}
    [tree[s].append(i + 1) for i, s in enumerate(superiors)]
    handshakes, fistbumps = calculate(tree)
    print(handshakes, fistbumps)
