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
