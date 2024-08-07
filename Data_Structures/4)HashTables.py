"""
HashMap Implementation using Python's built-in dictionary.

This class demonstrates a simple hash map using Python's dictionary, which is internally implemented as a hash table.

HashMap Overview:
- A hash map is a data structure that maps keys to values for efficient data retrieval.
- Python's built-in dictionary is a type of hash map that uses a hash table under the hood.

Hash Table Techniques:
1. Separate Chaining:
   - Uses a list of lists (or another collection) where each index of the list holds a chain of key-value pairs.
   - Hash collisions are handled by appending new elements to the list at the index where the collision occurs.
   - Simple to implement but may lead to increased memory usage if many collisions occur.

2. Open Addressing:
   - All elements are stored in a single array (or table) and collisions are resolved by probing.
   - When a collision occurs, the hash table searches for the next available slot using a probing sequence.
   - Variants include:
     - Linear Probing: Searches for the next available slot sequentially.
     - Quadratic Probing: Uses a quadratic function to find the next slot.
     - Double Hashing: Uses a second hash function to determine the next slot, reducing clustering.

Load Factor and Resizing:
- The load factor is defined as the number of elements divided by the size of the hash table.
- A common threshold for resizing is when the load factor exceeds 0.7 (70%). 
- When this threshold is reached, the hash table is resized (usually doubled) to maintain efficient performance and reduce collisions.

Operations:
1. **Insert**: Insert data into the hash map with a given key.
2. **Delete**: Remove data from the hash map with a given key.
3. **Retrieve**: Retrieve data from the hash map using a given key.
4. **Print**: Print all key-value pairs in the hash map.

Time Complexity:
    - **Insert**: O(1) average case, O(n) worst case (if hash collisions occur frequently).
    - **Delete**: O(1) average case, O(n) worst case (if hash collisions occur frequently).
    - **Retrieve**: O(1) average case, O(n) worst case (if hash collisions occur frequently).
    - **Print**: O(n), where n is the number of elements in the hash map.

Applications:
    - Hash maps are commonly used for implementing associative arrays, database indexing, caches, and sets.
    - They are effective in scenarios where quick lookups, insertions, and deletions are required.

"""


class SimpleHashMap:
    def __init__(self):
        """
        Initialize the hash map using a dictionary.
        """
        self.hash_map = {}

    def insert_data(self, key: int, data: any) -> None:
        """
        Insert data into the hash map with the given key.

        Args:
            key (int): The key for the data.
            data (any): The data to be stored.

        Returns:
            None
        """
        self.hash_map[key] = data

    def remove_data(self, key: int) -> None:
        """
        Remove data from the hash map with the given key.

        Args:
            key (int): The key for the data to be removed.

        Returns:
            None
        """
        if key in self.hash_map:
            del self.hash_map[key]

    def get_data(self, key: int) -> any:
        """
        Retrieve data from the hash map using the given key.

        Args:
            key (int): The key for the data to be retrieved.

        Returns:
            any: The data associated with the key, or None if the key does not exist.
        """
        return self.hash_map.get(key, None)

    def print_table(self) -> None:
        """
        Print all key-value pairs in the hash map.

        Returns:
            None
        """
        for key, data in self.hash_map.items():
            print(f'{key}: {data}')


# Example usage
if __name__ == "__main__":
    # Create an instance of SimpleHashMap
    shm = SimpleHashMap()

    # Insert data
    shm.insert_data(1, 'Data 1')
    shm.insert_data(2, 'Data 2')
    shm.insert_data(3, 'Data 3')

    # Print hash map
    print("HashMap Contents:")
    shm.print_table()

    # Retrieve and print specific data
    print("Retrieve Data with Key 2:", shm.get_data(2))

    # Remove data
    shm.remove_data(2)

    # Print hash map after removal
    print("HashMap Contents after removal:")
    shm.print_table()
