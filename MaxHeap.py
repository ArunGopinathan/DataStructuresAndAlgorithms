class MaxHeap:
    def max_heapify(self, A, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(A) and A[left] > A[largest]:
            largest = left
        if right < len(A) and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)

    def build_max_heap(self,A):
        for i in range(len(A) // 2, -1, -1):
            self.max_heapify(A, i)

