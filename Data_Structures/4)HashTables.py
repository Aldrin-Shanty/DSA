# Just use Dictionaries

# Below HashMap Implementation
'''
class HashTable:
    def __init__(self, n):
        self.size = n
        self.hashTable = [[] for _ in range(n)]

    def checkPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def getPrime(self, n):
        if n % 2 == 0:
            n += 1
        while not self.checkPrime(n):
            n += 2
        return n

    def hash_function(self, key):
        return key % self.size

    def insertData(self, key, data):
        index = self.hash_function(key)
        self.hashTable[index].append((key, data))

    def removeData(self, key):
        index = self.hash_function(key)
        for i, (k, _) in enumerate(self.hashTable[index]):
            if k == key:
                del self.hashTable[index][i]
                return

    def printTable(self):
        for index, entry in enumerate(self.hashTable):
            print(index, end=' ')
            for key, data in entry:
                print(f'-->{(key, data)}', end=' ')
            print()
'''
