"""
Adelson-Velsky and Landis Tree (AVL Tree) Implementation

An AVL Tree (Adelson-Velsky and Landis Tree) is a self-balancing binary search tree.
In an AVL Tree, the heights of the two child subtrees of any node differ by at most one,
and this balance condition must be preserved after every insertion and deletion operation.

AVL Tree Operations:
1. **Insert**: Inserts a key into the AVL Tree while maintaining the AVL balance property.
2. **Search**: Searches for a key in the AVL Tree and returns True if the key is found, otherwise False.
3. **Delete**: Deletes a key from the AVL Tree and maintains the AVL balance property.
4. **Inorder Traversal**: Returns a list of elements in the AVL Tree in ascending order.
5. **Preorder Traversal**: Returns a list of elements in the AVL Tree following a preorder traversal (root, left, right).
6. **Postorder Traversal**: Returns a list of elements in the AVL Tree following a postorder traversal (left, right, root).

Time Complexity:
    - **Insertion**: O(log n), where n is the number of nodes in the tree.
    - **Deletion**: O(log n), where n is the number of nodes in the tree.
    - **Search**: O(log n), where n is the number of nodes in the tree.
    - **Traversal**: O(n), where n is the number of nodes in the tree.

Applications:
    - AVL Trees are used in situations where frequent insertions and deletions are performed
        and quick search, insertion, and deletion operations are needed.
    - They are useful in implementing associative arrays, priority queues, and other data structures
        where balanced search performance is required.

"""
class TreeNode:
    """
    A node in the AVL Tree.

    Attributes:
        value (int): The value of the node.
        left (TreeNode): The left child of the node.
        right (TreeNode): The right child of the node.
        height (int): The height of the node.
    """

    def __init__(self, key: int) -> None:
        """
        Initialize a new TreeNode with the given key.

        Args:
            key (int): The value to be stored in the node.
        """
        self.left = None
        self.right = None
        self.value = key
        self.height = 1  # New nodes are initially at height 1

