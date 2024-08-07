"""
Queue Data Structure

This module implements a basic queue using a Python list. A queue is a linear data structure that follows the First In, First Out (FIFO) principle.

Operations:
1. **Enqueue**: Adds an element to the rear of the queue. This operation involves appending the element to the end of the list.
2. **Dequeue**: Removes an element from the front of the queue. This operation involves removing the element at the start of the list and requires shifting all remaining elements.
3. **Display**: Shows all elements in the queue from front to rear. This operation involves traversing the entire list to present its contents.
4. **Size**: Returns the number of elements currently in the queue. This operation retrieves the length of the list.
5. **Is Empty**: Checks if the queue is empty. This operation verifies whether the list is empty.

Time Complexity:
    - **Enqueue**: O(1) (constant time as it involves appending an element to the end of the list)
    - **Dequeue**: O(n) (linear time as it involves removing the first element and shifting all remaining elements)
    - **Display**: O(n) (linear time as it requires traversing the entire list to show its contents)
    - **Size**: O(1) (constant time as it retrieves the length of the list)
    - **Is Empty**: O(1) (constant time as it checks if the list is empty)

Applications:
    - Queues are used in scenarios such as scheduling tasks, handling requests in web servers, and breadth-first search algorithms.
"""


from collections import deque


class Queue:
    def __init__(self):
        """Initializes an empty queue."""
        self.queue = []

    def enqueue(self, item: any) -> None:
        """
        Adds an item to the end of the queue.

        Args:
            item (any): The item to be added to the queue.

        Returns:
            None
        """
        self.queue.append(item)

    def dequeue(self) -> any:
        """
        Removes the item from the front of the queue.

        Returns:
            any: The item that was removed from the queue. If the queue is empty, returns a message "Queue is empty".
        """
        if len(self.queue) < 1:
            return "Queue is empty"
        return self.queue.pop(0)

    def display(self) -> None:
        """
        Displays the items in the queue.

        Returns:
            None
        """
        print(self.queue)

    def size(self) -> int:
        """
        Returns the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self.queue)

    def is_empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0


"""
Deque Data Structure using collections.deque

This module implements a deque using the collections.deque class. A deque (double-ended queue) allows insertion and deletion of items from both ends efficiently.

Time Complexity:
- `append_left`: O(1)
- `append_right`: O(1)
- `pop_left`: O(1)
- `pop_right`: O(1)
- `peek_left`: O(1)
- `peek_right`: O(1)
- `is_empty`: O(1)
- `size`: O(1)

Applications:
Deques are used in scenarios such as implementing a queue with both ends accessible, maintaining history in applications, and managing buffer data.
"""


class Deque:
    def __init__(self):
        """Initializes an empty deque."""
        self.queue = deque()

    def append_left(self, item: any) -> None:
        """
        Adds an item to the front of the deque.

        Args:
            item (any): The item to be added to the front of the deque.

        Returns:
            None
        """
        self.queue.appendleft(item)

    def append_right(self, item: any) -> None:
        """
        Adds an item to the end of the deque.

        Args:
            item (any): The item to be added to the end of the deque.

        Returns:
            None
        """
        self.queue.append(item)

    def pop_left(self) -> any:
        """
        Removes the item from the front of the deque.

        Returns:
            any: The item that was removed from the front of the deque. If the deque is empty, returns None.
        """
        if self.queue:
            return self.queue.popleft()
        else:
            print("Deque is empty, cannot pop from the front.")
            return None

    def pop_right(self) -> any:
        """
        Removes the item from the end of the deque.

        Returns:
            any: The item that was removed from the end of the deque. If the deque is empty, returns None.
        """
        if self.queue:
            return self.queue.pop()
        else:
            print("Deque is empty, cannot pop from the end.")
            return None

    def peek_left(self) -> any:
        """
        Retrieves the item from the front of the deque without removing it.

        Returns:
            any: The item at the front of the deque. If the deque is empty, returns None.
        """
        if self.queue:
            return self.queue[0]
        else:
            print("Deque is empty, no front item.")
            return None

    def peek_right(self) -> any:
        """
        Retrieves the item from the end of the deque without removing it.

        Returns:
            any: The item at the end of the deque. If the deque is empty, returns None.
        """
        if self.queue:
            return self.queue[-1]
        else:
            print("Deque is empty, no end item.")
            return None

    def is_empty(self) -> bool:
        """
        Checks if the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return len(self.queue) == 0

    def size(self) -> int:
        """
        Returns the number of items in the deque.

        Returns:
            int: The number of items in the deque.
        """
        return len(self.queue)

    def display(self) -> None:
        """
        Displays the items in the deque.

        Returns:
            None
        """
        print(self.queue)


