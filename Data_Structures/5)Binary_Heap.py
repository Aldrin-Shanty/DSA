'''
Heap Operations are: push,pop,peek,heapify
'''

import heapq


class Heap:
    def __init__(self, max_heap=False):
        self.heap = []
        self.max_heap = max_heap  # Boolean flag to determine if it's a max-heap

    def _transform(self, item):
        return -item if self.max_heap else item

    def push(self, item):
        heapq.heappush(self.heap, self._transform(item))

    def pop(self):
        if not self.heap:
            raise IndexError("pop from an empty heap")
        return -heapq.heappop(self.heap) if self.max_heap else heapq.heappop(self.heap)

    def peek(self):
        if not self.heap:
            raise IndexError("peek from an empty heap")
        return -self.heap[0] if self.max_heap else self.heap[0]

    def heapify(self, iterable):
        self.heap = [self._transform(x) for x in iterable]
        heapq.heapify(self.heap)

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str([-x for x in self.heap]) if self.max_heap else str(self.heap)


# Below are heap implemented manually
'''
class MaxHeap:
    def __init__(self):
        self.arr = []

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def insert(self, newNum):
        self.arr.append(newNum)
        size = len(self.arr)
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(self.arr, size, i)

    def deleteNode(self, num):
        size = len(self.arr)
        i = 0
        for i in range(size):
            if num == self.arr[i]:
                break

        self.arr[i], self.arr[size - 1] = self.arr[size - 1], self.arr[i]
        self.arr.pop()

        for i in range((len(self.arr) // 2) - 1, -1, -1):
            self.heapify(self.arr, len(self.arr), i)

    def getMax(self):
        return self.arr[0] if self.arr else None

    def printHeap(self):
        print(self.arr)

class MinHeap:
    def __init__(self):
        self.arr = []

    def heapify(self, arr, n, i):
        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] > arr[l]:
            smallest = l

        if r < n and arr[smallest] > arr[r]:
            smallest = r

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)

    def insert(self, newNum):
        self.arr.append(newNum)
        size = len(self.arr)
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(self.arr, size, i)

    def deleteNode(self, num):
        size = len(self.arr)
        i = 0
        for i in range(size):
            if num == self.arr[i]:
                break

        self.arr[i], self.arr[size - 1] = self.arr[size - 1], self.arr[i]
        self.arr.pop()

        for i in range((len(self.arr) // 2) - 1, -1, -1):
            self.heapify(self.arr, len(self.arr), i)

    def getMin(self):
        return self.arr[0] if self.arr else None

    def printHeap(self):
        print(self.arr)
'''
