"""
Heap Implementation using Python's `heapq` and manual heap implementations.

Heap Overview:
- A heap is a specialized tree-based data structure that satisfies the heap property.
- In a max-heap, the parent node is always greater than or equal to its children, while in a min-heap, the parent node is always less than or equal to its children.
- Operations are performed to maintain the heap property during insertions and deletions.

Heap Operations:
1. **Push**: Inserts an item into the heap while maintaining the heap property.
2. **Pop** : Removes and returns the root element of the heap (i.e., the maximum element in a max-heap or the minimum element in a min-heap).
3. **Peek**: Returns the root element of the heap without removing it.
4. **Heapify**: Converts an iterable into a heap, rearranging the elements to satisfy the heap property.
5. **Heap Transformations**:
       - **Max-Heap**: Uses negation to transform Python’s min-heap into a max-heap.
       - **Min-Heap**: Uses Python’s built-in `heapq` for a min-heap implementation
6. **Underlying Heap Implementations**:
       - **MaxHeap**: Implements a max-heap manually with basic operations like insertion, deletion, and heapify.
       - **MinHeap**: Implements a min-heap manually with basic operations like insertion, deletion, and heapify.

Heap Time Complexity:
    - **Insertion**: O(log n)
    - **Deletion** O(log n)
    - **Peek**: O(1)
    - **Heapify**: O(n), where n is the number of elements

Applications:
    - Heaps are used in priority queues, heap sort, and algorithms like Dijkstra's shortest path and Prim's minimum spanning tree.

"""

import heapq


class Heap:
    """
    A heap class that supports max-heaps and min-heaps using Python's `heapq` module.
    """

    def __init__(self, max_heap=False):
        """
        Initialize the heap.

        Args:
            max_heap (bool): If True, use max-heap; otherwise, use min-heap.
        """
        self.heap = []
        self.max_heap = max_heap

    def _transform(self, item):
        """
        Transform the item based on heap type.

        Args:
            item (int): The item to be transformed.

        Returns:
            int: Transformed item for max-heap or min-heap.
        """
        return -item if self.max_heap else item

    def push(self, item):
        """
        Insert an item into the heap.

        Args:
            item (int): The item to be inserted.

        Returns:
            None
        """
        heapq.heappush(self.heap, self._transform(item))

    def pop(self):
        """
        Remove and return the root element of the heap.

        Returns:
            int: The root element of the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("pop from an empty heap")
        return -heapq.heappop(self.heap) if self.max_heap else heapq.heappop(self.heap)

    def peek(self):
        """
        Return the root element of the heap without removing it.

        Returns:
            int: The root element of the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("peek from an empty heap")
        return -self.heap[0] if self.max_heap else self.heap[0]

    def heapify(self, iterable):
        """
        Convert an iterable into a heap.

        Args:
            iterable (iterable): An iterable containing elements to be heapified.

        Returns:
            None
        """
        self.heap = [self._transform(x) for x in iterable]
        heapq.heapify(self.heap)

    def __len__(self):
        """
        Return the number of elements in the heap.

        Returns:
            int: The number of elements in the heap.
        """
        return len(self.heap)

    def __str__(self):
        """
        Return a string representation of the heap.

        Returns:
            str: The string representation of the heap.
        """
        return str([-x for x in self.heap]) if self.max_heap else str(self.heap)


class MaxHeap:
    """
    A manual implementation of a max-heap.
    """

    def __init__(self):
        """
        Initialize the max-heap.
        """
        self.arr = []

    def heapify(self, arr, n, i):
        """
        Rearrange the elements to maintain the max-heap property.

        Args:
            arr (list): The list of elements to heapify.
            n (int): The size of the heap.
            i (int): The index to be heapified.

        Returns:
            None
        """
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
        """
        Insert a new number into the max-heap.

        Args:
            newNum (int): The number to be inserted.

        Returns:
            None
        """
        self.arr.append(newNum)
        size = len(self.arr)
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(self.arr, size, i)

    def deleteNode(self, num):
        """
        Delete a number from the max-heap.

        Args:
            num (int): The number to be deleted.

        Returns:
            None
        """
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
        """
        Return the maximum element from the max-heap.

        Returns:
            int: The maximum element.

        Notes:
            Returns None if the heap is empty.
        """
        return self.arr[0] if self.arr else None

    def printHeap(self):
        """
        Print the elements of the max-heap.

        Returns:
            None
        """
        print(self.arr)


class MinHeap:
    """
    A manual implementation of a min-heap.
    """

    def __init__(self):
        """
        Initialize the min-heap.
        """
        self.arr = []

    def heapify(self, arr, n, i):
        """
        Rearrange the elements to maintain the min-heap property.

        Args:
            arr (list): The list of elements to heapify.
            n (int): The size of the heap.
            i (int): The index to be heapified.

        Returns:
            None
        """
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
        """
        Insert a new number into the min-heap.

        Args:
            newNum (int): The number to be inserted.

        Returns:
            None
        """
        self.arr.append(newNum)
        size = len(self.arr)
        for i in range((size // 2) - 1, -1, -1):
            self.heapify(self.arr, size, i)

    def deleteNode(self, num):
        """
        Delete a number from the min-heap.

        Args:
            num (int): The number to be deleted.

        Returns:
            None
        """
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
        """
        Return the minimum element from the min-heap.

        Returns:
            int: The minimum element.

        Notes:
            Returns None if the heap is empty.
        """
        return self.arr[0] if self.arr else None

    def printHeap(self):
        """
        Print the elements of the min-heap.

        Returns:
            None
        """
        print(self.arr)


# Example usage
if __name__ == "__main__":
    print("Testing Python Heap:")
    py_heap = Heap(max_heap=True)
    py_heap.push(3)
    py_heap.push(1)
    py_heap.push(5)
    print(f"Heap after pushes: {py_heap}")
    print(f"Peek: {py_heap.peek()}")
    print(f"Pop: {py_heap.pop()}")
    print(f"Heap after pop: {py_heap}")

    print("\nTesting MaxHeap:")
    max_heap = MaxHeap()
    max_heap.insert(3)
    max_heap.insert(1)
    max_heap.insert(5)
    max_heap.printHeap()
    print(f"Max: {max_heap.getMax()}")
    max_heap.deleteNode(5)
    max_heap.printHeap()

    print("\nTesting MinHeap:")
    min_heap = MinHeap()
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(5)
    min_heap.printHeap()
    print(f"Min: {min_heap.getMin()}")
    min_heap.deleteNode(1)
    min_heap.printHeap()