class AVLTree:
    """
    Adelson-Velsky and Landis Tree (AVL Tree) Implementation

    Attributes:
        root (TreeNode): The root node of the BST.
    """

    def __init__(self) -> None:
        """
        Initialize an empty AVL Tree.
        """
        self.root = None

    def insert(self, key: int) -> None:
        """
        Insert a key into the AVL Tree.

        Args:
            key (int): The value to be inserted into the AVL Tree.

        Returns:
            None
        """
        self.root = self._insert(self.root, key)

    def _insert(self, node: TreeNode, key: int) -> TreeNode:
        """
        Helper method to insert a key into the AVL Tree starting from the given node.

        Args:
            node (TreeNode): The root node of the subtree.
            key (int): The value to be inserted into the subtree.

        Returns:
            TreeNode: The updated node.
        """
        if not node:
            return TreeNode(key)
        
        if key < node.value:
            node.left = self._insert(node.left, key)
        elif key > node.value:
            node.right = self._insert(node.right, key)
        else:
            return node
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance = self._get_balance(node)
        
        if balance > 1:
            if key < node.left.value:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        
        if balance < -1:
            if key > node.right.value:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
        
        return node

    def _left_rotate(self, z: TreeNode) -> TreeNode:
        """
        Perform a left rotation.

        Args:
            z (TreeNode): The node to rotate.

        Returns:
            TreeNode: The new root of the rotated subtree.
        """
        y = z.right
        T2 = y.left
        
        y.left = z
        z.right = T2
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y

    def _right_rotate(self, z: TreeNode) -> TreeNode:
        """
        Perform a right rotation.

        Args:
            z (TreeNode): The node to rotate.

        Returns:
            TreeNode: The new root of the rotated subtree.
        """
        y = z.left
        T3 = y.right
        
        y.right = z
        z.left = T3
        
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        
        return y

    def _get_height(self, node: TreeNode) -> int:
        """
        Get the height of a node.

        Args:
            node (TreeNode): The node to check.

        Returns:
            int: The height of the node.
        """
        if not node:
            return 0
        return node.height

    def _get_balance(self, node: TreeNode) -> int:
        """
        Get the balance factor of a node.

        Args:
            node (TreeNode): The node to check.

        Returns:
            int: The balance factor of the node.
        """
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def search(self, key: int) -> bool:
        """
        Search for a key in the AVL Tree.

        Args:
            key (int): The value to search for.

        Returns:
            bool: True if the key is found, otherwise False.
        """
        return self._search(self.root, key)

    def _search(self, node: TreeNode, key: int) -> bool:
        """
        Helper method to search for a key in the AVL Tree starting from the given node.

        Args:
            node (TreeNode): The root node of the subtree.
            key (int): The value to search for in the subtree.

        Returns:
            bool: True if the key is found, otherwise False.
        """
        if not node:
            return False
        if key < node.value:
            return self._search(node.left, key)
        elif key > node.value:
            return self._search(node.right, key)
        else:
            return True

    def delete(self, key: int) -> None:
        """
        Delete a key from the AVL Tree.

        Args:
            key (int): The value to be deleted from the AVL Tree.

        Returns:
            None
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node: TreeNode, key: int) -> TreeNode:
        """
        Helper method to delete a key from the AVL Tree starting from the given node.

        Args:
            node (TreeNode): The root node of the subtree.
            key (int): The value to be deleted from the subtree.

        Returns:
            TreeNode: The updated node.
        """
        if not node:
            return node
        
        if key < node.value:
            node.left = self._delete(node.left, key)
        elif key > node.value:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            temp = self._get_min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)
        
        if not node:
            return node
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance = self._get_balance(node)
        
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._right_rotate(node)
            else:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)
        
        if balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._left_rotate(node)
            else:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)
        
        return node

    def _get_min_value_node(self, node: TreeNode) -> TreeNode:
        """
        Get the node with the minimum value greater than the given node.

        Args:
            node (TreeNode): The node to start from.

        Returns:
            TreeNode: The node with the minimum value.
        """
        current = node
        while current.left:
            current = current.left
        return current

    def inorder_traversal(self) -> list[int]:
        """
        Perform an inorder traversal of the AVL Tree.

        Returns:
            list[int]: A list of values in the AVL Tree in ascending order.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node: TreeNode, result: list[int]) -> None:
        """
        Helper method for inorder traversal of the AVL Tree.

        Args:
            node (TreeNode): The root node of the subtree.
            result (list[int]): The list to store the traversal result.

        Returns:
            None
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.value)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self) -> list[int]:
        """
        Perform a preorder traversal of the AVL Tree.

        Returns:
            list[int]: A list of values in the AVL Tree following preorder traversal.
        """
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node: TreeNode, result: list[int]) -> None:
        """
        Helper method for preorder traversal of the AVL Tree.

        Args:
            node (TreeNode): The root node of the subtree.
            result (list[int]): The list to store the traversal result.

        Returns:
            None
        """
        if node:
            result.append(node.value)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self) -> list[int]:
        """
        Perform a postorder traversal of the AVL Tree.

        Returns:
            list[int]: A list of values in the AVL Tree following postorder traversal.
        """
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node: TreeNode, result: list[int]) -> None:
        """
        Helper method for postorder traversal of the AVL Tree.

        Args:
            node (TreeNode): The root node of the subtree.
            result (list[int]): The list to store the traversal result.

        Returns:
            None
        """
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.value)

if __name__ == "__main__":
    # Create an AVL Tree instance
    avl = AVLTree()
    
    # Insert elements
    print("Inserting elements:")
    elements = [10, 20, 30, 40, 50, 25]
    for elem in elements:
        avl.insert(elem)
        print(f"Inserted {elem}")
    
    # Print traversals
    print("\nInorder Traversal:")
    print(avl.inorder_traversal())  # Expected: [10, 20, 25, 30, 40, 50]

    print("\nPreorder Traversal:")
    print(avl.preorder_traversal())

    print("\nPostorder Traversal:")
    print(avl.postorder_traversal())

    # Search for elements
    print("\nSearching for elements:")
    search_keys = [25, 15]
    for key in search_keys:
        found = avl.search(key)
        print(f"Search for {key}: {'Found' if found else 'Not Found'}")

    # Delete elements
    print("\nDeleting elements:")
    delete_keys = [40, 50, 25]
    for key in delete_keys:
        avl.delete(key)
        print(f"Deleted {key}")

    # Print traversals after deletions
    print("\nInorder Traversal after deletions:")
    print(avl.inorder_traversal())