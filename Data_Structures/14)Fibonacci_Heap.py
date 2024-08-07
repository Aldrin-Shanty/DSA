"""
Represents a Fibonacci Heap data structure.

Operations:
1. **Insert**: Inserts a new node with the given key into the heap.
2. **Find Minimum**: Finds and returns the minimum key in the heap.
3. **Extract Minimum**: Extracts and returns the minimum key from the heap.
4. **Decrease Key**: Decreases the key of a node in the heap.
5. **Delete**: Deletes a node with the specified key from the heap.
6. **Merge**: Merges another Fibonacci Heap into this heap.

Time Complexity:
- **Insert**: O(1) - Inserting a new node into the heap is constant time.
- **Find Minimum**: O(1) - Finding the minimum node is constant time.
- **Extract Minimum**: O(log n) - Extracting the minimum node requires consolidation and takes logarithmic time in the number of nodes.
- **Decrease Key**: O(1) - Decreasing a key involves adjusting nodes and may trigger cascading cuts, which is amortized constant time.
- **Delete**: O(log n) - Deleting a node is performed by decreasing its key to negative infinity and then extracting the minimum.
- **Merge**: O(1) - Merging two heaps is constant time.

Space Complexity:
- The space complexity is O(n), where 'n' is the number of nodes in the heap, due to the storage required for nodes and their relationships.

Applications:
- Fibonacci Heaps are used in algorithms requiring a priority queue where decrease-key operations are frequent, such as Dijkstra's shortest path algorithm and Prim's minimum spanning tree algorithm.
- Useful in scenarios where amortized time efficiency for decrease-key operations is crucial.
"""
class Node:
    """Represents a node in a Fibonacci Heap.

    Attributes:
        key (int): The key of the node.
        degree (int): The degree of the node (number of children).
        parent (Node): The parent of the node.
        child (Node): The child node.
        is_marked (bool): Whether the node is marked.
        next (Node): The next node in the circular doubly linked list.
        prev (Node): The previous node in the circular doubly linked list.
    """

    def __init__(self, key: int):
        """Initializes a new node with the given key."""

        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.is_marked = False
        self.next = self
        self.prev = self


