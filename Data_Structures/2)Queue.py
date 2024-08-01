'''
Queue Operations : enqueue, dequeue, display, size, is_empty
Deque(collections) Operations : append_left, append_right, popleft, popright, peek_left, peek_right, is_empty, size
Circular Queue(collections.deque implementation): enqueue, dequeue, display, size, is_empty
'''
from collections import deque


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

    def is_empty(self):
        empty = len(self.queue) == 0
        return empty

# Just use deque from collections module instead of implementing deque using list as it will make insertion take O(n) time.


class Deque:
    def __init__(self):
        self.queue = deque()

    def append_left(self, item):
        self.queue.appendleft(item)

    def append_right(self, item):
        self.queue.append(item)

    def pop_left(self):
        if self.queue:
            item = self.queue.popleft()
            return item
        else:
            print("Deque is empty, cannot pop from the front.")
            return None

    def pop_right(self):
        if self.queue:
            item = self.queue.pop()
            return item
        else:
            print("Deque is empty, cannot pop from the end.")
            return None

    def peek_left(self):
        if self.queue:
            item = self.queue[0]
            return item
        else:
            print("Deque is empty, no front item.")
            return None

    def peek_right(self):
        if self.queue:
            item = self.queue[-1]
            return item
        else:
            print("Deque is empty, no end item.")
            return None

    def is_empty(self):
        empty = len(self.queue) == 0
        return empty

    def size(self):
        size = len(self.queue)
        return size


# Below docstring has deque using lists
'''
class Deque(Queue):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()
'''

# CircularQueue implemented using lists are inefficient as it will take O(n) for insertion at front, to make the  structure more efficient,
# we can implement it on deque structure from collections module
# By setting deque maxlen , we are basically making it a circulare queue, the class below is just a decoration over the deque strucutre from collections module.


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = deque(maxlen=size)

    def enqueue(self, data):
        self.queue.append(data)  # O(1) operation

    def dequeue(self):
        if not self.queue:
            print("Queue is empty")
        else:
            return self.queue.popleft()  # O(1) operation

    def display(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Queue elements:", list(self.queue))

    def is_empty(self):
        empty = len(self.queue) == 0
        return empty

    def size(self):
        size = len(self.queue)
        return size


# Below docstring has circular queue using lists
'''
class CircularQueue(Queue):

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def display(self):
        if (self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
'''
