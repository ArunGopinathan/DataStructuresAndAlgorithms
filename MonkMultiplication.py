def max_heapify(a, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(a) and a[left] > a[largest]:
        largest = left
    if right < len(a) and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)
    return a


def build_max_heap(a):
    for i in range(len(a) // 2, -1, -1):
        a = max_heapify(a, i)
    return a

h = []
n = int(input())
items = [int(x) for x in input().split(' ')]
for item in items:
    h.append(item)
    h = build_max_heap(h)