class FibonacciHeap:
    """Represents a Fibonacci Heap data structure.

    Attributes:
        min (Node): The minimum node in the heap.
        total_nodes (int): The total number of nodes in the heap.
    """

    def __init__(self):
        """Initializes an empty Fibonacci Heap."""
        self.min = None
        self.total_nodes = 0

    def insert(self, key: int) -> None:
        """Inserts a new node with the given key into the heap.

        Args:
            key (int): The key to be inserted.
        """
        new_node = Node(key)
        if self.min is None:
            self.min = new_node
        else:
            self._link_nodes(self.min, new_node)
            if key < self.min.key:
                self.min = new_node
        self.total_nodes += 1

    def find_min(self) -> int:
        """Finds the minimum key in the heap.

        Returns:
            int: The minimum key in the heap, or None if the heap is empty.
        """
        return self.min.key if self.min else None

    def extract_min(self) -> int:
        """Extracts and returns the minimum key from the heap.

        Returns:
            int: The minimum key that was removed, or None if the heap is empty.
        """
        min_node = self.min
        if min_node is not None:
            if min_node.child is not None:
                children = [x for x in self._iterate(min_node.child)]
                for child in children:
                    self._link_nodes(min_node, child)
                    child.parent = None

            self._remove_node(min_node)
            if min_node == min_node.next:
                self.min = None
            else:
                self.min = min_node.next
                self._consolidate()

            self.total_nodes -= 1
        return min_node.key if min_node else None

    def decrease_key(self, old_key: int, new_key: int) -> None:
        """Decreases the key of a node in the heap.

        Args:
            old_key (int): The current key of the node to decrease.
            new_key (int): The new key to set, must be less than the old key.

        Raises:
            ValueError: If new_key is not less than old_key or if node with old_key is not found.
        """
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

    def delete(self, key: int) -> None:
        """Deletes a node with the specified key from the heap.

        Args:
            key (int): The key of the node to delete.
        """
        self.decrease_key(key, float('-inf'))
        self.extract_min()

    def merge(self, other_heap: 'FibonacciHeap') -> None:
        """Merges another Fibonacci Heap into this heap.

        Args:
            other_heap (FibonacciHeap): The heap to merge with this heap.
        """
        if self.min is None:
            self.min = other_heap.min
        elif other_heap.min is not None:
            self._link_nodes(self.min, other_heap.min)
            if other_heap.min.key < self.min.key:
                self.min = other_heap.min
        self.total_nodes += other_heap.total_nodes

    def _link_nodes(self, a: Node, b: Node) -> None:
        """Links node b to node a.

        Args:
            a (Node): The node to link to.
            b (Node): The node to be linked.
        """
        b.prev = a
        b.next = a.next
        a.next.prev = b
        a.next = b

    def _remove_node(self, node: Node) -> None:
        """Removes a node from the heap.

        Args:
            node (Node): The node to remove.
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def _consolidate(self) -> None:
        """Consolidates trees of the same degree in the heap."""
        max_degree = int(self.total_nodes ** 0.5) + 1
        degree_table = [None] * (max_degree + 1)

        nodes = [x for x in self._iterate(self.min)]
        for node in nodes:
            degree = node.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node

                self._link_tree(node, other)
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

    def _link_tree(self, parent: Node, child: Node) -> None:
        """Links two trees of the same degree.

        Args:
            parent (Node): The parent node.
            child (Node): The child node to be linked.
        """
        self._remove_node(child)
        child.next = child
        child.prev = child
        if parent.child is None:
            parent.child = child
        else:
            self._link_nodes(parent.child, child)
        child.parent = parent
        parent.degree += 1
        child.is_marked = False

    def _cut(self, node: Node, parent: Node) -> None:
        """Cuts a node from its parent and adds it to the root list.

        Args:
            node (Node): The node to cut.
            parent (Node): The parent node from which the node will be cut.
        """
        if node.next == node:
            parent.child = None
        else:
            if parent.child == node:
                parent.child = node.next
        self._remove_node(node)
        parent.degree -= 1
        self._link_nodes(self.min, node)
        node.parent = None
        node.is_marked = False

    def _cascading_cut(self, node: Node) -> None:
        """Performs a cascading cut on a node.

        Args:
            node (Node): The node to perform the cascading cut on.
        """
        parent = node.parent
        if parent is not None:
            if not node.is_marked:
                node.is_marked = True
            else:
                self._cut(node, parent)
                self._cascading_cut(parent)

    def _find_node(self, root: Node, key: int) -> Node:
        """Finds a node with the given key in the subtree.

        Args:
            root (Node): The root of the subtree to search.
            key (int): The key of the node to find.

        Returns:
            Node: The node with the given key, or None if not found.
        """
        for node in self._iterate(root):
            if node.key == key:
                return node
            if node.child:
                result = self._find_node(node.child, key)
                if result:
                    return result
        return None

    def _iterate(self, start: Node):
        """Iterates over the circular doubly linked list starting from a node.

        Args:
            start (Node): The starting node for iteration.

        Yields:
            Node: The nodes in the circular doubly linked list.
        """
        if start is None:
            return
        node = start
        while True:
            yield node
            node = node.next
            if node == start:
                break


if __name__=="__main__":
    # Create a new Fibonacci Heap
    heap = FibonacciHeap()

    # Insert elements into the heap
    print("Inserting elements 3, 5, 7, 2, 8 into the heap...")
    heap.insert(3)
    heap.insert(5)
    heap.insert(7)
    heap.insert(2)
    heap.insert(8)

    # Find the minimum element
    print(f"Minimum element in the heap: {heap.find_min()}")  # Expected output: 2

    # Extract the minimum element
    print(f"Extracting the minimum element: {heap.extract_min()}")  # Expected output: 2
    print(f"Minimum element after extraction: {heap.find_min()}")  # Expected output: 3

    # Decrease key of a node
    print("Decreasing key from 7 to 1...")
    heap.decrease_key(7, 1)
    print(f"Minimum element after decreasing key: {heap.find_min()}")  # Expected output: 1

    # Delete a node
    print("Deleting node with key 1...")
    heap.delete(1)
    print(f"Minimum element after deletion: {heap.find_min()}")  # Expected output: 3

    # Create another Fibonacci Heap and merge it
    other_heap = FibonacciHeap()
    other_heap.insert(10)
    other_heap.insert(4)
    other_heap.insert(6)

    print("Merging another heap with elements 10, 4, 6...")
    heap.merge(other_heap)
    print(f"Minimum element after merging: {heap.find_min()}")  # Expected output: 3

    # Extract minimums from the merged heap
    print(f"Extracting the minimum element: {heap.extract_min()}")  # Expected output: 3
    print(f"Minimum element after extraction: {heap.find_min()}")  # Expected output: 4