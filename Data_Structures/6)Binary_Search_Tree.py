"""
    Binary Search Tree (BST) Implementation

The Binary Search Tree (BST) is a data structure that stores elements in a sorted manner, allowing for efficient searching, insertion, and deletion operations.
Each node in the BST has at most two children, with the left child having a smaller value and the right child having a larger value.

BST Operations:
1. **insert(key)**:
   - Inserts a key into the BST while maintaining the BST property.

2. **search(key)**:
   - Searches for a key in the BST and returns True if the key is found, otherwise False.

3. **delete(key)**:
   - Deletes a key from the BST and maintains the BST property.

4. **inorder_traversal()**:
   - Returns a list of elements in the BST in ascending order.

5. **preorder_traversal()**:
   - Returns a list of elements in the BST following a preorder traversal (root, left, right).

6. **postorder_traversal()**:
   - Returns a list of elements in the BST following a postorder traversal (left, right, root).

Time Complexity:
- **Insertion**: O(h), where h is the height of the tree. In the average case, it's O(log n), but in the worst case (unbalanced tree), it's O(n).
- **Search**: O(h), where h is the height of the tree. In the average case, it's O(log n), but in the worst case (unbalanced tree), it's O(n).
- **Deletion**: O(h), where h is the height of the tree. In the average case, it's O(log n), but in the worst case (unbalanced tree), it's O(n).
- **Traversal**: O(n), where n is the number of nodes in the tree.

Applications:
- BSTs are used in various applications such as efficient searching, sorting, and maintaining ordered collections of data.

"""

class TreeNode:
    """
    A node in the Binary Search Tree.

    Attributes:
        value (int): The value of the node.
        left (TreeNode): The left child of the node.
        right (TreeNode): The right child of the node.
    """

    def __init__(self, key: int):
        """
        Initialize a new TreeNode with the given key.

        Args:
            key (int): The value to be stored in the node.
        """
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    """
    A Binary Search Tree (BST) implementation.

    Attributes:
        root (TreeNode): The root node of the BST.
    """

    def __init__(self):
        """
        Initialize an empty Binary Search Tree.
        """
        self.root = None

    def insert(self, key: int) -> None:
        """
        Insert a key into the BST.

        Args:
            key (int): The value to be inserted into the BST.

        Returns:
            None
        """
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root: TreeNode, key: int) -> None:
        """
        Helper method to insert a key into the BST starting from the given root.

        Args:
            root (TreeNode): The root node of the subtree.
            key (int): The value to be inserted into the subtree.

        Returns:
            None
        """
        if key < root.value:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = TreeNode(key)
            else:
                self._insert(root.right, key)

    def search(self, key: int) -> bool:
        """
        Search for a key in the BST.

        Args:
            key (int): The value to search for.

        Returns:
            bool: True if the key is found, otherwise False.
        """
        return self._search(self.root, key)

    def _search(self, root: TreeNode, key: int) -> bool:
        """
        Helper method to search for a key in the BST starting from the given root.

        Args:
            root (TreeNode): The root node of the subtree.
            key (int): The value to search for in the subtree.

        Returns:
            bool: True if the key is found, otherwise False.
        """
        if root is None or root.value == key:
            return root is not None
        if key < root.value:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key: int) -> None:
        """
        Delete a key from the BST.

        Args:
            key (int): The value to be deleted from the BST.

        Returns:
            None
        """
        self.root = self._delete(self.root, key)

    def _delete(self, root: TreeNode, key: int) -> TreeNode:
        """
        Helper method to delete a key from the BST starting from the given root.

        Args:
            root (TreeNode): The root node of the subtree.
            key (int): The value to be deleted from the subtree.

        Returns:
            TreeNode: The new root of the subtree after deletion.
        """
        if root is None:
            return root
        if key < root.value:
            root.left = self._delete(root.left, key)
        elif key > root.value:
            root.right = self._delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor
            min_larger_node = self._min_value_node(root.right)
            root.value = min_larger_node.value
            root.right = self._delete(root.right, min_larger_node.value)

        return root

    def _min_value_node(self, node: TreeNode) -> TreeNode:
        """
        Get the node with the smallest value greater than the given node.

        Args:
            node (TreeNode): The node to start from.

        Returns:
            TreeNode: The node with the smallest value.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self) -> list[int]:
        """
        Perform an inorder traversal of the BST.

        Returns:
            list[int]: A list of values in the BST in ascending order.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root: TreeNode, result: list[int]) -> None:
        """
        Helper method for inorder traversal of the BST.

        Args:
            root (TreeNode): The root node of the subtree.
            result (list[int]): The list to store the traversal result.

        Returns:
            None
        """
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.value)
            self._inorder_traversal(root.right, result)

    def preorder_traversal(self) -> list[int]:
        """
        Perform a preorder traversal of the BST.

        Returns:
            list[int]: A list of values in the BST following preorder traversal.
        """
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, root: TreeNode, result: list[int]) -> None:
        """
        Helper method for preorder traversal of the BST.

        Args:
            root (TreeNode): The root node of the subtree.
            result (list[int]): The list to store the traversal result.

        Returns:
            None
        """
        if root:
            result.append(root.value)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)

    def postorder_traversal(self) -> list[int]:
        """
        Perform a postorder traversal of the BST.

        Returns:
            list[int]: A list of values in the BST following postorder traversal.
        """
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, root: TreeNode, result: list[int]) -> None:
        """
        Helper method for postorder traversal of the BST.

        Args:
            root (TreeNode): The root node of the subtree.
            result (list[int]): The list to store the traversal result.

        Returns:
            None
        """
        if root:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.value)

if __name__ == "__main__":
    # Create a Binary Search Tree instance
    bst = BinarySearchTree()

    # Insert elements
    print("Inserting elements:")
    elements = [10, 5, 20, 3, 7, 15, 25]
    for elem in elements:
        bst.insert(elem)
        print(f"Inserted {elem}")

    # Print inorder traversal (should be sorted)
    print("\nInorder Traversal:")
    print(bst.inorder_traversal())  # Expected: [3, 5, 7, 10, 15, 20, 25]

    # Print preorder traversal
    print("\nPreorder Traversal:")
    print(bst.preorder_traversal())  # Expected: [10, 5, 3, 7, 20, 15, 25]

    # Print postorder traversal
    print("\nPostorder Traversal:")
    print(bst.postorder_traversal())  # Expected: [3, 7, 5, 15, 25, 20, 10]

    # Search for elements
    print("\nSearching for elements:")
    search_keys = [7, 30]
    for key in search_keys:
        found = bst.search(key)
        print(f"Search for {key}: {'Found' if found else 'Not Found'}")

    # Delete elements
    print("\nDeleting elements:")
    delete_keys = [5, 20, 10]
    for key in delete_keys:
        bst.delete(key)
        print(f"Deleted {key}")

    # Print inorder traversal after deletions
    print("\nInorder Traversal after deletions:")
    print(bst.inorder_traversal())  # Expected to be updated based on deletions