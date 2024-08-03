"""
A Fenwick Tree (or Binary Indexed Tree) is a data structure that provides efficient methods for 
querying prefix sums and updating elements in an array.

Operations:
1. **Initialization**: Builds the Fenwick Tree from an array.
2. **Prefix Sum Query**: Computes the sum of elements from the start of the array to a given index.
3. **Range Sum Query**: Computes the sum of elements between two indices.
4. **Update**: Adds a value to an element at a specific index.
5. **Set**: Sets the value at a specific index to a new value.

Time Complexity:
- **Initialization**: O(n log n), where n is the number of elements in the array.
- **Prefix Sum Query**: O(log n).
- **Range Sum Query**: O(log n).
- **Update**: O(log n).
- **Set**: O(log n).

Applications:
- Efficiently performing range sum queries and updates in dynamic arrays.
- Used in algorithms for computational geometry, binary search, and dynamic programming.
- Suitable for scenarios where frequent updates and prefix sum queries are required.
"""

class Fenwick_Tree:
    """
    A Fenwick Tree (Binary Indexed Tree) for efficient prefix sum and update operations.

    Attributes:
        tree (list[int]): The internal list representing the Fenwick Tree.
        len (int): The length of the Fenwick Tree.
    """
    
    def __init__(self, arr: list[int] = []):
        """
        Initialize a Fenwick Tree with the given array.

        Args:
            arr (list[int], optional): The initial array to build the Fenwick Tree. Defaults to an empty list.
        """
        self.tree = [i for i in arr]
        self.len = len(self.tree)
        for i in range(1, self.len):
            j = i + (i & -i)
            if j < self.len:
                self.tree[j] += self.tree[i]

    def prefixsum(self, index: int) -> int:
        """
        Compute the prefix sum from the start of the array to the given index.

        Args:
            index (int): The index up to which the prefix sum is computed.

        Returns:
            int: The prefix sum from the start of the array to the given index.
        """
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def sum(self, left: int, right: int) -> int:
        """
        Compute the sum of elements between two indices, inclusive.

        Args:
            left (int): The starting index of the range (inclusive).
            right (int): The ending index of the range (inclusive).

        Returns:
            int: The sum of elements from index `left` to index `right`.
        """
        return self.prefixsum(right) - self.prefixsum(left - 1)

    def add(self, index: int, value: int) -> None:
        """
        Add a value to the element at the given index.

        Args:
            index (int): The index of the element to be updated.
            value (int): The value to be added to the element at the given index.

        Returns:
            None
        """
        while index < self.len:
            self.tree[index] += value
            index += index & -index

    def set(self, index: int, value: int) -> None:
        """
        Set the value of the element at the given index to the specified value.

        Args:
            index (int): The index of the element to be set.
            value (int): The new value to set at the given index.

        Returns:
            None
        """
        k = self.sum(index, index)
        self.add(index, value - k)

if __name__=="__main__":
    # Initialize Fenwick Tree with an array
    fenwick_tree = Fenwick_Tree([1, 3, 5, 7, 9, 11])
    
    # Query the prefix sum up to index 4
    print(fenwick_tree.prefixsum(4))  # Output: 16
    
    # Query the sum of elements between indices 2 and 5
    print(fenwick_tree.sum(2, 5))  # Output: 22
    
    # Add 5 to the element at index 3
    fenwick_tree.add(3, 5)
    
    # Set the element at index 2 to 10
    fenwick_tree.set(2, 10)