"""
A Segment Tree is a data structure used for efficiently answering range queries and updating elements in an array. It is particularly useful for scenarios where multiple queries and updates are required on an array of data.

Operations:
1. **Initialization**: Constructs the segment tree from the given array. 
    The build operation initializes the tree with the values from the array and computes internal nodes based on the sum of child nodes.
2. **Update**: Modifies the value of a specific element in the array and updates the segment tree to reflect this change. 
    The update operation affects only the nodes that correspond to the updated element.
3. **Query**: Retrieves the aggregate information (such as the sum) for a given range of elements in the array. 
    This operation efficiently computes the result by merging information from relevant segments of the tree.

Time Complexity:
    - **Initialization**: O(n), where n is the number of elements in the array.
    - **Update**: O(log n)
    - **Query**: O(log n)

Applications:
    -  **Range Queries**: Efficiently calculates sums, minimums, maximums, or other aggregate functions over a specified range in an array.
    - **Point Updates**: Allows updates to individual elements while maintaining the ability to query ranges efficiently.
    - **Interval Problems**: Useful for problems that involve querying and updating intervals or segments, such as finding the sum of elements in a range or updating specific values.

The Segment Tree is well-suited for scenarios where both updates and queries are frequent, and where direct array manipulations would be too slow or cumbersome. It provides a balanced approach to manage dynamic data with optimal time complexities for both updates and queries.
"""

class SegmentTree:
    """
    A Segment Tree data structure for efficient range queries and updates.

    Attributes:
        n (int): The number of elements in the original array.
        tree (list[int]): The segment tree stored as a list.
    """

    def __init__(self, data: list[int]):
        """
        Initialize the Segment Tree with the given data.

        Args:
            data (list[int]): The initial data to build the segment tree from.
        """
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data: list[int]) -> None:
        """
        Build the segment tree from the given data.

        Args:
            data (list[int]): The initial data to build the segment tree from.

        Returns:
            None
        """
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, value: int) -> None:
        """
        Update the value at the specified index in the segment tree.

        Args:
            index (int): The index of the element to be updated.
            value (int): The new value to be set at the specified index.

        Returns:
            None
        """
        pos = self.n + index
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]

    def query(self, left: int, right: int) -> int:
        """
        Query the sum of elements in the range [left, right).

        Args:
            left (int): The starting index of the range (inclusive).
            right (int): The ending index of the range (exclusive).

        Returns:
            int: The sum of elements in the specified range.
        """
        result = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                result += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result

if __name__ == "__main__":
    # Initialize data
    data = [1, 3, 5, 7, 9, 11]

    # Create Segment Tree
    seg_tree = SegmentTree(data)

    # Print the segment tree
    print("Initial Segment Tree:", seg_tree.tree)

    # Perform and print range queries
    print("Query range (1, 4):", seg_tree.query(1, 4))  # Expected output: 15 (3 + 5 + 7)

    # Update an element and print the segment tree
    seg_tree.update(2, 10)  # Update index 2 to value 10
    print("Segment Tree after update:", seg_tree.tree)

    # Perform and print range queries after update
    print("Query range (1, 4) after update:", seg_tree.query(1, 4))  # Expected output: 22 (3 + 10 + 7)