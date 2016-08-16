def max_heapify(A, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(A) and A[left] > A[largest]:
        largest = left
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)


def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapify(A, i)


n = int(input())
arr = []
count = {}
for _ in range(n):
    line = input()
    if ' ' in line:
        cmd, num = map(int, line.split(' '))
        if cmd == 1:
            count[num] = count.get(num, 0) + 1
            arr.append(num)
            build_max_heap(arr)
        elif cmd == 2:
            if num in count and count[num] > 0:
                count[num] -= 1
            else:
                print("-1")

    else:
        cmd = int(line)
        if cmd == 3:
            if len(arr) > 0:
                print(arr[0])  # max heap is faster
        if cmd == 4:
            print(min(arr))
