"""
A Red-Black Tree is a balanced binary search tree where each node has an additional color attribute (red or black). 
It maintains balance by ensuring that certain properties are satisfied during insertions and deletions.

Operations:
1. **Search**: Searches for a node with the given key in the subtree rooted at `node`.
2. **Insert**: Inserts a new node with the given key into the Red-Black Tree and maintains tree properties.
3. **Delete**: Deletes a node with the given key from the Red-Black Tree and maintains tree properties.
4. **Minimum**: Returns the node with the minimum key in the subtree rooted at `node`.
5. **Maximum**: Returns the node with the maximum key in the subtree rooted at `node`.
6. **Inorder Traversal**: Performs an in-order traversal of the Red-Black Tree and prints node keys.
7. **Preorder Traversal**: Performs a pre-order traversal of the Red-Black Tree and prints node keys.
8. **Postorder Traversal**: Performs a post-order traversal of the Red-Black Tree and prints node keys.

Time Complexity:    
- **Search**: O(log n), where n is the number of nodes in the tree.
- **Insert**: O(log n), where n is the number of nodes in the tree.
- **Delete**: O(log n), where n is the number of nodes in the tree.
- **Minimum**: O(log n), where n is the number of nodes in the tree.
- **Maximum**: O(log n), where n is the number of nodes in the tree.
- **Traversal**: O(n), where n is the number of nodes in the tree.

Applications:
    - Maintaining a balanced tree structure for efficient search, insertion, and deletion operations.
    - Used in database indexing and memory management systems.
    - Supports efficient set operations such as union, intersection, and difference.
"""

class Node:
    """Represents a node in the Red-Black Tree.

    Attributes:
        key (int): The key value of the node.
        color (str): The color of the node, either 'RED' or 'BLACK'.
        left (Node): Pointer to the left child.
        right (Node): Pointer to the right child.
        parent (Node): Pointer to the parent node.
    """

    def __init__(self, key: int, color: str = 'RED') -> None:
        """Initializes a new node with the given key and color.

        Args:
            key (int): The key value of the node.
            color (str): The color of the node, either 'RED' or 'BLACK'. Default is 'RED'.
        """
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    """Represents a Red-Black Tree.

    Attributes:
        TNULL (Node): Sentinel NIL node representing the end of the tree.
        root (Node): The root node of the Red-Black Tree.
    """

    def __init__(self) -> None:
        """Initializes an empty Red-Black Tree with a sentinel NIL node."""
        self.TNULL = Node(0, color='BLACK')
        self.root = self.TNULL

    def search_tree(self, node: Node, key: int) -> Node:
        """Searches for a node with the given key in the subtree rooted at `node`.

        Args:
            node (Node): The starting node for the search.
            key (int): The key to search for.

        Returns:
            Node: The node with the given key if found, otherwise the NIL node.
        """
        if node == self.TNULL or key == node.key:
            return node

        if key < node.key:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

    def insert(self, key: int) -> None:
        """Inserts a new node with the given key into the Red-Black Tree and maintains tree properties.

        Args:
            key (int): The key of the new node to be inserted.
        """
        node = Node(key)
        node.parent = None
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'RED'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 'BLACK'
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k: Node) -> None:
        """Fixes any violations of Red-Black Tree properties after an insertion.

        Args:
            k (Node): The newly inserted node.
        """
        while k.parent.color == 'RED':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'RED':
                    k.parent.color = 'BLACK'
                    u.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 'RED':
                    k.parent.color = 'BLACK'
                    u.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'BLACK'
                    k.parent.parent.color = 'RED'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'BLACK'

    def left_rotate(self, x: Node) -> None:
        """Performs a left rotation around the given node `x` to maintain tree balance.

        Args:
            x (Node): The node around which to perform the left rotation.
        """
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x: Node) -> None:
        """Performs a right rotation around the given node `x` to maintain tree balance.

        Args:
            x (Node): The node around which to perform the right rotation.
        """
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def delete_node(self, key: int) -> None:
        """Deletes a node with the given key from the Red-Black Tree and maintains tree properties.

        Args:
            key (int): The key of the node to be deleted.
        """
        self.delete_node_helper(self.root, key)

    def delete_node_helper(self, node: Node, key: int) -> None:
        """Helper function to find and delete a node with the given key, then fix any violations.

        Args:
            node (Node): The root node of the subtree.
            key (int): The key of the node to be deleted.
        """
        z = self.TNULL
        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'BLACK':
            self.fix_delete(x)

    def fix_delete(self, x: Node) -> None:
        """Fixes any violations of Red-Black Tree properties after a deletion.

        Args:
            x (Node): The node that caused the violation.
        """
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def transplant(self, u: Node, v: Node) -> None:
        """Replaces the subtree rooted at `u` with the subtree rooted at `v`, used during deletion.

        Args:
            u (Node): The node to be replaced.
            v (Node): The node to replace `u`.
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node: Node) -> Node:
        """Returns the node with the minimum key in the subtree rooted at `node`.

        Args:
            node (Node): The root of the subtree.

        Returns:
            Node: The node with the minimum key.
        """
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node: Node) -> Node:
        """Returns the node with the maximum key in the subtree rooted at `node`.

        Args:
            node (Node): The root of the subtree.

        Returns:
            Node: The node with the maximum key.
        """
        while node.right != self.TNULL:
            node = node.right
        return node

    def inorder_helper(self, node: Node) -> None:
        """Helper function to perform an in-order traversal of the subtree rooted at `node`.

        Args:
            node (Node): The root of the subtree.
        """
        if node != self.TNULL:
            self.inorder_helper(node.left)
            print(node.key, end=' ')
            self.inorder_helper(node.right)

    def inorder_traversal(self) -> None:
        """Performs an in-order traversal of the Red-Black Tree and prints node keys."""
        self.inorder_helper(self.root)
        print()

    def preorder_helper(self, node: Node) -> None:
        """Helper function to perform a pre-order traversal of the subtree rooted at `node`.

        Args:
            node (Node): The root of the subtree.
        """
        if node != self.TNULL:
            print(node.key, end=' ')
            self.preorder_helper(node.left)
            self.preorder_helper(node.right)

    def preorder_traversal(self) -> None:
        """Performs a pre-order traversal of the Red-Black Tree and prints node keys."""
        self.preorder_helper(self.root)
        print()

    def postorder_helper(self, node: Node) -> None:
        """Helper function to perform a post-order traversal of the subtree rooted at `node`.

        Args:
            node (Node): The root of the subtree.
        """
        if node != self.TNULL:
            self.postorder_helper(node.left)
            self.postorder_helper(node.right)
            print(node.key, end=' ')

    def postorder_traversal(self) -> None:
        """Performs a post-order traversal of the Red-Black Tree and prints node keys."""
        self.postorder_helper(self.root)
        print()


if __name__ == "__main__":
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(15)
    
    print("In-order traversal of the Red-Black Tree:")
    rbt.inorder_traversal()

    print("Pre-order traversal of the Red-Black Tree:")
    rbt.preorder_traversal()

    print("Post-order traversal of the Red-Black Tree:")
    rbt.postorder_traversal()

    rbt.delete_node(20)
    print("In-order traversal after deleting 20:")
    rbt.inorder_traversal()