"""
Circular Queue Data Structure using collections.deque

This module implements a circular queue using the collections.deque class. A circular queue efficiently manages elements in a fixed-size buffer by reusing space.

Time Complexity:
- `enqueue`: O(1)
- `dequeue`: O(1)
- `display`: O(n)
- `is_empty`: O(1)
- `size`: O(1)

Applications:
Circular queues are used in scenarios such as buffer management in circular buffers, implementing round-robin scheduling algorithms, and managing resources with fixed capacities.
"""


class CircularQueue:
    def __init__(self, size: int):
        """
        Initializes a circular queue with a fixed size.

        Args:
            size (int): The maximum number of items the circular queue can hold.

        Returns:
            None
        """
        self.max_size = size  # Renamed to avoid conflict
        self.queue = deque(maxlen=size)

    def enqueue(self, data: any) -> None:
        """
        Adds an item to the end of the circular queue.

        Args:
            data (any): The item to be added to the queue.

        Returns:
            None
        """
        self.queue.append(data)  # O(1) operation

    def dequeue(self) -> any:
        """
        Removes the item from the front of the circular queue.

        Returns:
            any: The item that was removed from the front of the queue. If the queue is empty, prints a message and returns None.
        """
        if not self.queue:
            print("Queue is empty")
            return None
        return self.queue.popleft()  # O(1) operation

    def display(self) -> None:
        """
        Displays the items in the circular queue.

        Returns:
            None
        """
        if not self.queue:
            print("Queue is empty")
        else:
            print("Queue elements:", list(self.queue))

    def is_empty(self) -> bool:
        """
        Checks if the circular queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def size(self) -> int:
        """
        Returns the number of items in the circular queue.

        Returns:
            int: The number of items in the circular queue.
        """
        return len(self.queue)


# Test cases for Queue
if __name__ == "__main__":
    # Queue Test
    q = Queue()
    print("Queue operations:")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue after enqueuing 1, 2, 3:")
    q.display()  # Expected output: [1, 2, 3]
    print("Dequeue operation:")
    print(q.dequeue())  # Expected output: 1
    print("Queue after dequeuing:")
    q.display()  # Expected output: [2, 3]
    print("Is the queue empty?")
    print(q.is_empty())  # Expected output: False
    print("Size of the queue:")
    print(q.size())  # Expected output: 2

    # Deque Test
    dq = Deque()
    print("\nDeque operations:")
    dq.append_left(1)
    dq.append_right(2)
    dq.append_left(0)
    print("Deque after operations:")
    dq.display()  # Expected output: deque([0, 1, 2])
    print("Pop left operation:")
    print(dq.pop_left())  # Expected output: 0
    print("Pop right operation:")
    print(dq.pop_right())  # Expected output: 2
    print("Peek left operation:")
    print(dq.peek_left())  # Expected output: 1
    print("Peek right operation:")
    print(dq.peek_right())  # Expected output: 1
    print("Is the deque empty?")
    print(dq.is_empty())  # Expected output: False
    print("Size of the deque:")
    print(dq.size())  # Expected output: 1

    # Circular Queue Test
    cq = CircularQueue(size=3)
    print("\nCircular Queue operations:")
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print("Circular Queue after enqueuing 1, 2, 3:")
    cq.display()  # Expected output: [1, 2, 3]
    cq.enqueue(4)  # This should overwrite the oldest item (1)
    print("Circular Queue after enqueuing 4:")
    cq.display()  # Expected output: [2, 3, 4]
    print("Dequeue operation:")
    print(cq.dequeue())  # Expected output: 2
    print("Circular Queue after dequeuing:")
    cq.display()  # Expected output: [3, 4]
    print("Is the circular queue empty?")
    print(cq.is_empty())  # Expected output: False
    print("Size of the circular queue:")
    print(cq.size())  # Expected output: 2
