"""
This module implements a stack data structure using a list.

Time Complexity:
- Push operation: O(1)
- Pop operation: O(1)
- Check if empty operation: O(1)
- Display operation: O(n)
- Size operation: O(1)

Applications:
Stacks are used in various applications such as function call management, expression evaluation, backtracking algorithms, and undo mechanisms in applications.
"""

class Stack:
    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.stack = []

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def push(self, item) -> None:
        """
        Pushes an item onto the stack.

        Args:
            item: The item to be added to the stack.

        Returns:
            None
        """
        self.stack.append(item)

    def pop(self):
        """
        Pops an item from the stack.

        Returns:
            The item removed from the stack, or a message indicating that the stack is empty if no items are present.
        """
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def display(self) -> None:
        """
        Displays the elements of the stack.

        Returns:
            None
        """
        print(self.stack)

    def size(self) -> int:
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.stack)

# Sample Test Cases

if __name__ == "__main__":
    stack = Stack()

    # Test is_empty on an empty stack
    print("Is the stack empty?", stack.is_empty())  # Expected: True

    # Push items onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Display stack contents
    print("Stack after pushes:")
    stack.display()  # Expected: [10, 20, 30]

    # Pop items from the stack
    print("Popped item:", stack.pop())  # Expected: 30
    print("Popped item:", stack.pop())  # Expected: 20
    print("Popped item:", stack.pop())  # Expected: 10
    print("Popped item:", stack.pop())  # Expected: Stack is empty

    # Check size of the stack
    print("Size of stack:", stack.size())  # Expected: 0

    # Push more items and display size
    stack.push(40)
    stack.push(50)
    print("Size of stack after more pushes:", stack.size())  # Expected: 2
    print("Stack contents:")
    stack.display()  # Expected: [40, 50]