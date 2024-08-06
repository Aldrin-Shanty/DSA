"""
A B+ Tree is a balanced tree data structure that maintains sorted data and allows for efficient insertion, deletion, and search operations. 
It is a type of self-balancing tree with all values stored in leaf nodes and internal nodes only storing keys.

Operations:
1. **Search**: Searches for the key 'k' in the B+ Tree. Returns True if the key is present, otherwise False.
2. **Insert**: Inserts a new key 'k' into the B+ Tree, splitting nodes as necessary.
3. **Delete**: Deletes the key 'k' from the B+ Tree, merging nodes if necessary.
4. **Traverse**: Traverses and prints all keys in the B+ Tree in sorted order.

Time Complexity:
    - **Search**: O(log n) on average, where 'n' is the number of keys in the B+ Tree.
    - **Insertion**: O(log n) on average, due to the need to maintain balance and split nodes.
    - **Deletion**: O(log n) on average, as it may require node merging and rebalancing.

Applications:
    - Used in databases and file systems to maintain large datasets with efficient search, insert, and delete operations.
    - Commonly used for indexing in database management systems (DBMS) due to its ability to handle large amounts of data with balanced access times.
"""

class BPlusTreeNode:
    """Represents a node in a B+ Tree.

    Attributes:
        t (int): Minimum degree of the B+ Tree.
        leaf (bool): True if the node is a leaf node, False otherwise.
        keys (list[int]): List of keys in the node.
        children (list[BPlusTreeNode]): List of child BPlusTreeNodes.
        next (BPlusTreeNode, optional): Pointer to the next leaf node in the linked list of leaves.
    """

    def __init__(self, t: int, leaf: bool = False) -> None:
        """Initializes a BPlusTreeNode.

        Args:
            t (int): Minimum degree of the B+ Tree.
            leaf (bool, optional): True if the node is a leaf node. Defaults to False.
        """
        self.t = t
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.next = None

