"""
Singly Linked List (SLL)

A singly linked list is a linear data structure where each element points to the next element in the sequence. 
Each node in a singly linked list contains a data field and a reference to the next node.

Time Complexity:
- Insertion at the beginning: O(1)
- Insertion at the end: O(n) (because traversal is required)
- Insertion after a node: O(1) (if the node is given)
- Deletion: O(n) (because traversal is required)
- Search: O(n) (linear search)
- Sorting: O(n^2) (using bubble sort)
- Reversing: O(n)

Applications:
- Used to implement stacks and queues
- Useful for memory-efficient implementations where elements are frequently inserted or removed
- Ideal for scenarios where dynamic memory allocation is required

"""

class Single_Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data: int) -> None:
        """
        Insert a new node with data at the beginning of the list.

        Args:
            new_data (int): The data to be inserted.

        Returns:
            None
        """
        new_node = Single_Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node: Single_Node, new_data: int) -> None:
        """
        Insert a new node with data after a given node.

        Args:
            prev_node (Single_Node): The node after which the new node will be inserted.
            new_data (int): The data to be inserted.

        Returns:
            None
        """
        if prev_node is None:
            print("The given previous node must be in the linked list.")
            return
        new_node = Single_Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAtEnd(self, new_data: int) -> None:
        """
        Insert a new node with data at the end of the list.

        Args:
            new_data (int): The data to be inserted.

        Returns:
            None
        """
        new_node = Single_Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def deleteNode(self, position: int) -> None:
        """
        Delete a node at a given position.

        Args:
            position (int): The position of the node to be deleted (0-based index).

        Returns:
            None
        """
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                return
        if temp is None or temp.next is None:
            return
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def search(self, key: int) -> bool:
        """
        Search for a node with the given data.

        Args:
            key (int): The data to search for.

        Returns:
            bool: True if the node with the given data is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def sortLinkedList(self) -> None:
        """
        Sort the linked list using bubble sort.

        Returns:
            None
        """
        if self.head is None:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def printList(self) -> None:
        """
        Print the linked list.

        Returns:
            None
        """
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end="")
            temp = temp.next
        print()

    def reverseList(self) -> None:
        """
        Reverse the linked list.

        Returns:
            None
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

"""
Doubly Linked List (DLL)

A doubly linked list is a linear data structure where each node contains a reference to both the next and the previous node in the sequence. This allows for bidirectional traversal.

Time Complexity:
- Insertion at the beginning: O(1)
- Insertion at the end: O(n) (because traversal is required)
- Insertion after a node: O(1) (if the node is given)
- Deletion: O(n) (because traversal is required)
- Search: O(n) (linear search)
- Sorting: O(n^2) (using bubble sort)
- Reversing: O(n)

Applications:
- Used in implementing advanced data structures like doubly linked trees
- Useful for applications requiring bidirectional traversal
- Ideal for scenarios where nodes are frequently inserted or removed from both ends

"""

class Double_Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data: int) -> None:
        """
        Insert a new node with data at the beginning of the list.

        Args:
            new_data (int): The data to be inserted.

        Returns:
            None
        """
        new_node = Double_Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node: Double_Node, new_data: int) -> None:
        """
        Insert a new node with data after a given node.

        Args:
            prev_node (Double_Node): The node after which the new node will be inserted.
            new_data (int): The data to be inserted.

        Returns:
            None
        """
        if prev_node is None:
            print("The given previous node must be in the linked list.")
            return
        new_node = Double_Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def insertAtEnd(self, new_data: int) -> None:
        """
        Insert a new node with data at the end of the list.

        Args:
            new_data (int): The data to be inserted.

        Returns:
            None
        """
        new_node = Double_Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def deleteNode(self, position: int) -> None:
        """
        Delete a node at a given position.

        Args:
            position (int): The position of the node to be deleted (0-based index).

        Returns:
            None
        """
        if self.head is None:
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            temp = None
            return
        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                return
        if temp is None or temp.next is None:
            return
        next_node = temp.next.next
        if next_node is not None:
            next_node.prev = temp
        temp.next = None
        temp.next = next_node

    def search(self, key: int) -> bool:
        """
        Search for a node with the given data.

        Args:
            key (int): The data to search for.

        Returns:
            bool: True if the node with the given data is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def sortLinkedList(self) -> None:
        """
        Sort the linked list using bubble sort.

        Returns:
            None
        """
        if self.head is None:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def printList(self) -> None:
        """
        Print the linked list.

        Returns:
            None
        """
        temp = self.head
        while temp:
            print(str(temp.data) + " ", end="")
            temp = temp.next
        print()

    def reverseList(self) -> None:
        """
        Reverse the doubly linked list.

        Returns:
            None
        """
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.head = temp.prev

if __name__ == "__main__":
    # Test SinglyLinkedList
    sll = SinglyLinkedList()

    print("Testing SinglyLinkedList:")
    
    # Insert at the beginning
    sll.insertAtBeginning(3)
    sll.insertAtBeginning(2)
    sll.insertAtBeginning(1)
    print("List after inserting at beginning:")
    sll.printList()  # Expected output: 1 2 3

    # Insert at the end
    sll.insertAtEnd(4)
    sll.insertAtEnd(5)
    print("List after inserting at end:")
    sll.printList()  # Expected output: 1 2 3 4 5

    # Insert after a node
    second_node = sll.head.next
    sll.insertAfter(second_node, 2.5)
    print("List after inserting 2.5 after second node:")
    sll.printList()  # Expected output: 1 2 2.5 3 4 5

    # Delete a node
    sll.deleteNode(3)
    print("List after deleting node at position 3:")
    sll.printList()  # Expected output: 1 2 2.5 4 5

    # Search for a value
    print("Search for 4 in the list:")
    print(sll.search(4))  # Expected output: True

    print("Search for 6 in the list:")
    print(sll.search(6))  # Expected output: False

    # Sort the list
    sll.sortLinkedList()
    print("List after sorting:")
    sll.printList()  # Expected output: 1 2 2.5 4 5

    # Reverse the list
    sll.reverseList()
    print("List after reversing:")
    sll.printList()  # Expected output: 5 4 2.5 2 1

    # Test DoublyLinkedList
    dll = DoublyLinkedList()

    print("Testing DoublyLinkedList:")
    
    # Insert at the beginning
    dll.insertAtBeginning(3)
    dll.insertAtBeginning(2)
    dll.insertAtBeginning(1)
    print("List after inserting at beginning:")
    dll.printList()  # Expected output: 1 2 3

    # Insert at the end
    dll.insertAtEnd(4)
    dll.insertAtEnd(5)
    print("List after inserting at end:")
    dll.printList()  # Expected output: 1 2 3 4 5

    # Insert after a node
    second_node = dll.head.next
    dll.insertAfter(second_node, 2.5)
    print("List after inserting 2.5 after second node:")
    dll.printList()  # Expected output: 1 2 2.5 3 4 5

    # Delete a node
    dll.deleteNode(3)
    print("List after deleting node at position 3:")
    dll.printList()  # Expected output: 1 2 2.5 4 5

    # Search for a value
    print("Search for 4 in the list:")
    print(dll.search(4))  # Expected output: True

    print("Search for 6 in the list:")
    print(dll.search(6))  # Expected output: False

    # Sort the list
    dll.sortLinkedList()
    print("List after sorting:")
    dll.printList()  # Expected output: 1 2 2.5 4 5

    # Reverse the list
    dll.reverseList()
    print("List after reversing:")
    dll.printList()  # Expected output: 5 4 2.5 2 1
