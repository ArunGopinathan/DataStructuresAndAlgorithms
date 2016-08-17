import heapq

n = int(input())
heap = [int(x) for x in input().strip().split(' ')]
t = int(input())
heapq.heapify(heap)
for _ in range(t):
    line = input().strip()
    if ' ' in line:
        line = line.split(' ')
        heapq.heappush(heap, int(line[1]))
    else:
        heapq.heappop(heap)
print(heapq.nlargest(1, heap)[0])