class BPlusTree:
    """Represents a B+ Tree data structure.

    Attributes:
        root (BPlusTreeNode): The root node of the B+ Tree.
        t (int): Minimum degree of the B+ Tree.
    """

    def __init__(self, t: int) -> None:
        """Initializes an empty B+ Tree.

        Args:
            t (int): Minimum degree of the B+ Tree.
        """
        self.root = BPlusTreeNode(t, True)
        self.t = t

    def search(self, k: int, x: BPlusTreeNode = None) -> bool:
        """Searches for a key in the B+ Tree.

        Args:
            k (int): The key to search for.
            x (BPlusTreeNode, optional): The node to start the search from. Defaults to None.

        Returns:
            bool: True if the key is found, False otherwise.
        """
        if x is None:
            x = self.root

        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and x.keys[i] == k:
            if x.leaf:
                return True
            else:
                return self.search(k, x.children[i])

        if x.leaf:
            return False

        return self.search(k, x.children[i])

    def insert(self, k: int) -> None:
        """Inserts a key into the B+ Tree.

        Args:
            k (int): The key to be inserted.
        """
        root = self.root
        if len(root.keys) == (2 * self.t - 1):
            s = BPlusTreeNode(self.t, False)
            self.root = s
            s.children.append(root)
            self.split_child(s, 0)
            self.insert_non_full(s, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x: BPlusTreeNode, k: int) -> None:
        """Inserts a key into a node that is not full.

        Args:
            x (BPlusTreeNode): The node to insert the key into.
            k (int): The key to be inserted.
        """
        if x.leaf:
            i = len(x.keys) - 1
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            i = len(x.keys) - 1
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t - 1):
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def split_child(self, x: BPlusTreeNode, i: int) -> None:
        """Splits a child of a given node.

        Args:
            x (BPlusTreeNode): The node to split the child from.
            i (int): The index of the child to be split.
        """
        t = self.t
        y = x.children[i]
        z = BPlusTreeNode(t, y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t - 1)]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.children = y.children[t: (2 * t)]

        if y.leaf:
            z.next = y.next
            y.next = z

    def delete(self, k: int) -> None:
        """Deletes a key from the B+ Tree.

        Args:
            k (int): The key to be deleted.
        """
        self.delete_node(self.root, k)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def delete_node(self, x: BPlusTreeNode, k: int) -> None:
        """Deletes a key from a node.

        Args:
            x (BPlusTreeNode): The node to delete the key from.
            k (int): The key to be deleted.
        """
        t = self.t
        idx = self.find_key(x, k)
        if idx < len(x.keys) and x.keys[idx] == k:
            if x.leaf:
                x.keys.pop(idx)
            else:
                self.delete_internal_node(x, idx)
        else:
            if x.leaf:
                return
            flag = (idx == len(x.keys))
            if len(x.children[idx].keys) < t:
                self.fill(x, idx)
            if flag and idx > len(x.keys):
                self.delete_node(x.children[idx - 1], k)
            else:
                self.delete_node(x.children[idx], k)

    def delete_internal_node(self, x: BPlusTreeNode, idx: int) -> None:
        """Handles deletion from an internal node.

        Args:
            x (BPlusTreeNode): The node from which to delete the key.
            idx (int): The index of the key to be deleted.
        """
        t = self.t
        k = x.keys[idx]
        if len(x.children[idx].keys) >= t:
            pred = self.get_predecessor(x, idx)
            x.keys[idx] = pred
            self.delete_node(x.children[idx], pred)
        elif len(x.children[idx + 1].keys) >= t:
            succ = self.get_successor(x, idx)
            x.keys[idx] = succ
            self.delete_node(x.children[idx + 1], succ)
        else:
            self.merge(x, idx)
            self.delete_node(x.children[idx], k)

    def get_predecessor(self, x: BPlusTreeNode, idx: int) -> int:
        """Finds the predecessor of a key in a non-leaf node.

        Args:
            x (BPlusTreeNode): The node containing the key.
            idx (int): The index of the key whose predecessor is to be found.

        Returns:
            int: The predecessor key.
        """
        cur = x.children[idx]
        while not cur.leaf:
            cur = cur.children[-1]
        return cur.keys[-1]

    def get_successor(self, x: BPlusTreeNode, idx: int) -> int:
        """Finds the successor of a key in a non-leaf node.

        Args:
            x (BPlusTreeNode): The node containing the key.
            idx (int): The index of the key whose successor is to be found.

        Returns:
            int: The successor key.
        """
        cur = x.children[idx + 1]
        while not cur.leaf:
            cur = cur.children[0]
        return cur.keys[0]

    def fill(self, x: BPlusTreeNode, idx: int) -> None:
        """Fills a node if it has fewer than t keys.

        Args:
            x (BPlusTreeNode): The parent node of the node to be filled.
            idx (int): The index of the child node to be filled.
        """
        t = self.t
        if idx != 0 and len(x.children[idx - 1].keys) >= t:
            self.borrow_from_prev(x, idx)
        elif idx != len(x.keys) and len(x.children[idx + 1].keys) >= t:
            self.borrow_from_next(x, idx)
        else:
            if idx != len(x.keys):
                self.merge(x, idx)
            else:
                self.merge(x, idx - 1)

    def borrow_from_prev(self, x: BPlusTreeNode, idx: int) -> None:
        """Borrows a key from the previous sibling.

        Args:
            x (BPlusTreeNode): The parent node.
            idx (int): The index of the child node.
        """
        t = self.t
        child = x.children[idx]
        sibling = x.children[idx - 1]
        child.keys.insert(0, x.keys[idx - 1])
        x.keys[idx - 1] = sibling.keys.pop()
        if not child.leaf:
            child.children.insert(0, sibling.children.pop())

    def borrow_from_next(self, x: BPlusTreeNode, idx: int) -> None:
        """Borrows a key from the next sibling.

        Args:
            x (BPlusTreeNode): The parent node.
            idx (int): The index of the child node.
        """
        t = self.t
        child = x.children[idx]
        sibling = x.children[idx + 1]
        child.keys.append(x.keys[idx])
        x.keys[idx] = sibling.keys.pop(0)
        if not child.leaf:
            child.children.append(sibling.children.pop(0))

    def merge(self, x: BPlusTreeNode, idx: int) -> None:
        """Merges a child with its sibling.

        Args:
            x (BPlusTreeNode): The parent node.
            idx (int): The index of the child node to be merged.
        """
        t = self.t
        child = x.children[idx]
        sibling = x.children[idx + 1]
        child.keys.append(x.keys[idx])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.children.extend(sibling.children)
        x.keys.pop(idx)
        x.children.pop(idx + 1)

    def find_key(self, x: BPlusTreeNode, k: int) -> int:
        """Finds the index of the first key greater than or equal to k.

        Args:
            x (BPlusTreeNode): The node to search in.
            k (int): The key to find.

        Returns:
            int: The index of the key.
        """
        idx = 0
        while idx < len(x.keys) and x.keys[idx] < k:
            idx += 1
        return idx

    def traverse(self) -> None:
        """Traverses the B+ Tree and prints keys."""
        def _traverse(node: BPlusTreeNode) -> None:
            """Helper function to recursively traverse nodes.

            Args:
                node (BPlusTreeNode): The node to start the traversal from.
            """
            if node:
                if node.leaf:
                    for key in node.keys:
                        print(key, end=" ")
                    print()
                else:
                    i = 0
                    while i < len(node.keys):
                        _traverse(node.children[i])
                        print(node.keys[i], end=" ")
                        i += 1
                    _traverse(node.children[i])

        _traverse(self.root)
        print()

if __name__=="__main__":
    bplustree = BPlusTree(t=2)  # Minimum degree t=2
    keys = [10, 20, 5, 6, 15, 30, 25, 40, 50, 35, 45]
    
    for key in keys:
        bplustree.insert(key)

    print("B+ Tree traversal:")
    bplustree.traverse()  # Should print keys in sorted order
    print("Search 15:", bplustree.search(15))  # Should print: True
    print("Search 100:", bplustree.search(100))  # Should print: False