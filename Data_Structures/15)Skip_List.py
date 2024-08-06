"""
A Skip List is a data structure that allows for fast search, insertion, and deletion operations 
in a probabilistic manner. It consists of multiple levels of linked lists where each level has a 
subset of elements from the level below it, allowing for efficient traversal.

Operations:
1. **Insert**: Inserts a new value into the Skip List, creating nodes at various levels based on a probabilistic function.
2. **Search**: Searches for a value in the Skip List and returns True if found, False otherwise.
3. **Delete**: Removes a value from the Skip List if it exists.
4. **Display**: Prints the elements of the Skip List at each level.

Time Complexity:
    - **Insert**: O(log n) expected, where n is the number of elements in the Skip List.
    - **Search**: O(log n) expected.
    - **Delete**: O(log n) expected.
    - **Display**: O(n), where n is the number of elements in the Skip List.

Applications:
    - Provides efficient search, insertion, and deletion operations with average-case logarithmic time complexity.
    - Useful in scenarios requiring fast access to elements and ordered data structures.
    - Often used in applications like databases and file systems where such operations are frequent.
"""

import random

class Node:
    """Represents a node in a Skip List.

    Attributes:
        value (int): The value of the node.
        forward (list[Node]): Forward pointers for the node at each level.
    """

    def __init__(self, value: int, level: int) -> None:
        """Initializes a node in the Skip List.

        Args:
            value (int): The value of the node.
            level (int): The level of the node in the Skip List.
        """
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    """Represents a Skip List data structure.

    Attributes:
        max_level (int): The maximum level of the Skip List.
        p (float): The probability factor used to determine the level of new nodes.
        header (Node): The header node of the Skip List.
        level (int): The current level of the Skip List.
    """

    def __init__(self, max_level: int, p: float) -> None:
        """Initializes an empty Skip List.

        Args:
            max_level (int): The maximum level of the Skip List.
            p (float): The probability factor used to determine the level of new nodes.
        """
        self.max_level = max_level
        self.p = p
        self.header = Node(-1, max_level)
        self.level = 0

    def _random_level(self) -> int:
        """Generates a random level for a new node based on probability p.

        Returns:
            int: The generated level for the new node.
        """
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, value: int) -> None:
        """Inserts a new value into the Skip List.

        Args:
            value (int): The value to be inserted.
        """
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if not current or current.value != value:
            new_level = self._random_level()
            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level

            new_node = Node(value, new_level)
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, value: int) -> bool:
        """Searches for a value in the Skip List.

        Args:
            value (int): The value to be searched.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current and current.value == value

    def delete(self, value: int) -> None:
        """Deletes a value from the Skip List.

        Args:
            value (int): The value to be deleted.
        """
        update = [None] * (self.max_level + 1)
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def display(self) -> None:
        """Displays the Skip List."""
        print("Skip List:")
        for i in range(self.level + 1):
            print(f"Level {i}: ", end="")
            node = self.header.forward[i]
            while node:
                print(node.value, end=" -> ")
                node = node.forward[i]
            print("None")

if __name__ == "__main__":
    # Create a Skip List with maximum level of 3 and probability factor of 0.5
    skip_list = SkipList(max_level=3, p=0.5)

    # Insert elements
    print("Inserting elements: 3, 6, 7, 9, 12, 19")
    for value in [3, 6, 7, 9, 12, 19]:
        skip_list.insert(value)
        skip_list.display()

    # Search for elements
    print("\nSearching for elements 3, 6, 15")
    for value in [3, 6, 15]:
        result = skip_list.search(value)
        print(f"Element {value} found: {result}")

    # Delete elements
    print("\nDeleting elements 3, 12, 19")
    for value in [3, 12, 19]:
        skip_list.delete(value)
        skip_list.display()

    # Search for deleted elements
    print("\nSearching for deleted elements 3, 12, 19")
    for value in [3, 12, 19]:
        result = skip_list.search(value)
        print(f"Element {value} found: {result}")

