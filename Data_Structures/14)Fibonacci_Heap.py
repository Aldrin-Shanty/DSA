class Node:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.is_marked = False
        self.next = self
        self.prev = self

class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.total_nodes = 0

    def insert(self, key):
        new_node = Node(key)
        if self.min is None:
            self.min = new_node
        else:
            self._link(self.min, new_node)
            if key < self.min.key:
                self.min = new_node
        self.total_nodes += 1

    def find_min(self):
        return self.min.key if self.min else None

    def extract_min(self):
        min_node = self.min
        if min_node is not None:
            if min_node.child is not None:
                child = min_node.child
                while True:
                    next_child = child.next
                    self._link(self.min, child)
                    if next_child == min_node.child:
                        break
                    child = next_child

            self._remove(min_node)
            if min_node == min_node.next:
                self.min = None
            else:
                self.min = min_node.next
                self._consolidate()

            self.total_nodes -= 1
        return min_node.key if min_node else None

    def decrease_key(self, old_key, new_key):
        if old_key <= new_key:
            raise ValueError("New key must be less than the old key")

        node = self._find_node(self.min, old_key)
        if node is None:
            raise ValueError("Node with the old key not found")

        node.key = new_key
        parent = node.parent
        if parent and node.key < parent.key:
            self._cut(node, parent)
            self._cascading_cut(parent)

        if node.key < self.min.key:
            self.min = node

    def delete(self, key):
        self.decrease_key(key, float('-inf'))
        self.extract_min()

    def merge(self, other_heap):
        if self.min is None:
            self.min = other_heap.min
        elif other_heap.min is not None:
            self._link(self.min, other_heap.min)
            if other_heap.min.key < self.min.key:
                self.min = other_heap.min
        self.total_nodes += other_heap.total_nodes

    def _link(self, a, b):
        # Link node b to node a
        a_next = a.next
        a.next = b
        b.prev = a
        b.next = a_next
        a_next.prev = b

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if self.min == node:
            if node.next == node:
                self.min = None
            else:
                self.min = node.next

    def _consolidate(self):
        max_degree = int(self.total_nodes ** 0.5) + 1
        degree_table = [None] * (max_degree + 1)

        nodes = [node for node in self._iterate(self.min)]
        for node in nodes:
            degree = node.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node

                self._link(node, other)
                degree_table[degree] = None
                degree += 1
            degree_table[degree] = node

        self.min = None
        for node in degree_table:
            if node is not None:
                if self.min is None:
                    self.min = node
                elif node.key < self.min.key:
                    self.min = node

    def _cut(self, node, parent):
        # Remove node from parent
        if node.next == node:
            parent.child = None
        else:
            if parent.child == node:
                parent.child = node.next
        self._remove(node)
        parent.degree -= 1
        self._link(self.min, node)
        node.parent = None
        node.is_marked = False

    def _cascading_cut(self, node):
        parent = node.parent
        if parent is not None:
            if not node.is_marked:
                node.is_marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def _find_node(self, root, key):
        node = root
        if node is None:
            return None
        if node.key == key:
            return node
        for child in self._iterate(node.child):
            result = self._find_node(child, key)
            if result:
                return result
        return None

    def _iterate(self, start):
        if start is None:
            return
        node = start
        while True:
            yield node
            node = node.next
            if node == start:
                break

