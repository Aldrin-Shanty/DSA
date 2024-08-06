"""
A Bloom Filter is a probabilistic data structure used to test whether an element is a member of a set. It allows for fast membership checking with a possibility of false positives but guarantees no false negatives.


Operations:
1. **Add**: Adds an item to the Bloom Filter. Uses hash functions to set bits in the bit array.
2. **Check**: Checks if an item is in the Bloom Filter. Returns True if the item may be in the filter (with a possible false positive), otherwise False.

Time Complexity:
    - **Add**: O(k), where 'k' is the number of hash functions. The time complexity is constant as the number of hash functions is fixed.
    - **Check**: O(k), where 'k' is the number of hash functions. The time complexity is constant as the number of hash functions is fixed.

Space Complexity:
    - The space complexity is O(m), where 'm' is the size of the bit array.

Applications:
    - Used in applications where space efficiency is crucial and occasional false positives are acceptable, such as in network systems, database systems, and spell checkers.
    - Commonly used to test membership of large datasets, especially when dealing with big data or streaming data where quick, approximate membership tests are required.
"""

import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        """
        Initialize the Bloom Filter.
        
        :param size: Size of the bit array.
        :param num_hashes: Number of hash functions.
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item):
        """
        Generate multiple hash values for an item.
        
        :param item: The item to hash.
        :return: List of hash values.
        """
        result = []
        for i in range(self.num_hashes):
            hash_value = int(hashlib.md5((item + str(i)).encode('utf-8')).hexdigest(), 16)
            result.append(hash_value % self.size)
        return result

    def add(self, item):
        """
        Add an item to the Bloom Filter.
        
        :param item: The item to add.
        """
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def check(self, item):
        """
        Check if an item is in the Bloom Filter.
        
        :param item: The item to check.
        :return: True if the item is possibly in the set, False if definitely not.
        """
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))

if __name__=="__main__":
    # Create a Bloom Filter with a bit array size of 10 and 3 hash functions
    bloom_filter = BloomFilter(size=10, num_hashes=3)
    
    # Add some items to the Bloom Filter
    items_to_add = ['apple', 'banana', 'cherry']
    for item in items_to_add:
        bloom_filter.add(item)
    
    # Test membership of added items
    for item in items_to_add:
        print(f"Check if '{item}' is in the Bloom Filter:", bloom_filter.check(item))  # Expected: True
    
    # Test membership of an item not added
    non_existent_item = 'grape'
    print(f"Check if '{non_existent_item}' is in the Bloom Filter:", bloom_filter.check(non_existent_item))  # Expected: False or True (False is preferable)
